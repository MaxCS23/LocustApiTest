
def error_500(TaskSet):
    TaskSet.client.get("/error500", name="Getting Error 500")


def error_404(TaskSet):
    TaskSet.client.get("/error404", name="Getting Error 404")
