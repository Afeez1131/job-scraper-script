import string
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.jobzilla.ng/jobs'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

job_elem = soup.find('div', class_='container')
article_job = job_elem.find_all('article', class_='card')

for job in article_job:
    if 'footer' not in str(job):
        continue
    else:
        job_url = (job.find('h2')).find('a').attrs['href']
        job_name = job.find('h2')
        job_desc = job.find('footer')
        date = job.find('small')

        job_url = 'https://www.jobzilla.ng' + job_url
        title = job_name.text
        desc = job_desc.text.strip()
        description = re.sub(r'\s{2,4}', '', desc)
        date= date.string.strip()
        print('JOB URL:', job_url)
        print('Title :', title)
        print('Descriptin :', description)
        print('Date :', date)
        print('\n'*2)