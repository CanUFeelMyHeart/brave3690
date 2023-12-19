Alekseev V Инструкция по работе с GIT

## Создание репозитория
```sh
git init
```
создает новый репозиторий

## Добавление
```sh
git add
```
добавляет содержимое рабочего каталога для последующего коммита.

## Команда git commit
```sh
git commit -m "message text"
```
Команда ***git commit -m "Текст"*** слхраняет данные, добавленные  с помощью *git add*, и сохраняет их в базе данных. 

## Команда git log --oneline
```sh
git log --oneline
```
показывает коммиты в укороченном формате

## Отображение веток
```sh
git branch
```
отображает все ветки

## Создание новой ветки
```sh
git branch <имя_ветки>
```
создает новую ветку

## Слияние веток с основной
```sh
git merge <имя_ветки>
```
выполняет слияние в единую ветку

 ## Работа с удаленными репозиториями

```sh
git clone <адрес удаленного репозитория>
```

копия удаленного репозитория в локальное хранилище

```sh
git pull
```
получить все изменения с удаленного репозитория

```sh
git push
```
отправить изменения в текущей ветке в удаленный репозиторий

# Пример создания pull request


1. Делаем fork репозитория, в которой потом хотим сделать pull request. Ищем кнопку Fork на странице репозитория <https://git@github.com:********************.git>
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

Чтобы сделать push от другого пользователя необходимо выполнить команду
```sh
GIT_SSH_COMMAND='ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes' git push git@github.com:******************.git
```

вместо *user-private-key* подставьте свой ключ

Можно прописать настройки для подсоединения по ssh
```sh
git config remote.origin.url git@github.com:gitusername/reponame
git config core.sshCommand "ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes"