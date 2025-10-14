# Usar la imagen oficial de Airflow como base
FROM apache/airflow:2.7.0

# Instalar dbt y dbt-postgres en la imagen de Airflow
RUN pip install dbt-core dbt-postgres dbt-snowflake
RUN pip3 install awscli
RUN pip3 install awscli
USER root
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


USER airflow

    