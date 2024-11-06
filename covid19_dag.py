from datetime import datetime, timedelta
from airflow import DAG # type: ignore
from airflow.operators.python import PythonOperator # type: ignore
from airflow.utils.dates import days_ago # type: ignore
from airflow.hooks.S3_hook import S3Hook # type: ignore

from Covid19_ETL import run_covid19_etl # type: ignore

def upload_to_s3(filename:str, key:str, bucket_name:str):
    hook=S3Hook('aws_s3_conn')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)

default_args ={
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2024,11,6),
    'email':['airflow@example.com'],
    'email_on_failure':False,
    'eamil_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='dag_covid19_extract',
    description='Dag using python operator for covid19 stats',
    start_date=datetime(2024,11,6),
    schedule_interval='@daily'
) as dag:
    
    etl_run = PythonOperator(
        task_id='covid19_etl',
        python_callable=run_covid19_etl
    )

    s3_upload = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={'filename':'Covid_statistics.csv',
                   'key':'Covid_statistics.csv',
                   'bucket_name':'chiranjeevi-covid19-airflow-etl-project'}
    )


    etl_run >> s3_upload