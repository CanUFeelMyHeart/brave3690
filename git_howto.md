# Подсказки по командной строке

Команда смены директории
```sh
cd c:\folder_name
```

Команда отображения текущей директории
```sh
pwd
```

Листик текущей директории
Windows:
```sh
dir
```
Linux, Mac0s:
```sh
ls
```

Удаление файла в Windows:
```sh
del <filename>
```
в Linux, Mac0s:
```sh
rm <filename>
```

Иницилизация Git
```sh
git init
```

Текущее состояние git
```sh
git status
```

Добавляем содержимое рабочего каталога
```sh
git add
```

Удаление содержимого рабочего каталога
```sh
git restore
```

Добавляем коментарий к сохранению
```sh
git commit -m "name"
```

Журнал изменений
```sh
git log
```

Сокращеный журнал изменений
```sh
git log --online
```

Переключение между версиями
```sh
git checkout
```

Возвращение в исходное положение терминала
```sh
q
```

Разница между версиями
```sh
git diff
```

# Команда отображения текущей ветки 
```sh
git branch
```
# Команда создания новой ветки
```sh
git branch <название новой ветки>
```
# Команда для слияния веток
```sh
git merge <название ветки text>
```

Отображение всех веток
```sh
git brainch
```

Перемещение по веткам
```sh
git checkout <имя ветки>
```

Создание новой ветки 
```sh
git branch <имя ветки текст>
```

# Учимся pull request

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

Вот видео инструкция https://youtu.be/E8cIjbJMEpE