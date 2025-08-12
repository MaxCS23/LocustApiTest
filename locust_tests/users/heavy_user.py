from locust import HttpUser, constant
from locust_tests.tasks.slow_tasks import SlowTasks


class HeavyUser(HttpUser):
    wait_time = constant(1)
    host = "http://127.0.0.1:8000/"
    tasks = [SlowTasks]
