# GeekBrains
## Работа с удаленными репозиториями

* Клонировать удаленный репозиторий
```sh
git clone https://github.com/AnatoliyS2019/gb.git
```
* Переименовать ветку master в main. Предварительно зайдя в ветку master
```sh
git branch -M main
```
* Связать локальный репозиторий с удаленным
```sh
git remote add origin https://github.com/AnatoliyS2019/gb.git
```
* Показать имя удаленного репозитория
```sh
git remote
git remote show
```
* Показать информацию по удаленному репозиторию origin
```sh
git remote show origin
```
* Вывести удаленные репозитории
```sh
git remote -v
```
* Забрать с удаленного репозитория и слить
```sh
git pull --rebase
```
* Команда используется после слияния изменений на удаленном и локальном репозиториях. После необходимо применить команду git push для размещения изменений на удаленном репозитории
```sh
git rebase --continue
```
* Удалить ветку
```sh
git branch -d brach_name
```
* Удалить ветку на удаленном репозитории
```sh
git push origin --delete barch_name
```
* Передать изменения ветки main в удаленный репозиторий
```sh
git push -u origin main
```
* Передать ветку branch_name и создать её в удаленном репозитории
```sh
git push --set-upstream origin branch_name
```