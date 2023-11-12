import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from datawagon.etl.update_station_id import run as run_update_station_id


default_args = {
    "owner": "airflow",
    "retries": None,
}

dag_update_station_id = DAG(
    dag_id="dag_update_station_id",
    default_args=default_args,
    description="Autodump postgresql",
    schedule=None,
    max_active_runs=1,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    tags=["datawagon"],
    catchup=False,
)


update_station_id = PythonOperator(
    python_callable=run_update_station_id,
    task_id="dag_update_station_id",
    dag=dag_update_station_id,
)

update_station_id
