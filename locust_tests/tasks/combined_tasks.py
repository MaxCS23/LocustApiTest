from locust import task, SequentialTaskSet

from locust_tests.tasks.error_tasks import error_404, error_500
from locust_tests.tasks.slow_tasks import slow


class CombinedTasks(SequentialTaskSet):

    @task(3)
    def slow_task(self):
        slow(self)

    @task(1)
    def error_500_task(self):
        error_500(self)

    @task(1)
    def error_404_task(self):
        error_404(self)
