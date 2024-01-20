import subprocess
import time
import yaml
import os
import json

# Leitura do arquivo de configuração JSON
config_path = "./config.json"
with open(config_path, "r") as config_file:
    config_data = json.load(config_file)

# Caminho base do projeto
project_base_path = config_data["config"]["path"]
config_output_path = "./config"

def has_changes(repo_path):
    # Obtém o status do branch remoto em relação ao branch local
    result_status = subprocess.run(["git", "-C", repo_path, "status", "-uno", "--porcelain"], capture_output=True, text=True)
    return bool(result_status.stdout.strip())


def get_remote_head_sha(repo_path):
    # Executa git fetch para atualizar as referências remotas
    subprocess.run(["git", "-C", repo_path, "fetch"])

    # Obtém o SHA-1 do commit mais recente no branch remoto
    result = subprocess.run(["git", "-C", repo_path, "rev-parse", "origin/master"], capture_output=True, text=True)
    
    return result.stdout.strip()

def run_pipeline_commands(commands, repo_path):
    # Certifica-se de que 'commands' não seja None
    if not commands:
        print("Erro: Arquivo YAML mal formatado ou vazio.")
        return

    # Itera sobre os comandos no arquivo YAML
    for command in commands:
        # Certifica-se de que 'command' não seja None
        if not command:
            print("Erro: Comando YAML mal formatado.")
            continue

        name = command.get("name")
        run_command = command.get("run")

        # Certifica-se de que 'name' e 'run_command' não sejam None
        if name is None or run_command is None:
            print("Erro: Comando YAML mal formatado.")
            continue

        # Exibe o nome do comando
        print(f"echo \"{name}\"")

        # Executa o comando
        subprocess.run(["bash", "-c", run_command], cwd=repo_path)

# Itera sobre os projetos e repositórios no arquivo de configuração
# ...

for project in config_data["projects"]:
    project_name = project["name"]
    project_path = project["path"]

    for repository in project["repositories"]:
        repository_name = repository["path"]
        pipeline_file_name = f"pipeline-{project_name}-{repository_name}.yml"
        pipeline_file_path = os.path.join(config_output_path, pipeline_file_name)

        # Lê o arquivo YAML específico do projeto/repositorio
        with open(pipeline_file_path, "r") as file:
            pipeline_commands = yaml.safe_load(file)

        while True:
            # Verifica se há mudanças no repositório
            if has_changes(os.path.join(project_base_path, project_path, repository_name)):
                print(f"Mudança detectada no projeto {project_name}, repositório {repository_name}!")
                print(f"Executando git pull...")

                # Executa git pull para obter as mudanças mais recentes
                subprocess.run(["git", "-C", os.path.join(project_base_path, project_path, repository_name), "pull"])

                print("Git pull concluído.")

                # Executa o script YAML após o git pull
                run_pipeline_commands(pipeline_commands, os.path.join(project_base_path, project_path, repository_name))

            # Espera por um tempo antes de verificar novamente
            time.sleep(10)  # Verifica a cada 10 segundos (ajuste conforme necessário)
