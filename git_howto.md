# Команды по работе с GIT

## Начало работы

+ Создание пустого локального репозитория:
```sh 
git init
```

+ Внесение имени и почты в Git
```sh
git config --global user.name "Name"

git config --global user.email "Email"
```
+ Проверить имя пользователя и почту 
```sh
git config --list
```

+ Добавление изменений в файл репозитория
```sh
git add filename  (для сохранения одного файла) или git add . (для сохранения изменений во всех файлах)
```

+ Сохранение изменений в файле репозитория
```sh 
git commit -m "Message"
```

## Просмотр статуса и внесенных изменений

+ Просмотреть внесенные изменения, а так же состояние файлов можно по команде:
```sh
git status
```

+ Узнать насколько и в чем изменился файл по сравнению с сохраненной версией можно по команде 
```sh 
git diff
```

### Информация о сохранениях
1. В виде списка
```sh
git log
```
2. в виде графического дерева
```sh
git log --graph
```

3. В виде одной строки с выводом только номеров созранений и сообщений
```sh
git log --oneline
```

4. Для просмотра истории коммитов по всем веткам используется флаг --all.

```sh
git log --all --graph --oneline --decorate
```

+ Перейти к необходимому сохранению можно с использованием команды
```sh
git checkout
```

## Работа с ветками
- просмотреть название всех веток и местоположение в ветках на данный момент (обозначено зеленой звездочкой)
```sh
git branch
```
- создать новую ветку
```sh
git branch new_name
```
- перейти в нужную ветку
```sh
git checkout branch_name
```
- Слить ветки (добавить некую ветку к той, в которой находишься в настоящий момент)
```sh
git merge branch_name
```
- Удалить ненужную ветку
```sh
git branch -d branch_name
```

## Работа с удаленным репозиторием (на примере сайта [GitHub](GitHub.ru))

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
