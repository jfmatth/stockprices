from django.core.management.base import BaseCommand

import logging
from datetime import date

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "loads all stock symbols from IEX_CLOUD"

    def handle(self, *args, **options):
        download()

def download():
    from prices.models import Download, Price, Symbol

    import pyEX
    # check the first character to see if it's T or not.
    environment = ("sandbox" if settings.IEX_TOKEN[0] == "T" else "v1") 
    pyClient = pyEX.Client(version=environment)

    logger.info(f"Downloading")

    today = date.today()
    todaystr = str(today)

    for symbol in Download.objects.all().distinct():
        logger.info(f"Downloading today's price for {symbol}")

        


    logger.info(f'done')