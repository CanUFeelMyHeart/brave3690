# Подсказки по командной строке

### Команда смены директории
```sh
cd c:/filder_name
```

### Просмотр содержимого текущей папки
Windows:
```sh
dir
```
Linux, MacOs:
```sh
ls
```

### Команда отображения текущей директории(MacOs, Linux)
```sh
pwd
```

### Команда инициализации Git в текущей директории
```sh
git init
```

### Добавление изменений в отслеживание
```sh
git add <file_name>
```

### Фиксация изменений 
```sh
git commit -m "text"
```
 
### Удаление файла
Windows:
```sh
del <file_name>
```
Linux, MacOs:
```sh
rm <file_name>
```

### Переход на другую ветку или коммит
```sh
git checkout <name>
```

### Просмотр списка коммитов
```sh
git log
```

### Просмотр списка коммитов без подробностей(в одну строку)

```sh
git log --oneline
```

### Отображение всех веток

```sh
git branch
```

### Создание новой ветки и переход на нее

```sh
git checkout -b <new_branch_name>
```

### Удаление ветки
```sh
git branch -d <branch_name>
```

### Графическое отображение веток
```sh
git log --oneline --graph
```
