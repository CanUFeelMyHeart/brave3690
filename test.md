

>   **git clone url**-адрес репозитория> – клонирование внешнего репозитория на  локальный ПК

>	**git pull** – получение изменений и слияние с локальной версией    
***git pull is a combination command, equal to git fetch + git merge***  

>	**git push** – отправляет локальную версию репозитория на внешний


>## add some information from lection by ILNAR SHAFIGULIN ##
>## **Инструкции как выгрузить локальный репо** в удаленный в   аккаунт на [GitHub.com](http://github.com/) 

>1. Заходим в наш аккаунт на [github.com](http://github.com) и выбираем создать репозиторий даем любое название, остальные параметры оставляем по умолчанию и нажимаем создать.
>2. После создания в пустом новом репозитории на ГитХабе появляются подсказки, что мы можем делать с новым репозиторием. Для того, чтобы привязать существующий локальный репозиторий с удаленным репозиторием надо последовательно выполнить их в терминале Visual Studio Code:  
    1. **git remote add origin https://github.com/alekscode33/Test.git** 
    // локально работающий существующий репозиторий мы добавили в интернет на ГитХаб  
    2. **git branch -M main**
    // говорим Гиту что основная ветка будет ветка main  
    3. **git push -u origin main**   
    // и пушим - передаем изменения в ветку main
    // При первичном `git push -u origin main` нужно авторизоваться и подружить **github repository** and **local repository** 
    warning: could not find UI helper 'GitHub.UI' 
    Select an authentication method for ' https://github.com/':
    1. Web browser (default)
    2. Device code
    3. Personal access token
    option (enter for default): 1
    info: please complete authentication in your browser...

>3. После этого все изменения будут переданы на Гит Хаб и если открыть на ГитХабе изменения будут отображаться

## Далее изменения делаются как обычно