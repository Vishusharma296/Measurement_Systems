** Github Basic Notes **

Git is an open source version control system used to keep track of changes in repositories, bugs in code and rollbacks of repositories to previous versions.

## GitHub Basics:

- **Repositories**: 
  - Git repositories are where your code lives. Each repository contains all the project files and revision history.
- **Branches**: 
  - Branches are separate lines of development that allow you to work on different features or fixes simultaneously.
- **Commits**: 
  - Commits are snapshots of your repository at a specific point in time. Each commit has a unique identifier and includes changes made to the files.
- **Pull Requests**: 
  - Pull requests are proposed changes to a repository. They allow you to discuss and review changes before merging them into the main branch.

### GitHub Features:

- **Issues**: 
  - Issues are used to track tasks, bugs, and feature requests. They can be assigned to team members, labelled, and discussed.
- **Projects**: 
  - Projects help you organize and prioritize work with customizable boards. You can create tasks, track progress, and visualize workflows.
- **Wiki**: 
  - Wikis allow you to document your project, including installation instructions, usage guidelines, and FAQs.
- **Actions**: 
  - GitHub Actions automate workflows, such as testing, building, and deploying your code. You can create custom workflows using YAML files.

### Collaborative Development:

- **Forks**: 
  - Forks are copies of a repository. They allow you to experiment with changes without affecting the original project.
- **Collaborators**: 
  - Collaborators are individuals with access to a repository. They can push changes directly to the repository.
- **Code Review**: 
  - Code reviews are discussions about proposed changes. Reviewers can leave comments, suggest improvements, and approve or reject pull requests.

### GitHub Security:

- **Branch Protection**: 
  - Branch protection rules prevent unauthorized changes to specific branches. You can require code reviews, status checks, and other criteria before merging changes.
- **Security Alerts**: 
  - GitHub automatically scans repositories for known security vulnerabilities and notifies maintainers.
- **Dependency Graph**: 
  - The dependency graph displays the dependencies of your project and any known vulnerabilities in those dependencies.

### GitHub Integration:

- **CI/CD**: 
  - Continuous Integration (CI) and Continuous Deployment (CD) automate testing and deployment processes. GitHub integrates with various CI/CD services and tools.
- **Webhooks**: 
  - Webhooks allow you to receive notifications about events in your repository, such as push events, issue updates, or pull request merges.

***

## List of important Github Commands

| Command                   | Description of Commands                                                                  |
|---------------------------|------------------------------------------------------------------------------------------|
| `git init`                | Initialize a new Git repository in the current directory.                                 |
| `git clone <repository>`  | Clone a repository from a URL into a new directory.                                      |
| `git add <file>`          | Add file(s) to the staging area, preparing them to be committed.                         |
| `git commit -m "message"` | Record changes to the repository with a commit message.                                    |
| `git status`              | Show the status of modified files in the working directory.                               |
| `git diff`                | Show changes between commits, commit and working tree, etc.                               |
| `git push`                | Push local changes to a remote repository.                                                |
| `git pull`                | Fetch from and integrate with another repository or a local branch.                        |
| `git branch`              | List, create, or delete branches.                                                         |
| `git checkout <branch>`   | Switch branches or restore working tree files.                                            |
| `git merge <branch>`      | Merge changes from one branch into another.                                                |
| `git log`                 | Show commit logs.                                                                         |
| `git remote add <name> <url>` | Add a new remote repository and name it.                                                |
| `git fetch`               | Download objects and refs from another repository.                                         |
| `git stash`               | Stash changes in a dirty working directory away.                                          |
| `git tag`                 | Create, list, delete or verify a tag object signed with GPG.                               |
| `git revert <commit>`     | Create a new commit that undoes changes made by one or more existing commits.             |
| `git reset <file>`        | Reset current HEAD to the specified state.                                                |
| `git rm <file>`           | Remove files from the working tree and from the index.                                     |
| `git config`              | Get and set repository or global options.                                                  |


## YouTube Tutorials:

- [How to upload a project/folder to github](https://www.youtube.com/watch?v=p8bZBvcFPuk&lc=UgwQlQmQQWOdjxRbroB4AaABAg.A1zNvtncqmKA207le2ZizF)
- [Github for Beginners](https://www.youtube.com/watch?v=RGOj5yH7evk&t=181s)
