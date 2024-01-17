import os
import json

import shutil

def backup_env_files(config_folder, project):
    for repo in project['repositories']:
        repo_path = os.path.join(project['path'], repo['path'])
        env_file_path = os.path.join(repo_path, '.env')

        if os.path.exists(env_file_path):
            backup_name = f"{project['name']}-{repo['path']}.env"
            backup_path = os.path.join(config_folder, backup_name)

            shutil.copy(env_file_path, backup_path)
            print(f"Arquivo .env em {repo_path} copiado para {backup_path}")

def read_config_json(config_json):
    with open(config_json) as f:
        data = json.load(f)

        for project in data.get('projects', []):
            config_path = project.get('config', {}).get('path', './')
            config_folder = os.path.join(config_path, 'config')

            backup_env_files(config_folder, project)

config_json = "./config.json"
read_config_json(config_json)
