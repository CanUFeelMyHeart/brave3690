

Команда смены директории 
```sh
cd c:\folder_name
```

Листинг текущей директории
Windows
```sh
dir
```
Команда для удалений файла
```sh
del <filename>
```
## Команды для git

1. Проверяем установлен ли git
```sh
git --version
```
2. Запускаем процесс запоминания
```sh
git init
```
3. Сохраняем новый файл
```sh
git add "name"
```
4. Запоминаем новый файл иначинаем его отслеживать
```sh
git commit -m"filename"
```
5. Показывает все изменения (commits) в терминале
```sh
git log
```
6. Показывает все изменения (commits) в укороченном виде
```sh
git log --oneline
```
7. Вернуться к актуальной версии файла
```sh
git checkout master
```
8. Показывает текущие изменения
```sh
git diff
```
9. Используеться для слияния веток
```sh
git merge name
```
10. Для перехода с ветки на ветку
```sh
git branch name
```
11. Для очистки терминала используется
```sh
clear
```
12. увидеть ветки комитов
```sh
git log --graph
```


## Первые шаги

1. Делаем fork репозитория, в которой потом хотим сделать pull request. Ищем кнопку Fork на странице репозитория <https://git@github.com:gulden-geekbrains/version_control.git>
2. Выполняем команду клонирования из своей fork-копии
```sh
git clone git@github.com:*YOURE_GITHUB*/version_control.git
```
3. Создаем новую ветку и вносим необходимые изменения в файл
```sh
git checkout -b updatereadme
vim README.md
git add README.md
git commit -m "Добавили инструкцию как создать pull request"
```
4. Делаем push  
```sh
git push --set-upstream origin updatereadme
```
5. Переходим на свою страницу репозитория. Выбираем ветку **updatereadme** и жмем кнопку **Compare & pull request**

## Заметки

Что бы сделать push от другого пользователя необходимо выполнить команду
```sh
GIT_SSH_COMMAND='ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes' git push git@github.com:gulden-geekbrains/version_control.git
```

вместо *user-private-key* подставьте свой ключ

Можно прописать настройки для подсоединения по ssh
```sh
git config remote.origin.url git@github.com:gitusername/reponame
git config core.sshCommand "ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes"
```
# Как подружить git с github под Windows 10

Вот видео инструкция [ссылка](https://youtu.be/E8cIjbJMEpE)



