#!/usr/bin/env python3
import os
import sys

def create_folders(folder_list):
    for folder in folder_list:
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"Created directory: {folder}")
        except Exception as e:
            print(f"Error creating directory {folder}: {e}", file=sys.stderr)

def main():
    # Define a list of folder paths as you need
    folders = [
        "./tests",
        "./infra/terraform/modules/aks",
        "./infra/terraform/modules/network",
        "./infra/terraform/modules/database",
        "./infra/terraform/environments/dev",
        "./infra/terraform/environments/prod",
        "./infra/k8s/base",
        "./infra/k8s/overlays/dev",
        "./infra/k8s/overlays/prod",
        "./infra/ansible/roles/nginx",
        "./infra/ansible/roles/flask",
        "./infra/ansible/environments/dev",
        "./infra/ansible/environments/prod",
        "./ci-cd/jenkins/pipelines",
        "./ci-cd/jenkins/shared-libraries/vars",
        "./scripts",
        "./docs",
    ]

    create_folders(folders)

if __name__ == "__main__":
    main()
