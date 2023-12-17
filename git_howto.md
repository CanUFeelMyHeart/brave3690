# Инструкции и подсказки по Git

* Задать логин:
```sh
git config --global user.name "Psey"
```

* Задать email:
```sh
git config --global user.email Vysangao@mail.ru
```

* Создание репозитория:
```sh
git init
```

* Изменение директории репозитория:
```sh
cd C:\Users\Роман\Desktop\Учеба\Git education
```

* Добавить файл к отслеживанию:
```sh
git add file_name.txt
```

* Сохранить текущее состояние файлов и оставить текстовое напоминание:
```sh
git commit -m "message"
```

* Показать разницу между текущим состоянием файла и его последней сохраненной версией:
```sh
git diff
```

* Показать журнал всех изменений в файле:
```sh
git log
```

* Показать журнал всех изменений в укороченной форме:
```sh
git log --oneline"
```

* Загрузить сохранение по коммиту:
```sh
git checkout 4_first_numbers
```

* Загрузить актуальное состояние файла по коммиту:
```sh
git checkout master
```

* Показать историю всех изменений в виде графа/дерева:
```sh
git log --oneline --graph
```

* Импорт репозитория из GitHub:
```Sh
git clone http://
```

* Экспорт репозитория в GitHub:
```sh
git remote add origin http://
git brunch -M main
git push -u origin main
```

* Загрузить изменения в GitHub:
```sh
git push
```

* Выгрузить изменения с GitHub:
```sh
git pull
```

* Очистка выдачи терминала:
```sh
clear
```

* Создание и переключение на новую ветку:
```sh
git checkout -b [branch_name]
```

* Слияние всех коммитов ветки:
```sh
git rebase
```

* Перемещение на 1 коммит назад:
```sh
git checkout HEAD^
```

* Перемещение на несколько коммитов назад:
```sh
git checkout HEAD~<num>
```
* Принудительное прикрепление ветки к коммиту:
```sh
git branch -f main HEAD~3
```

* Отмена изменений, перенос ветки назад как-будто некоторых коммитов не было:
```sh
git reset Head~1
```

* Копирование перечисленных коммитов на место, где сейчас находишься (HEAD):
```sh
git cherry-pick <commit1><commit2>...
```

* Внесение изменений в коммит:
```sh
git commit --amend
```