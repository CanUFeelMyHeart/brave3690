## Работа с удаленными репозиториями. (Некоторые команды git)

### Переименовать ветку master в main. Предварительно зайдя в ветку master
```sh
git branch -M main
```
### Клонировать удаленный репозиторий
```sh
git clone https://github.com/FIGAro2KK/brave3690.git
```
### Связать локальный репозиторий с удаленным
```sh
git remote add origin https://github.com/FIGAro2KK/brave3690.git
```
### Показать имя удаленного репозитория
```sh
git remote
```
### Показать информацию по удаленному репозиторию origin
```sh
git remote show origin
```
### Вывести удаленные репозитории
```sh
git remote -v
```
### Забрать с удаленного репозитория и слить
```sh
git pull --rebase
```
### Cлияние изменений на удаленном и локальном репозиториях. 
```sh
git rebase --continue
```
### Удалить ветку
```sh
git branch -d brach_name
```
### Удалить ветку на удаленном репозитории
```sh
git push origin --delete barch_name
```
### Передать изменения ветки main в удаленный репозиторий
```sh
git push -u origin main
```
### Передать ветку branch_name и создать её в удаленном репозитории
```sh
git push --set-upstream origin branch_name
```

_Примечание:_

При возникновении ошибки 
SSL certificate problem: unable to get local issuer certificate
```sh
git config --global http.sslBackend schannel
```