# Подсказки по Git

![Git logo](Git_image.jpg "Логотип Git")

* [ссылка на Git](https://git-scm.com/ "Официальная страница")
* [ссылка на интерактивное обучение Git](https://learngitbranching.js.org "Обучение Git")

> для начала использования Git необходимо его скачать с официального источника и установить на свой ПК
### Создание репозитория
```sh
git init
```
### Добавление содержимого файла к индексированию
```sh
git add
```
### Создание коммита
```sh
git commit -m "Текст"
```
### Просмотр коммитов
```sh
git log
```
### Краткий просмотр коммитов
```sh
git log --oneline
```
### Просмотр дерева 
```sh
git log --graph 
```
### Переключение версий в репозитории, переключение веток
```sh
git checkout number_of_commit
git checkout branch_name
```
### Сравнение разных версий коммитов
```sh
git diff
```
### Восстановление прежнего состояния в рабочей директории
```sh
git restore
```
### Просмотр статуса в рабочей директории
```sh
git status
```
### Добавить своё имя
```sh
git config --global user.name "John Doe"
```
### Добавить свой емайл
```sh
git config --global user.email johndoe@example.com
```
### Просмотр веток 
```sh
git branch 
```
### Добавить новую ветку 
```sh
git branch branch_new_name
```
### удалить ветку 
```sh
git branch --delete branch_name 
git branch -D branch_name
```
### Переименовать ветку 
```sh
git branch -M new_branch_name 
```
## Клонируем репозиторий с Github
```sh
git clone https://github.com/gulden-geekbrains/version_control.git
```
## Соединяемся с репозиторием Github
```sh
git remote add origin https://github.com/Kondratovo/my_first_repo.git
```
## Отправляем локальный репозиторий в Github 
* необходима авторизация
```sh
git push -u origin main
git push
```
## Вытятиваем в локальный репозиторий из Github 
* необходима авторизация
```sh
git pull
```
## Выталкиваем/создаем новую ветку в Github
```sh
git push --set-upstream origin NewBranch
```
## Удаляем ветку в Github
```sh
git push --delete origin NewBranch
```
## Выкачать с Github и произвести слияние с локальным репозиторием
```sh
git pull --rebase
```