# Git commands instruction

> ## **Usefull links:**

- [git youtube course](https://www.youtube.com/playlist?list=PLDyvV36pndZFHXjXuwA_NywNrVQO0aQqb)

- [git reference manual](https://git-scm.com/docs)

> ## **1. Set user configurations: git config**

![git config hierarchy](src\git_config.png)

- ### Basic operations:

*set username/email for local project:*

```sh
git config --local user.name <put_your_name> <put_your_email>
```

*set global username/email for all projects of current user:*

```sh
git config --global user.name <put_your_name>/<put_your_email> 
```

*set system username/email for all users:*

```sh
git config --system user.name <put_your_name>/<put_your_email>
```


*remove local parametres:*

```sh
git config --unset <user.name> or <user.email>
```

*remove section user:*

```sh
git config --remove-section user
```
- ### Show info:

*show all git configurations:*

```sh
git config --list
```

*show certaion git configurations, for example:*

```sh
git config user.name
```

> ## **2. Initialize git repository: git init**

```sh
git init
```

don't forget to create .gitingore + do initial commit!

> ## **3. Add changes from Working Directory to Index: git add**

![git workspaces](src\git_workspaces.png)

- ### Basic operations:

*add changed file to Index:*

```sh
git add  <file_name>
```

*add all changes from current Working Directory:*

```sh
git add .
```

*remove changes from Index:*

```sh
git reset HEAD <file_name>
```

or

```sh
git restore --staged <file_name>
```

- ### Usefull flags:

*add all changes from project source:*

```sh
git add -A
```

*add just choosen changes from file:*

```sh
git add -p <file_name>
```

- ### Show Working Directory and Index status:

```sh
git status
```

> ## **4. Commit changes from Index to Repository: git commit**

- ### Basic operations:

*commit all changes form Index to Repository:*

```sh
git commit -m <commit_message>
```

*checkout to branch:*

```sh
git checkout <branch_name>/<commit_tag>
```

- ### Usefull flags:

*commit all changes from Workong Directory to Repository (only if files are already been in Index!):*

```sh
git commit -a -m <commit_message>
```

*commit changes from Workong Directory to Repository (only if files are already been in Index!):*

```sh
 git commit -m <commit_message> <file(s)_path>
 ```

- ### Show commits information:

*show commit information:*

```sh
git show <commit_tag> --pretty=fuller
```

*commits history with all information:*

```sh
git log
```

*short version of commits history:*

```sh
git log --oneline 
```

*show branches graph:*

```sh
git log --graph
```

> ## **7. Branches**

- ### Basic operations:

*create new branch:*

```sh
git branch <branch_name>
```
*create and checkout to new branch:*

```sh
git checkout -b <branch_name>

```
*delete branch:*

```sh
git branch -d <branch_name>
```

- ### Merge branches:

![before_merge](src\before_merge.png)

*1. checkout to branch (e.g. master):*

```sh
git checkout <destination_branch>
```

*2. merge branches:* 

```sh
git merge <branch_to_merge>
```

![after_merge](src\after_merge.png)

*3. merged branch can be deleted after merge.*

> ## **8. Remote repositories**

- ### Link local and remote repos:

*link your local repo with remote repo:*

```sh
git remote add origin <repo_url.git>
```

*rename local branch to main (github recommended):*

```sh
git branch -M main
```

*send main branch to remote repo:*

```sh
git push -u origin main
```

- ### Basic operations:

*clone remote repo:*

```sh
git clone <repo_url>
```

*add local changes to remote repo:*

```sh
git push
```

*get remote changes to local repo:*

```sh
git pull
```

*push local branch to remote repo:*

```sh
git checkout <local_branch>
git push --set-upstream origin <local_branch>
```
- ### Conflicts:

*pull remote changes with merging to your local repo:*

```sh
git pull --rebase
```

*after conflict is solve, finish rebase:*

```sh
git rebase --continue
```

- ### Show info:

*show fetch and push:*

```sh
git remote -v
```

or

```sh
git remote show origin
```
