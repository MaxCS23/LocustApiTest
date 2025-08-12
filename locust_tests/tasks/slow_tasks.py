

def slow(TaskSet):
    TaskSet.client.get("/slow", name="Accessing Slow route")
