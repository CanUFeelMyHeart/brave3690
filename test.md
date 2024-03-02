1391499931841894891491494119491409491949194
4419418914881481484814848841818488481481481481848148481488141481848189418481948198491981518г581985915814545
Привет, Гитхаб! Здесь будет информация о первых командах из 3 семинара
> git push - отправить изменения в удаленный репозиторий 
Привет мы пробуем работу с удаленным репозиторием =)

dfgdf

Это репозиторий для обучения pull request

Первые шаги

Делаем fork репозитория, в которой потом хотим сделать pull request. Ищем кнопку Fork на странице репозитория https://git@github.com:gulden-geekbrains/version_control.git

Выполняем команду клонирования из своей fork-копии

git clone git@github.com:*YOURE_GITHUB*/version_control.git

Создаем новую ветку и вносим необходимые изменения в файл

git checkout -b updatereadme

vim README.md

git add README.md

git commit -m "Добавили инструкцию как создать pull request"

Делаем push

git push --set-upstream origin updatereadme

Переходим на свою страницу репозитория. Выбираем ветку updatereadme и жмем кнопку Compare & pull request

Заметки

Что бы сделать push от другого пользователя необходимо выполнить команду

GIT_SSH_COMMAND='ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes' git push git@github.com:gulden-geekbrains/version_control.git

вместо user-private-key подставьте свой ключ

Можно прописать настройки для подсоединения по ssh

git config remote.origin.url git@github.com:gitusername/reponame

git config core.sshCommand "ssh -i ~/.ssh/user-private-key -o IdentitiesOnly=yes"

Как подружить git с github под Windows 10

Вот видео инструкция https://youtu.be/E8cIjbJMEpE
