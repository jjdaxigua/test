from celery import Celery

broker_url = 'redis://localhost:6379/1'
app = Celery("task", broker=broker_url, backend='redis://localhost:6379/2')


@app.task
def add(x, y):
    return x + y