import requests
import os
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

#APP_ID = "f9d46aec"
#APP_KEY = "d929fd7cefd910a0aea4b2c7bf1d7498"


def fetch_real_jobs(role):

    url = (
        f"https://api.adzuna.com/v1/api/jobs/in/search/1"
        f"?app_id={APP_ID}"
        f"&app_key={APP_KEY}"
        f"&results_per_page=5"
        f"&what={role}"
    )

    response = requests.get(url)

    data = response.json()

    jobs = []

    if "results" in data:

        for item in data["results"]:

            jobs.append({

                "title": item.get("title"),

                "company": item.get(
                    "company", {}
                ).get("display_name"),

                "location": item.get(
                    "location", {}
                ).get("display_name"),

                "salary": item.get("salary_is_predicted"),

                "redirect_url": item.get("redirect_url")
            })

    return jobs