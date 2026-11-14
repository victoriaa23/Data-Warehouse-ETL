import boto3
import io
import yaml

config = yaml.safe_load(open("include/config.yaml"))

def save_to_s3(df, key):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=config["aws"]["access_key_id"],
        aws_secret_access_key=config["aws"]["secret_access_key"],
        region_name=config["aws"]["region"]
    )
    out_buffer = io.BytesIO()
    df.to_parquet(out_buffer, index=False)
    s3.put_object(Bucket=config["aws"]["processed_bucket"], Key=key, Body=out_buffer.getvalue())
