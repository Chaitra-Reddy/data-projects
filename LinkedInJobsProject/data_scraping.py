import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%2BAnalyst&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&start={}'
job_details_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
no_of_loops = 4
job_ids_list = list()
job_details = list()

# make the request to get list of jobs using a loop
for i in range(0, no_of_loops):
    resp = requests.get(target_url.format(25*(i+1)))
    soup = BeautifulSoup(resp.text, "html.parser")
    # html of jobs in current page
    all_jobs_current_page = soup.find_all("li")
    
    # make the request by job ID to get the details about the specific job
    for j in range(0, len(all_jobs_current_page)):
        # get the job ID
        try:
            job_id = all_jobs_current_page[j].find("div",{"class":"base-card"}).get("data-entity-urn").split(":")[3]
        except:
            job_id = all_jobs_current_page[j].find("a",{"class":"base-card"}).get("data-entity-urn").split(":")[3]
            
        job_ids_list.append(job_id)
        
        # get the details of that particular job by job ID
        each_job = dict()
        resp = requests.get(job_details_url.format(job_id))
        soup = BeautifulSoup(resp.text, "html.parser")
        
        try:
            each_job["company"] = soup.find("div", {"class":"top-card-layout__card"}).find("a").find("img").get("alt")
        except:
            each_job["company"] = None
            
        try:
            each_job["job_title"] = soup.find("h2", {"class":"top-card-layout__title"}).text
        except:
            each_job["job_title"] = None
            
        extra_details = soup.find_all("li", {"class":"description__job-criteria-item"})
        for each in extra_details:
            if "Seniority level" in each.text:
                try:
                    each_job["seniority"] = each.text.replace("Seniority level", "").strip()
                except:
                    each_job["seniority"] = None
            elif "Employment type" in each.text:
                try:
                    each_job["employment_type"] = each.text.replace("Employment type", "").strip()
                except:
                    each_job["employment_type"] = None
            elif "Job function" in each.text:
                try:
                    each_job["job_function"] = each.text.replace("Job function", "").strip()
                except:
                    each_job["job_function"] = None
            elif "Industries" in each.text:
                try:
                    each_job["industry"] = each.text.replace("Industries", "").strip()
                except:
                    each_job["industry"] = None
                    
        try:
            each_job["location"] = soup.find("span", {"class":"topcard__flavor topcard__flavor--bullet"}).text.strip()
        except:
            each_job["location"] = None
            
        try:
            each_job["posted_date"] = soup.find("span", {"class":"posted-time-ago__text"}).text.strip()
        except:
            each_job["posted_date"] = None
          
        # append the dict of all the scraped details into a list
        job_details.append(each_job)
        
# create a dataframe
df = pd.DataFrame(job_details)
print(df)

# convert df to a csv file
df.to_csv("jobs.csv", index=False, encoding="utf-8") 