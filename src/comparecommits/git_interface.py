import requests
import json
from requests.structures import CaseInsensitiveDict

#https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28#get-a-commit
def get_commits(org, repo):
    try:
        url = "https://api.github.com/repos/" + org + "/" + repo + "/commits"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            parsed_resp = json.loads(resp.content)
        return parsed_resp
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

# https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28#compare-two-commits
def compare_commits(org, repo, base, head):
    try:
        url = "https://api.github.com/repos/" + org + "/" + repo + "/compare/" + base + "..." + head
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            parsed_resp = json.loads(resp.content)
        return parsed_resp
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise