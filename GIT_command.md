# Instruction for GIT

## GIT Commands

*below are the most common GIT commands*

### Introduction to Version Control

#### by KatZ, the new person to IT World

##### [GeekBrains](https://gb.ru/"link to official Web-page")


**Command #1** -

To create the repository in the folder at the local machine - use
```sh
git init
```

**Command #2** - 

To check the current status - use
```sh
git status
```
*this will show if any file was modified*

**Command #3** - 

To add the modified file to the index - use
```sh
git add <file_name>
```

**Command #4** - 

To save the changes in the file - use
```sh
git commit -m "message text"
```

**Command #5** - 

To see commits made in the file - use
```sh
git log
```

**Command #6** - 

To display all commits made in file as one line - use
```sh
git log --oneline
```

**Command #6** - 

To switch between different branches (to work on a different branch) - use
```sh
git checkout <name_of_branch>
```

**Command #7** - 

To see what is different between commits - use
```sh
git diff
```
**Command #8** - 

To display all branches - use
```sh
git branch
```

**Command #9** - 

To create the new branch - use 
```sh
git branch <branch_name>
```
*__NB__ Branch name shall have no spaces!*

**Command #10** - 

To merge branches - use 
```sh
git merge <branch_name>
```
*__NB__ First checkout to the branch you need - then indicate the name of the branch you want to merge with the checked out branch*

**Command #11** - 

To delete the branch -  use
```sh
git branch -d <branch_name>
```