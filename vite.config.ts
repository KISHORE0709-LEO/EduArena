import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { componentTagger } from "lovable-tagger";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => ({
  server: {
    host: "::",
    port: 8080,
    proxy: {
      "/api": {
        target: "http://localhost:8080",
        changeOrigin: true,
        configure: (proxy, options) => {
          proxy.on("error", (err, _req, _res) => {
            console.log("proxy error", err);
          });
          proxy.on("proxyReq", (proxyReq, req, _res) => {
            console.log("Sending Request:", req.method, req.url);
          });
          proxy.on("proxyRes", (proxyRes, req, _res) => {
            console.log("Received Response:", proxyRes.statusCode, req.url);
          });
        },
      },
    },
  },
  plugins: [
    react(),
    mode === "development" && componentTagger(),
    {
      name: "api-routes",
      configureServer(server: any) {
        server.middlewares.use(async (req: any, res: any, next: any) => {
          if (req.url?.startsWith("/api/")) {
            try {
              const routePath = req.url.replace("/api", "");
              const modulePath = path.resolve(
                __dirname,
                `./src/pages/api${routePath}.ts`
              );

              const module = await import(modulePath);
              const handler = module[req.method || "GET"];

              if (handler) {
                const request = new Request(
                  `http://${req.headers.host}${req.url}`,
                  {
                    method: req.method,
                    headers: req.headers as Record<string, string>,
                    body:
                      req.method !== "GET" && req.method !== "HEAD"
                        ? await new Promise<string>((resolve) => {
                            let body = "";
                            req.on("data", (chunk: any) => {
                              body += chunk.toString();
                            });
                            req.on("end", () => resolve(body));
                          })
                        : undefined,
                  }
                );

                const response = await handler(request);
                res.statusCode = response.status;
                response.headers.forEach((value: string, key: string) => {
                  res.setHeader(key, value);
                });
                res.end(await response.text());
                return;
              }
            } catch (error) {
              console.error("API route error:", error);
              res.statusCode = 500;
              res.end(JSON.stringify({ error: "Internal server error" }));
              return;
            }
          }
          next();
        });
      },
    },
  ].filter(Boolean),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
}));
