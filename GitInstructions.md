# Инструкция по работе с Git

## Комманды:
### Создание репозитория:

**git init** - *инициализация GIT - репозитория*

### Сохранение файла в репозитории:

 **git add fileName** - *конкретный файл*

 **git add .** - *добавить все файлы из папки*

### Вывести изменения:

 **git diff**

### Создание коммита (сохранениия):

 **git commit -m “message”** - *создание коммита после ручного добавления* 
 **git commit -am "message"** - *добавление файлов в коммит и создание коммита сразу*

### Вывод в терминал всех коммитов:

 **git log**

### Переход к коммиту:

 **git checkout (hashcode)** - переход к конкретному коммиту по хашкоду

 **git checkout master** - переход к актуальной версии

## Синтаксис 

* \# Заголовок – выделение заголовков. Количество символов “#” задаёт уровень заголовка  (поддерживается 6 уровней)

* = или - – подчёркиванием этими символами (не менее 3 подряд) выделяют заголовки  первого (“=”) и второго (“-”) уровней.

* \**Полужирное начертание** или \__Полужирное начертание__

* \*Курсивное начертание* или _ Курсивное начертание_

* \*\*\*Полужирное курсивное начертание***

* \~~Зачёркнутый текст~~

*  \* Строка – ненумерованные списки, символ “*” в начале строки 

* 1\. , 2\. , 3\. … – нумерованные списки

> Основано на [презентации](https://docs.google.com/presentation/d/1UFrFZwXRNMBXe15m8YGtdcqiwFfmPm8Tdi9NbKVKeFU/edit#slide=id.p3) от GeekBrains

[![GeekBrainsLogo](data:image/png;base64,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)](https://gb.ru/)

## Работа с ветками

### Создание ветки:

> **git branch branch_name** - создание ветки с именем branch_name

> **git checkout -b branch_name** - создание ветки с переходом на неё же


### Переход на ветку:

> **git checkout branch_name** - переход на ветку с названием branch_name

### Вывод всех веток на экран:

> **git branch**


### Слияние веток:

> **git merge branch_name** - добавление(слияние) ветки branch_name в текущую ветку(на которой находимся)

### Графическое отображение работы с ветками:

> **git log --graph**

*Если ветка была удалена, то в логе она отображаться не будет*

### При ошибке исправления слияния или утрате данных при слиянии:

> **git reset --hard хэш_код_коммита_перед_слиянием**

### Удаление веток:

> **git branch -d** - удаление с проверкой на слияние

> **git branch -D** - удаление без проверки на слияние

## Работа с удалёнными репозиториями