```a
import os
import subprocess
import shutil

def clone_or_update_repo(repo_url, local_dir):
    """
    Клонирует репозиторий, если он не существует, или обновляет его, если он уже есть.
    :param repo_url: URL репозитория GitHub.
    :param local_dir: Локальная директория для клонирования репозитория.
    """
    if os.path.exists(local_dir):
        print("Репозиторий уже существует. Обновляю...")
        subprocess.run(["git", "-C", local_dir, "pull"], check=True)
    else:
        print("Репозиторий не найден. Клонирую...")
        subprocess.run(["git", "clone", repo_url, local_dir], check=True)

def run_script(script_path):
    """
    Запускает указанный Python-скрипт.
    :param script_path: Путь к Python-скрипту.
    """
    if os.path.exists(script_path):
        print(f"Запускаю скрипт: {script_path}")
        subprocess.run(["python", script_path], check=True)
    else:
        print(f"Скрипт {script_path} не найден.")

if __name__ == "__main__":
    # URL репозитория GitHub
    repo_url = "https://github.com/prem1umservice/Jarvis.git"  # Замените на URL вашего репозитория

    # Локальная директория для репозитория
    local_dir = "repository"

    # Путь к скрипту, который нужно запустить
    script_name = "main.py"  # Замените на имя вашего скрипта
    script_path = os.path.join(local_dir, script_name)

    # Клонируем или обновляем репозиторий
    clone_or_update_repo(repo_url, local_dir)

    # Запускаем скрипт
    run_script(script_path)```
