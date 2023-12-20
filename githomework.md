# Подсказки по GIT
Создание репозитория
```sh
git init
```
Команда смены директории
```sh
cd c:\folder.name
Добавить к индексации
```sh
git add
```
Зафиксировать изменения
```sh
git commit -m "Messege"
```
посмотреть log в полном виде
```sh
git log
```
Посмотреть Log в сокращенном виде
```sh
git log --oneline

Перемещение по веткам
```sh
git checkout
```

```
Команда отображения директории
 MacOs, Linux
```sh
pwd
```
Листинг текущей директории
Windows:
```sh
dir
```
MacOs, Linux:
```sh
ls
Удаление файлаWindows:`
``sh
del <filename>
```
MacOs, Linux
```sh
rm <filename>
```
Отобразить все ветки
```sh
git branch
```
Создание новой ветки
 ```sh
git branch <имя ветки>
```
Список изменений со всеми ветками
```sh
git log --oneline --graph
```
Копирование удаленного репозитория
```sh
git clone <filename>
```
Переименовать главную ветку
```sh
git branch -M main
```
Перенести изменения в удаленный репозиторий из локального
```sh
git push
```
Перенести изменения из удаленного репозитория в локальный
```sh
git pull
```
Добавить новую ветку с локального репозитория на удаленный
```sh
git push --set-upstream origin название  ветки
```
Удалить при переносе данных на удаленный репозиторий ненужную ветку
```sh
git push origin --delete название ветки
```
