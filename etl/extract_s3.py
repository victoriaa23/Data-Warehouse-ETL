import boto3
import pandas as pd
import io
import yaml

config = yaml.safe_load(open("include/config.yaml"))

def read_s3_json(key):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=config["aws"]["access_key_id"],
        aws_secret_access_key=config["aws"]["secret_access_key"],
        region_name=config["aws"]["region"]
    )
    obj = s3.get_object(Bucket=config["aws"]["raw_bucket"], Key=key)
    return pd.read_json(io.BytesIO(obj["Body"].read()))

def read_s3_csv(key):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=config["aws"]["access_key_id"],
        aws_secret_access_key=config["aws"]["secret_access_key"],
        region_name=config["aws"]["region"]
    )
    obj = s3.get_object(Bucket=config["aws"]["raw_bucket"], Key=key)
    return pd.read_csv(io.BytesIO(obj["Body"].read()))

def extract():
    products = read_s3_json("raw/product_data.json")
    sales = read_s3_csv("raw/sales_data.csv")
    return products, sales
