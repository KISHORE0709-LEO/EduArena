import os
import requests
import zipfile
import shutil
from pathlib import Path

def download_with_progress(url, filename):
    """Download file with progress indicator"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\rDownloading: {percent:.1f}%", end='', flush=True)
        print()  # New line after progress
        return True
    except Exception as e:
        print(f"\nDownload failed: {e}")
        return False

def install_ffmpeg():
    """Download and install FFmpeg for Windows"""
    
    # Use a smaller, faster download
    ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    download_path = "ffmpeg.zip"
    extract_path = "ffmpeg_temp"
    final_path = "ffmpeg"
    
    print("Downloading FFmpeg (this may take a few minutes)...")
    
    if not download_with_progress(ffmpeg_url, download_path):
        print("Download failed. Please install FFmpeg manually.")
        return False
        
    try:
        print("Extracting FFmpeg...")
        os.makedirs(extract_path, exist_ok=True)
        
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        
        # Find and move the bin folder
        for root, dirs, files in os.walk(extract_path):
            if 'bin' in dirs and 'ffmpeg.exe' in os.listdir(os.path.join(root, 'bin')):
                src_bin = os.path.join(root, 'bin')
                if os.path.exists(final_path):
                    shutil.rmtree(final_path)
                shutil.copytree(src_bin, final_path)
                break
        
        # Cleanup
        os.remove(download_path)
        shutil.rmtree(extract_path)
        
        # Test installation
        ffmpeg_exe = os.path.join(final_path, 'ffmpeg.exe')
        if os.path.exists(ffmpeg_exe):
            print(f"✓ FFmpeg installed successfully to: {os.path.abspath(final_path)}")
            print("\nTo use FFmpeg permanently, add this to your system PATH:")
            print(f"  {os.path.abspath(final_path)}")
            return True
        else:
            print("✗ Installation failed - ffmpeg.exe not found")
            return False
            
    except Exception as e:
        print(f"Error installing FFmpeg: {e}")
        return False

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("Installing requests...")
        import subprocess
        subprocess.check_call(["pip", "install", "requests"])
        import requests
    
    success = install_ffmpeg()
    if success:
        print("\nFFmpeg is ready to use!")
    else:
        print("\nManual installation required. Visit: https://ffmpeg.org/download.html")