# Подсказка по GIT

Создание репозитория:
```sh
git init
```
Добавление файла к индексации:
```sh
git add
```
Проверка статуса файла
```sh
git status
```
Сохранение изменений файла
```sh
git commit -m"Message_text"
```
Отображение всех внесенных сохранений:
```sh
git log
```
Отображение всех внесенных сохранений кратко
```sh
git log --oneline
```
Перемешение между ветками или логами:
```sh
git checkout <имя_ветки или номер лога>
```
Вазвращение к основной ветке:
```sh
git checkout master
```
Просмотр внесенных изменений между сохранениями:
```sh
git diff
```
Добавить ветку:
```sh
branch <name_branch>
```
Удалить ветку:
```sh
gif branch -d <name_branch>
```
Слить ветку:
```sh
merge <name_branch>
```
Отменить слияние веток:
```sh
merge --abort
```
Добавить все изменения:
```sh
add --all
```
# Работа с удаленным репозиторием

Скопировать чужой репозиторий
```sh
Git clone 
```
Смена директории
```sh
Cd 
```
Выйти из директории
```sh
Cd .. 
```
Переименовать основную ветку с мастер на мэйн
```sh
git branch -M main 
```
Связать локальный репозиторий с удаленным
```sh
git remote add origin https://github.com/MilaTakushevich/my_first_repo.git 
```
Просмотреть
```sh
git remote show 
```
```sh
git remote show origin
```
Выталкнуть (отправить) на сервер (на удаленный репозиторий)
```sh
git push -u origin main 
```
Передать новую ветку в удаленный репозиторий
```sh
git push --set-upstream origin newbranch 
```
Удалить ветку в удаленном репозитории 
```sh
git push origin -–delete newbrach 
```
При выкачке изменений с сервера позволит наложить локальные изменения
```sh
git pull –rebase 
```
Продолжить перебазирование:
```sh
git rebase --continue
```
Откатить изменения — вернуться в состояние до использования команды rebase.
```sh
git rebase --abort
```