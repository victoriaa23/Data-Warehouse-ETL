from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract_s3 import extract
from validations.validate_inputs import validate_inputs
from etl.transform import transform
from validations.validate_outputs import validate_outputs
from etl.load_s3_parquet import save_to_s3

def run_etl():
    products, sales = extract()
    products, sales = validate_inputs(products, sales)
    df = transform(products, sales)
    df = validate_outputs(df)
    save_to_s3(df, "processed/sales_clean.parquet")

with DAG(
    dag_id="retail_etl_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
):
    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )
