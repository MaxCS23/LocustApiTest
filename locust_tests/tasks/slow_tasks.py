from locust import TaskSet, task


class SlowTasks(TaskSet):
    @task
    def slow(self):
        self.client.get("/slow", name="Accessing Slow route")
