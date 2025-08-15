from locust import HttpUser, constant
from locust_tests.tasks.combined_tasks import CombinedTasks
from config import settings


class HeavyUser(HttpUser):
    weight = 2
    wait_time = constant(settings.MIN_WAIT)
    host = settings.BASE_URL
    tasks = [CombinedTasks]
