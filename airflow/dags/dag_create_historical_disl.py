import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from datawagon.etl.create_historical_disl import run as run_create_historical_disl


default_args = {
    "owner": "airflow",
    "retries": None,
}

dag_create_historical_disl = DAG(
    dag_id="dag_create_historical_disl",
    default_args=default_args,
    description="Autodump postgresql",
    schedule="0 0 * * 3",
    max_active_runs=1,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    tags=["datawagon"],
    catchup=False,
)


create_historical_disl = PythonOperator(
    python_callable=run_create_historical_disl,
    task_id="dag_create_historical_disl",
    dag=dag_create_historical_disl,
)

create_historical_disl
