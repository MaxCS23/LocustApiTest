from locust import HttpUser, constant
from locust_tests.tasks.combined_tasks import CombinedTasks


class HeavyUser(HttpUser):
    weight = 2
    wait_time = constant(1)
    host = "http://127.0.0.1:8000/"
    tasks = [CombinedTasks]
