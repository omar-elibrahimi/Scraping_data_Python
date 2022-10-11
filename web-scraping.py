#1st
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


job_title = []
company_name = []
location_name = []
skills = []

#2end step use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

#3rd step save page content/markup
src = result.content

#4th step create soup object to parse content
soup = BeautifulSoup(src, "lxml")

#5th step find the element needed job , titles , skills, names, location names
job_title = soup.find_all("h2", {"class":"css-m604qf"})
company_name = soup.find_all("a", {"class":"css-17s97q8"}) 
location_name = soup.find_all("span", {"class":"css-5wys0k"})
skills = soup.find_all("div", {"class":"css-y4udm8"})

#6th step loop over returned lists to extract info into other lists
for i in range(len(job_title)):
    job_title.append(job_title[i].text)
    company_name.append(company_name[i].text)
    location_name.append(location_name[i].text)
    skills.append(skills[i].text)




#7th step create csv file and fill it with values

with open("test.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title", "Company name", "Location", "skills"])
    wr.writerows([job_title, company_name, location_name, skills])