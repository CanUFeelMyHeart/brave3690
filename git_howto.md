# Краткая инструкция GIT

## Основные команды Git. Работа с ветками.
**1. Отображение всех веток**
```sh
git branch
```
**2. Переключение между ветками**
```sh
git checkout <branch_name>
```
**3. Создание новой ветки**
```sh
git branch <branch_name>
```
**4. Удаление  ветки с именем <_branch_to_delete_>**
```sh
git branch -d <branch_to_delete>
```
**5. Список коммитов в виде сжатого графа/дерева**
```sh
git log --oneline --graph
```
**6. Cлияние ветки <branch_name> с текущей веткой**  
  ВАЖНО: вызывается из той ветки, куда хотите добавить изменения (master, например).
```sh
git merge <branch_name>
```
## Создание своего нового репозитория на GitHub

1. Задаем папку для работы 
```sh
echo "# test_l3_gb" >>README.md
```
2. Проверяем созданное 
```sh
dir
```
3. Начинаем контроль версий Git в папке 
```sh
git init
```
4. Определяем файл для отслеживания 
```sh
git add .\README.md 
```
5. Комментируем и записываем изменения 
```sh
git commit -m "Создание репозитория"
```
6. Переименовываем основную ветку по правилам GitHub 
```sh
git branch -M main
```
7. Связываем локальный репозиторий с удаленным репозиторием на ГитХабе 
```sh
git remote add origin <http-ссылка из GitHub>
```
8. Узнаем, задан ли удаленный (origin) репозиторий 
```sh
git remote show
```
9. Редактируем нужные файлы на локальном ПК, добавляем и коммитим (см. п.п.4,5)
10. Передаем готовые изменения с локального на удаленный репозиторий 
```sh
git push -u origin main
```

## Базовое обучение pull request

1. Делаем fork понравившегося публичного репозитория, в которой потом хотим сделать сои предложения pull request. Авторизовавшись в GitHub, ищем кнопку Fork на странице репозитория <https://git@github.com:gulden-geekbrains/version_control.git>
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
