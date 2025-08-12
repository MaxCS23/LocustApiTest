from locust import HttpUser, between
from locust_tests.tasks.basic_tasks import BasicTasks


class BasicUser(HttpUser):
    weight = 3
    wait_time = between(2, 5)
    host = "http://127.0.0.1:8000/"
    tasks = [BasicTasks]
