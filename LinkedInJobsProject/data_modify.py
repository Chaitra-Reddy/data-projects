import pandas as pd
import numpy as np


def main():
    
    # read the data into a dataframe
    df = pd.read_csv(".\jobs_sql_cleaned.csv")

    # replace NAN values with emoty string
    df.replace(np.nan, "", inplace=True)

    # calculate number of date from posted date column
    df["days"] = df["posted_date"].apply(get_days)
    
    # convert dataframe to csv file
    df.to_csv("jobs_cleaned.csv", index=False, encoding="utf-8")
    
    
def get_days(posted_time_str):
    posted_time_str = str(posted_time_str)
    count = int(posted_time_str.split(" ")[0])
    if "week" in posted_time_str:
        return count * 7
    elif "day" in posted_time_str:
        return count
    elif "month" in posted_time_str:
        return count * 30
    else:
        return 0
        
    
if __name__ == "__main__":
    main()
