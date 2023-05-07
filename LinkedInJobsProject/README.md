# LinkedIn Jobs Data Analysis Project

- In this project, we'll be scraping the job postings data from LinkedIn website and perform data cleaning and analysis on the data.

## High Level Steps

- Scrape job postings data using Python (**BeautifulSoup** library)
- Store the data in a *.csv* file using **Pandas** library
- Cleanup data using pandas (calculate days based on posted date column) and sql (remove empty rows, correct the rows where company name is not present, extract city name from location column)
- Show the findings using **Tableau**

## Files 

- **data_scraping.py** - Scraping of data, data storing in CSV file using pandas
- **jobs.csv** - Scraped data
- **sql_queries.txt** - SQL queries used for data cleanup
- **jobs_sql_cleaned.csv** - Cleaned up data after using only SQL
- **data_modify.py** - Cleaning and organizing data using pandas
- **jobs_cleaned.csv** - Cleaned data after using pandas and SQL both

<hr>

#### Click [here](https://public.tableau.com/app/profile/chaitra.reddy/viz/LinkeInJobsAnalysis/Dashboard1?publish=yes) to view the dashboard

<hr>

## Findings

- There are significantly more opening for entry level jobs in India
- Bangalore city has a lot of full-time data analyst jobs when compared to other cities
