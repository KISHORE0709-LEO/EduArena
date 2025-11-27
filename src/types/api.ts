export type APIRoute = (request: Request) => Promise<Response> | Response;
