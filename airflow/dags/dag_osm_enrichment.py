import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from datawagon.etl.geofabrik_download import run as run_geofabrik_download
from datawagon.etl.osm_enrichment import run as run_osm_enrichment


default_args = {
    "owner": "airflow",
    "retries": None,
}

dag_osm_enrichment = DAG(
    dag_id="dag_osm_enrichment",
    default_args=default_args,
    description="Enrichment OSM data",
    schedule="0 0 * * 3",
    max_active_runs=1,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    tags=["datawagon"],
    catchup=False,
)


geofabrik_download = PythonOperator(
    python_callable=run_geofabrik_download,
    task_id="geofabrik_download",
    dag=dag_osm_enrichment,
)


osm_enrichment = PythonOperator(
    python_callable=run_osm_enrichment,
    task_id="osm_enrichment",
    dag=dag_osm_enrichment,
)

geofabrik_download >> osm_enrichment
