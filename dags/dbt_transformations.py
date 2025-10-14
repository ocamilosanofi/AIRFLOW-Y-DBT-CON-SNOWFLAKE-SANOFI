from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import base64
import boto3
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.backends import default_backend 


def get_secret(secret_name, region_name="eu-west-1"): 
    client = boto3.client("secretsmanager", region_name=region_name) 
    response = client.get_secret_value(SecretId=secret_name) 
    secret_string = response.get("SecretString") 
    return secret_string  
 
private_key_pem_str = get_secret("PROJECT/chc-ecommerce-analytics/MWAA_ECOMM_DEV_TRANSFORM_KEY") 
private_key_passphrase_str = get_secret("PROJECT/chc-ecommerce-analytics/MWAA_ECOMM_DEV_TRANSFORM_KEY_PASSPHRASE") 

my_env = {
    "SNOWFLAKE_PRIVATE_KEY": private_key_pem_str,
    "SNOWFLAKE_PRIVATE_KEY_PASSPHRASE" : private_key_passphrase_str,
    "DBT_PROFILES_DIR": "/opt/airflow/mi_proyecto_dbt"
}

default_args = {
    'owner': 'airflow',
    'retries': 0,
}

dag = DAG(
    'dbt_transformations',
    default_args=default_args,
    description='Run dbt transformations',
    schedule_interval='@daily',
    start_date=days_ago(1),
)

run_dbt = BashOperator(
    task_id='run_dbt',
    bash_command='echo "hola mundo"; /home/airflow/.local/bin/dbt debug --project-dir /opt/airflow/mi_proyecto_dbt --profile chc_ecommerce_analytics',
    dag=dag,
    env=my_env,
)

run_dbt
