# Работа с удаленным репозиторием

Скопировать чужой репозиторий:
```sh
Git clone 
```
Смена директории:
```sh
Cd 
```
Выйти из директории:
```sh
Cd .. 
```
Переименовать основную ветку с master на main:
```sh
git branch -M main 
```
Связать локальный репозиторий с удаленным:
```sh
git remote add origin https://github.com/MilaTakushevich/my_first_repo.git 
```
Просмотреть:
```sh
git remote show 
```
```sh
git remote show origin
```
Выталкнуть (отправить) на сервер (на удаленный репозиторий):
```sh
git push -u origin main 
```
Передать новую ветку в удаленный репозиторий:
```sh
git push --set-upstream origin newbranch 
```
Удалить ветку в удаленном репозитории:
```sh
git push origin -–delete newbrach 
```
При выкачке изменений с сервера позволит наложить локальные изменения:
```sh
git pull –rebase 
```
Продолжить перебазирование:
```sh
git rebase --continue
```
Откатить изменения — вернуться в состояние до использования команды rebase:
```sh
git rebase --abort
```
Git имеет огромную вариативность команд. В данном файле указаны лишь основные для работы с удаленным репозиторием.