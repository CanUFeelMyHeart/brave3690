1391499931841894891491494119491409491949194
4419418914881481484814848841818488481481481481848148481488141481848189418481948198491981518г581985915814545
Привет, Гитхаб! Здесь будет информация о первых командах из 3 семинара
> git push - отправить изменения в удаленный репозиторий 
Привет мы пробуем работу с удаленным репозиторием =)

# Это репозиторий для обучения pull request

## Первые шаги

1. Делаем fork репозитория, в которой потом хотим сделать pull request. Ищем кнопку Fork на странице репозитория https://git@github.com:gulden-geekbrains/version_control.git
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

5. Переходим на свою страницу репозитория. Выбираем ветку updatereadme и жмем кнопку Compare & pull request