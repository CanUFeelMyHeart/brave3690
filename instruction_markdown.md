# Подсказки по командной строке

Команда для запуска Git-а:
```sh
git init
```

Команда смены директории:
```sh
cd c:\folder_name
```

Команда для отображения текущий директории в MacOs, Linux:
```sh
pwd
```

Листинг текущей директории для Windows:
```sh
dir
```

Linus, MacOs:
```sh
ls
```

Удаление файла в Windows:
```sh
del <filename>
```

В Linux, MacOs:
```sh
rm <filename>
```

Список изменения:
```sh
git log
```

Список изменения в одну строку:
```sh
git log --oneline
```

Вернутся к изменению:
```sh
git checkout
```

Вернутся последним изменениям:
```sh
git checkout master
```

Показ изменения:
```sh
git diff
```

Создание ветки:
```sh
git branch (имя_ветки)
```

Проверка на какой ветке:
```sh
git branch
```

Для перемещения между ветками:
```sh
git checkout (имя_ветки)
```

Создание нового репозиторий в командной строке:
```sh
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YDaniyar/test.git
git push -u origin main
```

Загрузка существующий репозиторий из командной строки:
```sh
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YDaniyar/test.git
git push -u origin main
```

Загрузка существующий репозиторий из командной строки:
```sh
git remote add origin https://github.com/YDaniyar/test.git
git branch -M main
git push -u origin main
```

Команда для копирования репозиторий:
```sh
git clone (ссылка репозиторий)
```
Отправить свою версию репозитория во внешний репозиторий:
```sh
git push
```

**git fetch** синхронизирует локальное представление удалённых репозиториев с тем, что является актуальным на текущий момент времени
```sh
git fetch
```

Эта команда позволяет скачать все из текущего репозитория и автоматически сделать merge с нашей версией^
```sh
git pull
```