from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
date = datetime.now()
utc = datetime.utcnow().isoformat()


@app.get('/api')
def api(slack_name: str, track: str):
    return {
        "slack_name": f"{slack_name}",
        "current_day": f"{date.strftime('%A')}",
        "utc_time": f"{utc}",
        "track": f"{track}",
        "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
        "github_repo_url": "https://github.com/username/repo",
        "status_code": 200
    }
