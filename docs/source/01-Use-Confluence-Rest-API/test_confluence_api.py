# -*- coding: utf-8 -*-

import json
from pathlib import Path
import requests
from requests.auth import HTTPBasicAuth

base_url = "https://sanhehu.atlassian.net"
username = "husanhe@gmail.com"
api_token = (
    Path.home().joinpath(".atlassian", "sanhehu", "sanhe-dev.txt").read_text().strip()
)
auth = HTTPBasicAuth(username=username, password=api_token)

headers = {"Accept": "application/json"}
url = f"{base_url}/wiki/api/v2/spaces"
response = requests.get(
    url,
    headers=headers,
    auth=auth,
)
print(json.dumps(response.json(), indent=4))
