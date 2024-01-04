# Project Automation Scripts

## main.py

This project aims to help developers set up their projects quickly and in a standardized way. It performs three main actions: creating folders, cloning Git repositories, and generating task configurations for Visual Studio Code. To use it, follow the instructions below:

### Setting Up the Project

Before getting started, it's essential to configure the project by following these steps:

1. Download and install Python (3.6 or higher) on your machine if you haven't already. You can do this by visiting python.org.

2. Download and install Git on your machine if you haven't already. You can do this by visiting git-scm.com.

3. Before running the script for the first time, open the terminal and execute the following command to install the necessary dependency:

   ```bash
   pip install gitpython
   ```

### How to Use

1. Edit the config.json file to configure your projects and repositories.

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
          "command": "command_task", <<< -- For more information, go to the VSCode Tasks documentation at https://code.visualstudio.com/docs/editor/tasks-appendix
          "group": "[GROUP_NAME]" <<< -- Name of Terminal Grouping in VSCODE
        },
        // Add more tasks if necessary
      ]
    }
    // Add more projects if necessary
  ]
}

```

2. Execute the script using the command python main.py.

The script will create folder structures, download repositories, and generate configurations for VS Code.

## clean_install.py

This Python script performs specific cleanup in all subdirectories, excluding unnecessary folders and files. It is useful for preparing the environment for a clean installation or compression. Follow the instructions below to use it:

### How to Use - clean_install.py

1. Execute the script using the command python clean_install.py. Make sure to run the script in the folder where you want to perform the cleanup; it will check all subfolders for files such as package-lock.json, yarn.lock, composer.lock, and folders like node_modules, vendor to remove them.

The script will remove the specified folders recursively, ensuring a clean installation.

---

**Nota:** Make sure to understand the implications of these scripts before running them, especially when deleting folders and files.
