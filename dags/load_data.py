import time
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 21),
}

def load_index(index_id):
    url = 'http://5.63.114.131:8000/api/v1/loader/insert-index-data/'
    token = 'f835150d7ae7e67ccfedb633944c86591d54c791'
    headers = {'Authorization': 'Token ' + token}
    data = {'index_id': index_id}
    response = requests.post(url, headers=headers, json=data)
    print(response.text)


with DAG('data_load', default_args=default_args, catchup=False, concurrency=1, max_active_runs=1, schedule_interval=None) as dag:
    index_ids = [701276,702974,702972,702976,704447,704448,704449,704498,19722414,
             2709379,2709380,701188,701592,703831,701625,701227,701228,701925,701939,702022,
             702041,700917,4023003,4023004,701830,701852,703076,703039,2979005,702740,4244622, 
             702742,3782164,702944,702943,702840,702835,703857,701608,701850,700925,700916,20558808,
             700899,700908,2709378,700907,2709376,700970,700967,700966,700965,2709436]
    for index_id in index_ids:
        task_id = f"load_index_id_{index_id}"
        PythonOperator(
            task_id=task_id,
            python_callable=load_index,
            op_kwargs={'index_id': index_id}
        )


