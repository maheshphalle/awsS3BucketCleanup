import boto3
import datetime

# Define S3 bucket name
BUCKET_NAME = "mahesh-s3-cleanup-bucket"

def lambda_handler(event, context):
    s3 = boto3.client("s3")

    # Get current date
    current_date = datetime.datetime.now(datetime.timezone.utc)

    # List objects in the S3 bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    # Check if bucket is empty
    if "Contents" not in response:
        print("No files to delete.")
        return {"status": "No files to delete"}

    deleted_files = []

    # Iterate through each file in the bucket
    for obj in response["Contents"]:
        file_last_modified = obj["LastModified"]

        # Calculate file age
        file_age = (current_date - file_last_modified).days

        # Delete files older than 30 days
        if file_age > 30:
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj["Key"])
            deleted_files.append(obj["Key"])

    # Log deleted files
    if deleted_files:
        print("Deleted Files:", deleted_files)
    else:
        print("No old files found for deletion.")

    return {"status": "Cleanup complete", "deleted_files": deleted_files}
