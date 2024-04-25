import os
import json
import git
from git import repo

repo = git.Repo(".")

commits = repo.iter_commits('HEAD^..HEAD')
#commits = repo.iter_commits(f'76ed97bb6da6f28f4d15a74bc70a5e9ddbde96cc..HEAD')

files_list = []

# Get the list of files against the commit
# and add it to files_list[] only if file path
# contains either 'datasources' or 'workbooks'

for commit in commits:
    for file in commit.stats.files:
        if file.__contains__('datasources/') or file.__contains__('workbooks/'):
            files_list.append(file)

print(json.dumps(files_list))
