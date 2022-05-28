#!/usr/bin/env python

## Script for talking to the gitlab API and listing my all projects 

import requests

response = requests.get("https://gitlab.com/api/v4/users/osher.levi7/projects")
my_project = response.json()

for project in my_project: 
    print(f"Project Name: {project['name']}\n Project URL: {project['web_url']}\n")