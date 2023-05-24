from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django_apscheduler.jobstores import register_events

from .views import get_dbdata, mv_recommend

def start():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    register_events(scheduler)
    scheduler.add_executor
    scheduler.add_job(
        mv_recommend,
        trigger=CronTrigger(hour="16", minute="33"),
        max_instances=1,
        name="DB_update(movie,genre)",
    )
    

    scheduler.start()