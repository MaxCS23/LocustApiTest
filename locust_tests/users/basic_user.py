from locust import HttpUser, between
from config import settings
from locust_tests.tasks.basic_tasks import BasicTasks


class BasicUser(HttpUser):
    weight = 3
    wait_time = between(settings.MIN_WAIT, settings.MAX_WAIT)
    host = settings.BASE_URL
    tasks = [BasicTasks]
