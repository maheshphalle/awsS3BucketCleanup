# Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Project Overview
This project demonstrates how to automate the deletion of files older than 30 days in an Amazon S3 bucket using an AWS Lambda function written in Python with Boto3.

## Features
- Automatically deletes files older than 30 days in the specified S3 bucket.
- Uses AWS Lambda for serverless execution.
- IAM Role with Amazon S3 Full Access for Lambda function execution.
- Manual triggering and logging of deleted files.

## Prerequisites
- An AWS account.
- An S3 bucket named `mahesh-s3-cleanup-bucket`.
- IAM role named `mahesh-LambdaS3CleanupRole` with `AmazonS3FullAccess` permissions.
- Python 3.x runtime enabled in AWS Lambda.
- Git installed on your local machine.

## Setup Instructions
### Step 1: Create an S3 Bucket
1. Go to **AWS Console** > **S3**.
2. Click **Create Bucket** and name it `mahesh-s3-cleanup-bucket`.
3. Upload test files, including some older than 30 days.

### Step 2: Create an IAM Role
1. Navigate to **AWS Console** > **IAM** > **Roles**.
2. Click **Create Role** > **AWS Service** > **Lambda**.
3. Attach the `AmazonS3FullAccess` policy.
4. Name the role `mahesh-LambdaS3CleanupRole` and create it.

### Step 3: Create and Deploy the AWS Lambda Function
1. Go to **AWS Console** > **Lambda** > **Create Function**.
2. Choose **Author from scratch**.
3. Set function name: `S3CleanupFunction`.
4. Select **Python 3.x** as the runtime.
5. Assign **mahesh-LambdaS3CleanupRole** to the function.
6. Replace the default code with `lambda_function.py`.
7. Click **Deploy**.

### Step 4: Invoke the Lambda Function
1. Click **Test** in the Lambda dashboard.
2. Use a blank event `{}` and click **Invoke**.
3. Check **S3 bucket** to verify that old files were deleted.

## Running the Code Locally & Pushing to GitHub
1. Clone this repository:
   ```sh
   git clone [https://github.com/your-username/your-repo.git](https://github.com/maheshphalle/awsS3BucketCleanup.git)
   cd awsS3BucketCleanup
   ```
2. Add and commit changes:
   ```sh
   git add s3BucketCleanup.py
   git commit -m "Added S3 Cleanup Lambda function"
   git push origin main
   ```

## Screenshots
- Upload proof of execution as part of submission.

## Contribution
- Feel free to open issues or pull requests for improvements.

## License
This project is open-source and free to use.

---

### Author: Mahesh

