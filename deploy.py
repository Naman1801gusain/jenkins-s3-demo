import boto3
import os
import mimetypes

# --- CONFIGURATION ---
BUCKET_NAME = "jenkins-naman-website-2025"  # <--- YOUR BUCKET
S3_REGION = "ap-south-1"

def deploy():
    s3 = boto3.client('s3')
    print("-----------------------------------------")
    print(f"🚀 Starting BULK upload to: {BUCKET_NAME}")

    # Walk through all files in the current directory
    for root, dirs, files in os.walk("."):
        for file in files:
            # Skip sensitive or unnecessary files
            if ".git" in root or file in ["deploy.py", "Jenkinsfile", ".gitignore"]:
                continue

            # Create the full local path
            local_path = os.path.join(root, file)
            
            # Create the S3 path (relative to the folder)
            # This handles subfolders correctly (e.g., css/style.css)
            relative_path = os.path.relpath(local_path, ".")
            s3_path = relative_path.replace("\\", "/") # Fix for Windows paths

            # Guess the file type (HTML, PNG, CSS) so browser opens it correctly
            content_type, _ = mimetypes.guess_type(local_path)
            if content_type is None:
                content_type = 'application/octet-stream'

            try:
                print(f"📤 Uploading: {s3_path} ...")
                s3.upload_file(
                    local_path, 
                    BUCKET_NAME, 
                    s3_path, 
                    ExtraArgs={'ContentType': content_type} # Important for websites!
                )
            except Exception as e:
                print(f"❌ Failed to upload {file}: {e}")
                exit(1)

    print("-----------------------------------------")
    print("✅ All files uploaded successfully!")
    print(f"🌍 Live URL: http://{BUCKET_NAME}.s3-website.{S3_REGION}.amazonaws.com")

if __name__ == "__main__":
    deploy()
