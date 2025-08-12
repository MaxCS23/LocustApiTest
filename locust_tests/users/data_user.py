from locust import HttpUser, constant
from locust_tests.tasks.data_tasks import DataTasks


class DataUser(HttpUser):
    weight = 1
    wait_time = constant(1)
    host = "http://127.0.0.1:8000/"
    tasks = [DataTasks]
