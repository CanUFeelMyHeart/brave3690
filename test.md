# git-remote commands
### Manage the set of repositories ("remotes") whose branches you track.
git remote
  ``` [-v | --verbose]```
Be a little more verbose and show remote url after name.<br>
- ```add```  [-t <branch>] [-m <master>] [-f] [--[no-]tags] [--mirror=(fetch|push)] \<name> \<URL><br>
Add a remote named <name> for the repository at \<URL>.<br>
- ```rename``` Rename the remote named \<old> to \<new>. All remote-tracking branches and configuration settings for the remote are updated.<br>
- ```remove``` ```rm```Remove the remote named <name>. All remote-tracking branches and configuration settings for the remote are removed.<br>
- ```set-head```Sets or deletes the default branch (i.e. the target of the symbolic-ref refs/remotes/\<name>/HEAD) for the named remote. Having a default branch for a remote is not required, but allows the name of the remote to be specified in lieu of a specific branch.
- ```set-branches```Changes the list of branches tracked by the named remote. This can be used to track a subset of the available remote branches after the initial setup for a remote.<br>
- ```get-url```Retrieves the URLs for a remote. Configurations for insteadOf and pushInsteadOf are expanded here. By default, only the first URL is listed.<br>
- ```set-url```Changes URLs for the remote. Sets first URL for remote \<name> that matches regex \<oldurl> (first URL if no \<oldurl> is given) to \<newurl>. If \<oldurl> doesn’t match any URL, an error occurs and nothing is changed.<br>
- ```show```Gives some information about the remote \<name>.<br>
- ```prune```Deletes stale references associated with \<name>. By default, stale remote-tracking branches under \<name> are deleted, but depending on global configuration and the configuration of the remote we might even prune local tags that haven’t been pushed there. Equivalent to git fetch --prune \<name>, except that no new references will be fetched.<br>
-```update```Fetch updates for remotes or remote groups in the repository as defined by remotes.\<group><br>






#  GIT COOMMANDS | _using markdown syntaxis_
## <GIT>
usage **git:**
 1. [-v | --version] --<tt>Prints the Git suite version that the git program came from.</tt>
 2. [-h | --help] --<tt>Prints the synopsis and a list of the most commonly used commands.</tt>
 3. [-C  \<path>] --<tt>Run as if git was started in \<path> instead of the current working directory</tt>
    1. [-c <name>=<value>]

        2. [--exec-path[=\<path>]] 
        
        3. [--html-path]
    4. [--man-path]

        5. [--info-path]
4. [-p | --paginate | -P | --no-pager] --<tt>Pipe all output into less</tt>
    * [--no-replace-objects] 
        - [--bare]
            - [--git-dir=<path>]
            - [--work-tree=<path>]
        - [--namespace=<name>]
        
        
    * [--config-env=<name>=<envvar>] \<command>  [\<args>]

## ``` These are common Git commands used in various situations:```

>_start a working area (see also: git help tutorial)_


|`git` **command**| _discription_|
|-----------------|----------------|
|clone            | clone a repository into a new directory|
|init             | create an empty Git repository or reinitialize an existing one|
<br>


>_work on the current change (see also: git help everyday)_

|`git` **command**|_discription_|
|-----------------|----------------|
|add              | Add file contents to the index                        |
|mv               | Move or rename a file, a directory, or a symlink      |
|restore          | Restore working tree files                            |
|rm               | Remove files from the working tree and from the index |

<br>

>_examine the history and state (see also: git help revisions)_

|`git` **command**| _discription_|
|-----------------|--------------|
|bisect           | Use binary search to find the commit that introduced a bug |
|diff             | Show changes between commits, commit and working tree, etc |
|grep             | Print |lines| matching a pattern                             |
|log              | Show commit logs                                           |
|show             | Show various types of objects                              |
|status           | Show the working tree status                               |
<br>
>_grow, mark and tweak your common history_

|`git` **command**|**discription**|
|---------------|---------------|
|branch         | List, create, or delete branches                          |        
|commit         | Record changes to the repository                          |
|merge          | Join two or more development histories together           |
|rebase         | Reapply commits on top of another base tip                |
|reset          | Reset current HEAD to the specified state                 |
|switch         | Switch branches                                           | 
|tag            | Create, list, delete or verify a tag object signed with GPG|
|checkout       | Switch branches or restore working tree files             |
<br>
>_collaborate (see also: git help workflows)_

|`git` **command**|**discription**|
|---------------|---------------|
|fetch          | Download objects and refs from another repository          |
|pull           | Fetch from and integrate with another repository or a local branch|
|push           | Update remote refs along with associated object|
<br>

<span style="color:yellow;font-weight:700;font-size:20px">

~~Here i've made 3 commits with saved comments  and two without~~

</span>
<br>
