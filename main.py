from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
day = datetime.now().strftime("%A")
utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")



@app.get('/api')
def api(slack_name: str, track: str):
    return {
        "slack_name": f"{slack_name}",
        "current_day": f"{day}",
        "utc_time": f"{utc_time}",
        "track": f"{track}",
        "github_file_url": "https://github.com/baccrie/Hng_Internship_Task1/blob/main/main.py",
        "github_repo_url": "https://github.com/baccrie/Hng_Internship_Task1",
        "status_code": 200
    }