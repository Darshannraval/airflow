from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'kubernetes_hello_world', default_args=default_args, schedule_interval=timedelta(minutes=10))


start = DummyOperator(task_id='start', dag=dag)

passing = KubernetesPodOperator(namespace='default',
                          service_account_name="mynewsa",
                          image="python:3.6",
                          cmds=["python","-c"],
                          arguments=["print('hello Kubernetes')"],
                          labels={"foo": "bar"},
                          name="passing-test",
                          task_id="passing-task",
                          get_logs=True,
                          dag=dag
                          )
