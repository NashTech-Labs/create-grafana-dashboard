from grafana_api.grafana_face import GrafanaFace
import os
from grafanalib._gen import DashboardEncoder
import json
import requests

def create_grafana_dashboard(json, verify=True):
    try:
        server=os.getenv('GRAFANA_HOST','localhost:3000')
        api_key=os.getenv('GRAFANA_API_TOKEN','None')
        headers = {'Authorization': f"Bearer {api_key}", 'Content-Type': 'application/json'}
        r = requests.post(f"http://{server}/api/dashboards/db", data=json, headers=headers, verify=verify)
        # TODO: add error handling
        print(f"{r.status_code} - {r.content}")
        if r.status_code == 200:
            dashboard = r.json()
            return dashboard
        else:
            dashboard={
                "id":-1,
                "slug":"None",
                "status":"failed",
                "uid":"None",
                "url":"None",
                "version":2
            }
            return dashboard
    except Exception as e:
        print("Error in Creating Dashboard:\n{}".format(e))
        dashboard={
                "id":-1,
                "slug":"kNone",
                "status":"failed",
                "uid":"None",
                "url":"None",
                "version":2
            }
        return dashboard
