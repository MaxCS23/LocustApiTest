from locust import task, TaskSet


class BasicTasks(TaskSet):
    @task(3)
    def home(self):
        self.client.get("/", name="Accessing Home Page")

    @task(1)
    def about(self):
        self.client.get("/about", name="Accessing About Page")
