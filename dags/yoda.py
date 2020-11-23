from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 17),
    'email': ['leonardo.nascimento@example.com.br'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'yoda', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='yoda_greets_you',
    bash_command='echo "Master Yoda greets you..."',
    dag=dag)

t2 = BashOperator(
    task_id='yoda_analyzes_you',
    bash_command='echo "Master Yoda is analizing you..."',
    dag=dag)

t3 = BashOperator(
    task_id='yoda_advises_you',
    bash_command='python /usr/local/airflow/scripts/python/yoda.py',
    dag=dag)

# t3 = PythonOperator(
#     task_id='yoda_advises_you',
#     python_callable=get_advice,
#     # op_args=['arguments_passed_to_callable'],
#     # op_kwargs={'keyword_argument': 'which will be passed to function'}
#     dag=dag)

# setting up dependecies
t1 >> t2 >> t3
