from celery import shared_task
from time import sleep

@shared_task
def sleepy(s):
    sleep(s)