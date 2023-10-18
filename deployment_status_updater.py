#!/usr/bin/env python3

# pip install PyGithub
import os
import time
import github
import fire


def main(deployment_id: int) -> None:
  github_token = os.getenv('GITHUB_TOKEN')
  if not github_token:
    raise RuntimeError('Could not load Github token.')

  auth = github.Auth.Token(github_token)
  gh = github.Github(auth=auth)

  repo = gh.get_repo(os.getenv('GITHUB_REPOSITORY'))
  deployment = repo.get_deployment(deployment_id)

  deployment.create_status(state='success', description='From a python script', target_url='https://www.youtube.com')


if __name__ == '__main__':
  fire.Fire(main)