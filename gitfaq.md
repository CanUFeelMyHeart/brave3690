# Подсказка по GIT

*git - система контроля и управления версиями файлов*

## Инициализация нового репозитория Git

### <span style = "color:blue"> Установка и конфигурирование

###### <span style = "color: black"> **Инициализация нового репозитория Git:**
> git init
###### <span style = "color: black"> **Клонирование и создание локальной копии удалённого репозитория:**
> git clone < url>
###### <span style = "color: black"> **Настройка глобальных параметров git:**
> git config --global <имя_параметра> <значение>
###### <span style = "color: black"> **Настройка локальных параметров Git для конкретного репозитория:**
> git config --local <имя_параметра> <значение>

#### *---Расширенные---*

###### <span style = "color: black"> **Показать сводку настроек конфигурации Git**
> git config --list
###### <span style = "color: black"> **Установить пользовательский текстовый редактор для сообщений Git**
> git config --global core.editor " <команда_редактора>"
###### <span style = "color: black"> **Создать псевдоним команды Git**
> git config --global alias.<псевдоним> <команда>
###### <span style = "color: black"> **Включить автоматическое окрашивание вывода Git'а**
> git config --global color.ui auto
###### <span style = "color: black"> **Кэшировать учётные данные Git на определённое время**
> git config --global credential.helper 'cache --timeout=<секунды>'
###### <span style = "color: black"> **Настроить git на обнаружение определённых типов ошибок пробельных символов**
> git config --global core.whitespace <опции>
###### <span style = "color: black"> **Автоматически обрезать ветви удалённого отслеживания при получении обновлений**
> git config --global fetch.prune true
###### <span style = "color: black"> **Установить пользовательский инструмент diff для Git**
> git config --global diff.tool <инструмент>
###### <span style = "color: black"> **Установить пользовательский инструмент слияния для Git**
> git config --global merge.tool <инструмент>
###### <span style = "color: black"> **Сравнение изменения с помощью пользовательского инструмента diff**
> git difftool
###### <span style = "color: black"> **Разрешение конфликтов слияния с помощью пользовательского инструмента слияния**
> git mergetool

### <span style = "color:blue"> Файловые операции

###### <span style = "color: black"> **Показать состояние рабочего дерева**
> git status
###### <span style = "color: black"> **Добавить файлы в область хранения**
> git add <файл(ы)>
###### <span style = "color: black"> **Удалить файлы из рабочего дерева и области хранения**
> git rm <файл(ы)>
###### <span style = "color: black"> **Переместить или переименовать файл**
> git mv <старый_файл> <новый_файл>
###### <span style = "color: black"> **Коммит изменений с сообщением**
> git commit -m "сообщение коммита"
###### <span style = "color: black"> **Показать различия между рабочим деревом и последним коммитом**
> git diff

#### *---Расширенные---*

###### <span style = "color: black"> **Предположить, что отслеживаемый файл не изменился**
> git update-index --assume-unchanged <файл>
###### <span style = "color: black"> **Восстановить нормальное поведение отслеживания изменений**
> git update-index --no-assume-unchanged <файл>
###### <span style = "color: black"> **Показать различия между двумя коммитами**
> git diff <коммит_id1>..<коммит_id2>
###### <span style = "color: black"> **Удалить файл, но сохранить в рабочем каталоге**
> git rm --cached <имя_файла>

### <span style = "color:blue"> История коммитов

###### <span style = "color: black"> **Показать историю коммитов**
> git log
###### <span style = "color: black"> **Показать сжатую историю коммитов**
> git log --oneline
###### <span style = "color: black"> **Показать историю коммитов с ветвлением**
> git log --graph
###### <span style = "color: black"> **Фильтровать историю коммитов по автору**
> git log --author=<имя_автора>
###### <span style = "color: black"> **Показать историю коммитов с определённой даты**
> git log --since=<дата>
###### <span style = "color: black"> **Показать историю коммитов до определённой даты**
> git log --until=<дата>

### <span style = "color:blue"> Тэги

###### <span style = "color: black"> **Список всех тегов**
> git tag
###### <span style = "color: black"> **Создать новый тег для определённого коммита**
> git tag <имя_тега> <коммит_id>
###### <span style = "color: black"> **Создать аннотированный тег с сообщением**
> git tag -a <имя_тега> -m "сообщение тега"
###### <span style = "color: black"> **Удалить определённый тег**
> git tag -d <имя_тега>
###### <span style = "color: black"> **Удалить определённый удалённый тег**
> git push <имя_удалённого_репозитория> --delete <имя_тега>
###### <span style = "color: black"> **Показать информацию о конкретном теге**
> git show <имя_тега>

### <span style = "color:blue"> Работа с удалёнными репозиториями

###### <span style = "color: black"> **Выгрузить из репозитория**
> git pull 

###### <span style = "color: black"> **Загрузить в репозиторий**
> git push


    