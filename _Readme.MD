# GIT -based project manager

## Description

The purpose of this repository is to help management of GIT -based projects, organized folder projects, downloading the repository and creating Tasks for VSCode

## Project Structure

- `./config.json`: Main configuration file.
- `./[PROJECT_NAME]`: Project root folder.
  - `./[PROJECT_NAME]/.vscode`: Visual Studio Code settings.
    - `./[PROJECT_NAME]/.vscode/tasks.json`: VSCode task settings.
- `main.py`: main script that is responsible for doing all the work
- `clean_install.py`: Script used for cleaning, removes all files and installation folders such as node_modles/, vendor/, package-lock.json, yarn.lock and compose.lock

## Installation

1. Clone this repository using the following command:

```
  git clone git@github.com:rodrigoadachi/projects-manager.git projects
  cd projects
```

2. Install the project premises:

```
  pip install gitpython
```

## Setup

```
{
  "projects": [
    {
      "path": "[PROJECT_NAME]",
      "config": {
        "path": "./"
      },
      "repositories": [
        {
          "path": "[REPOSITORY_NAME]", <<< -- Enter the name of the folder where the repository will be downloaded
          "repository": "[URL_GIT_REPOSITORY]" <<< -- Repository address
        }
        // Add more repositories if necessary
      ],
      "tasks": [
        {
          "label": "[REPOSITORY_NAME]", <<< -- Here you will define the name of the repository
          "command": "command_task", <<< -- For more information go to the VSCode Tasks documentation in https://code.visualstudio.com/docs/editor/tasks-appendix
          "group": "[GROUP_NAME]" <<< -- Name of Terminal Grouping in the VSCODE
        },
        // Add more tasks if necessary
      ]
    }
    // Add more projects if necessary
  ]
}
```

## Run

To create the folder structure and download the repositories just run the command below

```
  python main.py
```

To remove all files and installation folders, such as node_modles/, supplier/, package-lock.json, yarn.lock and compose.lock, just run the command below

```
  python clean_install.py
```
