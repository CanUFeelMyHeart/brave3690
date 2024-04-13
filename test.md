### Команды CMD для GIT
* Смена дирректории
```sh
CD
```
* Инициализация GIT в текщей дирректории
  ```sh
  git init
  ```
  * Добавление файла в индекс GIT
  ```sh
  Git add <filename.md>
  ```
  * Создание коммита для файла
  ```sh
  git commit -m "comit_name"
  ```
  * Запрос статуса git
  ```sh
  git status
  ```
  * Лог git
  ```sh 
  git log
  ```
  ```sh
  git log --oneline
  ```
  ```sh
  git log --oneline --graph
  ```
  * Переключение между версиями
  ```sh 
  git checkout <commit ID>
  ```
  * Просмотр различий между версиями
  ```sh 
  git diff
  ```

   ### Работа с ветками
  * просмотр текущей ветки
  ```sh 
  git branch 
  ```
  * создание новой ветки
  ```sh 
  git branch "имя новой ветки"
  ```
  * переход между ветками
  ```sh 
  git checkout "имя ветки" 
  ```
  * добавление ветки 
  ```sh
  git merge "имя ветки"
  ```

  ## создание списка неотсежживаемых файлов
  создать файл .gitignor и добавить в него имя файлов



cherry-pick
reset
revert
rebase
merge


## GitHub
Clone remote repository
```sh
git clone <URL>
```

Connect to remote repository
```sh
git remote add origin <url>
```
Push to remote repository
```sh 
git push -u origin main
```

Pull from remote repository
```sh
git pull
```
11


change branch to main (GitHub only main)
```sh
git branch -M main
```




