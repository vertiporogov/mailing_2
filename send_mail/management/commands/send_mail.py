import logging

from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from datetime import timedelta, datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from send_mail.models import MailingModel

logger = logging.getLogger(__name__)


@util.close_old_connections
def start_mailing():
    logger.info('ggggggggggggggggggggggg')
    print('popopop')
    now = timezone.now()
    start_interval = now - timedelta(minutes=1)
    queryset = MailingModel.objects.filter(start_time__gte=start_interval, start_time__lte=now)
    for mailing in queryset:
        if mailing.period == 1 and mailing.start_time + datetime.timedelta(day=1) > now():
            client_email = list(mailing.clients.values_list('email', flat=True))
            body_massage = mailing.body_massage.body_massage
            subject_massage = mailing.body_massage.topic_massage
            send_mail(
                subject=subject_massage,
                message=body_massage,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=client_email,
                fail_silently=False
            )
        elif mailing.period == 2 and mailing.start_time + datetime.timedelta(month=1) > now():
            client_email = list(mailing.clients.values_list('email', flat=True))
            body_massage = mailing.body_massage.body_massage
            subject_massage = mailing.body_massage.topic_massage
            send_mail(
                subject=subject_massage,
                message=body_massage,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=client_email,
                fail_silently=False
            )
        elif mailing.period == 3 and mailing.start_time + datetime.timedelta(week=1) > now():
            client_email = list(mailing.clients.values_list('email', flat=True))
            body_massage = mailing.body_massage.body_massage
            subject_massage = mailing.body_massage.topic_massage
            send_mail(
                subject=subject_massage,
                message=body_massage,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=client_email,
                fail_silently=False
            )


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            start_mailing,
            trigger=CronTrigger(minute="*/1"),  # Every 10 seconds
            id="start_mailing",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )

        try:
            self.stdout.write("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            self.stdout.write("Stopping scheduler...")
            scheduler.shutdown()
            self.stdout.write("Scheduler shut down successfully!")
