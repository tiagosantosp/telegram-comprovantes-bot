import boto3
from config.config import S3_BUCKET

s3 = boto3.client("s3")


def upload_file(filename, file_bytes):

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=filename,
        Body=file_bytes
    )

    return f"https://{S3_BUCKET}.s3.amazonaws.com/{filename}"
