import string
import requests
from bs4 import BeautifulSoup
import re

      
url = 'https://www.jobberman.com/jobs?page=1'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='search-main__content')

job_elem = results.find_all('article', class_="search-result")

for job in job_elem:
    if 'group' not in str(job):
        job_title = ((job.find('header', class_='search-result__header')).find('h3')).text.strip()
        job_url = (job.find('header', class_='search-result__header')).find('a').attrs['href']
        job_time = (job.find(class_='if-wrapper-column align-self--end text--right')).text.strip()
        content = (job.find('div', class_='search-result__content transform-y-center content-hide--under-md')).text.strip()

        print('Job title :', job_title)
        print('Job URL :', job_url)
        print('Job time :', job_time)
        print('Content :', content)
        print('\n')
    else:
        pass
