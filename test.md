# Git commands

1. Initialization, start git
```sh
git init
```
2. Change directory
```sh
cd c:\users\...folder_name
```
3. Remove file
```sh
del <filename>
```
4. View log
```sh
git log
```
5. View 1 line log
```sh
git log --oneline
```
6. View log with graph lines
```sh
git log --graph
``` 
7. Add new commit & comment/message
```sh
git commit -m"text"
```
8. Go to selected commit
```sh
git checkout 0000
```
9. Add file to track
```sh
git add "filename.xx"
```
10. Show status
```sh
git status
```
11. Show differences between 2 commits
```sh
git diff 0000 1111
```
12. Come back to the last saved version
```sh
git restore filename.xx
```
13. Show all branches
```sh
git branch
```
14. Create new branch
```sh
git branch new_branch_name
```
15. Remove branch
```sh
git branch -d branch_name
```
16. Go to branch_name
```sh
 git checkout branch_name
```
17. Rename branch
```sh
git branch -m <new_name>
```
18. Return to the latest commit, go to master branch
```sh
 git checkout master
```
19. Copy a repository from GitHub using URL-link
```sh
git clone <link>
```
20. Send data on GitHub repository
```sh
git push
```
21. Recieve data from GitHub repository
```sh
git pull
```