import boto3
import os

# --- CONFIGURATION ---
BUCKET_NAME = "jenkins-deployment-naman-01"  # <--- REPLACE WITH YOUR BUCKET NAME
FILE_TO_UPLOAD = "index.html"
S3_FILE_NAME = "index.html"

def deploy_to_s3():
    print(f"🚀 Starting upload to bucket: {BUCKET_NAME}...")

    # Initialize S3 Client
    s3 = boto3.client('s3')

    try:
        # Upload the file
        s3.upload_file(FILE_TO_UPLOAD, BUCKET_NAME, S3_FILE_NAME)
        print("✅ Upload Successful!")
        print(f"🌍 Your site should be live at: http://{BUCKET_NAME}.s3-website.ap-south-1.amazonaws.com")
        
    except Exception as e:
        print(f"❌ Error uploading to S3: {e}")
        exit(1) # Fail the build if upload fails

if __name__ == "__main__":
    deploy_to_s3()
