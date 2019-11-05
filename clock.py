from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=17)
def scheduled_job():
    print('Test Job.')

sched.start()