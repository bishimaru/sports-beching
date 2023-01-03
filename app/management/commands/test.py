from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://www.yahoo.co.jp/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        test = soup.find('div', class_='cdcrk1cfotq338-label-1')
        print('hello world')
