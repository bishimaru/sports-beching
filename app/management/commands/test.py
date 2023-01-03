from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

class Command(BaseCommand):
    def handle(self, *args, **options):
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        url = "https://zenn.dev/"
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        r = requests.get(url)

        print(driver.title)
        driver.quit()
        
        print('hello world')
