import os
from ghapi.core import GhApi

api = GhApi(owner='radikon', repo='wandb-cicd')

for pr in api.pulls.list():
    print(pr.title, pr.number, pr.html_url)

comment = api.issues.create_comment(5, "/bug")

from ghapi.event import load_sample_events

evts = load_sample_events()

comments[0].payload.issue.number, comments[0].payload.comment.body

comments[0].payload

api = GhApi(owner='radikon', repo='wandb-cicd')

branch_name = 'hamelsmu-patch-12'
runid = '647ubuzj'

result = api.repos.create_deployment(ref=branch_name, 
                                     payload={'runid': runid})

result.id

deployment = api.repos.create_deployment_status

