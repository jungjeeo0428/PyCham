from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

worker = BackgroundScheduler()
def fn_interval():
    print('interval', datetime.datetime.now())
def fn_cron():
    print('cron', datetime.datetime.now())
worker.add_job(fn_interval, 'interval', seconds=10)
worker.start()
print('Start!')