from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def job():
    print(datetime.now())

def start():
    print("apscheduler start..")
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=3)
    scheduler.start()