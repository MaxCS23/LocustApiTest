from locust import HttpUser, constant
from config import settings
from locust_tests.tasks.data_tasks import DataTasks


class DataUser(HttpUser):
    weight = 1
    wait_time = constant(settings.MIN_WAIT)
    host = settings.BASE_URL
    tasks = [DataTasks]
