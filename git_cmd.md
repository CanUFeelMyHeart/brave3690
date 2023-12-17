# Commands Git

* Сreating local repository

```sh
git init
```

* Get information from git about its current state

```sh
git status
```

* Add versioning to the file in the local repository

```sh
git add "filename"
```

* Captures the changes and reports when new versions of files appear

```sh
git commit -m "Message of the commit"
```

* Shows the difference between the current and the already committed version of the file

```sh
git diff
```

* Displays a list of all commits (saves) in chronological order (full)

```sh
git log
```

* Displays a list of all commits (saves) in chronological order (oneline)

```sh
git log --oneline
```

* Displays a list of all commits (saves) in chronological order (in one line) and graphically changes

```sh
git log --oneline --graph
```

* Navigate between saves and commits

```sh
git checkout
```

* Displays branchs

```sh
git branch
```

* Shows branchs

```sh
git branch
```

* Add new branch

```sh
git branch <branch_name>
```

* Delete branch

```sh
git branch -d <branch_name>
```

* Merge branch

```sh
git merge <branch_name>
```

* Rename original Main branch
```sh
git branch -M main  
```

* See remote repositories linked to your local clone
```sh
git remote -v
```

* reassign another Git for push
```sh
git remote set-url origin git@github.com:<Login>/<Repo>
```

* Make a local copy of a remote repository
```sh
git clone git@github.com:<Login>/<Repo>
```

* "pull/download" all changes from the remote repository
```sh
git pull
```

* Push changes to a remote repository
```sh
git push
```

* Push local branches to a remote repository
```sh
git push --set-upstream origin <branch>
```
