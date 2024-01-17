import os
import subprocess
import json

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Pasta criada em: {path}")
    except OSError as error:
        print(f"Falha ao criar pasta: {error}")

def download_repository(url, path):
    try:
        subprocess.run(["git", "clone", url, path])
        print(f"Repositório baixado em: {path}")
    except Exception as e:
        print(f"Falha ao baixar repositório: {e}")

def create_tasks(project):
    tasks_json = {
        "version": "2.0.0",
        "configurations": {
            "type": "node",
            "runtimeVersion": "14.21.3",
            "request": "launch",
            "name": "Launch",
            "preLaunchTask": "",
        },
        "presentation": {
            "echo": False,
            "reveal": "always",
            "focus": False,
            "panel": "dedicated",
            "showReuseMessage": True
        },
        "tasks": []
    }

    dependencies = set()
    depends_on_set = set()

    for task in project.get('tasks', []):
        task_entry = {
            "label": task['label'],
            "type": "shell",
            "command": task['command'],
            "isBackground": True,
            "problemMatcher": [],
            "presentation": {},
            "dependsOn": []
        }

        # Add 'group' if it exists
        if 'group' in task:
            task_entry["presentation"]["group"] = task['group']

        # Adiciona 'dependsOn' se existir
        if 'dependsOn' in task:
            task_entry["dependsOn"] = task['dependsOn']
            depends_on_set.update(task['dependsOn'])
            
        tasks_json['tasks'].append(task_entry)
        dependencies.add(task['label'])

    # Removes the tasks that are 'Dependon' from others
    dependencies.difference_update(depends_on_set)
    
    # Adds the "Create Terminals" input only if there are dependencies
    create_terminals_entry = {
      "label": "Create terminals",
      "dependsOn": list(dependencies),
      "group": {
          "kind": "build",
          "isDefault": True
      },
      "runOptions": {
          "runOn": "folderOpen"
      }
    }

    tasks_json['tasks'].append(create_terminals_entry)

    return tasks_json

def process(project):
    config_path = project.get('config', {}).get('path', './')
    root_folder = os.path.join(config_path, project['path'])
    create_folder(root_folder)

    # Processes the repository in the project
    for repo in project['repositories']:
        folder_destination = os.path.join(root_folder, repo['path'])
        url_repository = repo['repository']

        create_folder(folder_destination)
        download_repository(url_repository, folder_destination)

    # Creates the .vscode directory and the Tasks.json file inside it
    vscode_path = os.path.join(root_folder, '.vscode')
    create_folder(vscode_path)
    tasks_json_path = os.path.join(vscode_path, 'tasks.json')
    tasks_json_content = create_tasks(project)

    with open(tasks_json_path, 'w') as tasks_file:
        json.dump(tasks_json_content, tasks_file, indent=2)

def read_config_json(config_json):
    with open(config_json) as f:
        data = json.load(f)

        for project in data.get('projects', []):
            config_path = project.get('config', {}).get('path', './')
            project['config'] = {'path': config_path}
            process(project)

config_json = "./config.json"
read_config_json(config_json)
