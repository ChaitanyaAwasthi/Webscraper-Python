from bs4 import BeautifulSoup
import requests
import time 

print("Please type out skills you are unfamiliar with")
unfamiliar_skills = input('>')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace('  ', ' ')
            more_info = job.header.h2.a['href']

            if unfamiliar_skills.lower() not in skills.lower():
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company: {company_name.strip()}\nSkills: {skills.strip()}\nPublished Date: {published_date}\nMore Info: {more_info}")
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True: 
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
