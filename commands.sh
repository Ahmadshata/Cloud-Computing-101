aws s3 ls  # List all S3 buckets in your AWS account

aws s3 ls s3://BUCKET_NAME/  # List objects (files) inside a specific S3 bucket

aws s3 cp PATH_TO_LOCAL_FILE s3://BUCKET_NAME/  # Upload a file from local system to S3 bucket

aws s3 cp s3://BUCKET_NAME/FILE_NAME -  # Display the content of a file stored in S3
