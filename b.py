# from datetime import datetime
# from airflow import DAG
# from customoperator.hello_operator import HelloOperator #import form customoperator folder


# dag = DAG('custom_operator', description='custom operator DAG',
#           schedule_interval='0 12 * * *',
#           start_date=datetime(2017, 3, 20), catchup=False)
#           # create dag name is : operator dag

# hello_task = HelloOperator(task_id="airflow-task", name="airflow", dag=dag)

# hello_task


import hello_operator
from threading import Event # Needed for the  wait() method
from time import sleep     

print("Calling Operator")
print("\n wait for 100 sec start")

hello_operator.HelloOperator.execute()
sleep(100)  
print("Execute custom operator")