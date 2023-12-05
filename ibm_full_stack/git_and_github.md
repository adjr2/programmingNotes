## Week 1

## Overview

A version control system allows you to keep track of changes to your documents. This makes it easy for you to recover older versions of your document if you make a mistake, and it makes collaboration with others much easier.

Version control systems are widely used for things involving code, but you can also version control images, documents, and any number of file types.

The SSH protocol is a method for secure remote login from one computer to another.

A repository contains your project folders that are set up for version control.

A fork is a copy of a repository.

A pull request is the way you request that someone reviews and approves your changes before they become final.

A working directory contains the files and subdirectories on your computer that are associated with a Git repository.

Git Basics:

- When starting out with a new repository, you only need create it once: either locally, and then push to GitHub, or by cloning an existing repository by using the command git init.
- git add: moves changes from the working directory to the staging area.
- git status: allows you to see the state of your working directory and the staged snapshot of your changes.
- git commit: takes your staged snapshot of changes and commits them to the project.
- git reset: undoes changes that you’ve made to the files in your working directory.
- git log: enables you to browse previous changes to a project.
- git branch: lets you create an isolated environment within your repository to make changes.
- git checkout: lets you see and change existing branches.
- git merge: lets you put everything back together again.

### Introduction to Github

What is special about the Git Repository model? Git is designed as a distributed version-control system. Primarily focused on tracking source code during development. Contains elements to coordinate among programmers, track changes, and support non-linear workflows.

Git is a distributed version-control system that is used to track changes to content. It serves as a central point for collaboration with a particular focus on agile development methodologies. In a central version control system, every developer needs to check out code from the central system and commit back into it. As Git is a distributed version control, each developer has a local copy of the full development history, and changes are copied from one such repository to another. Each developer can act as a hub.

A Repository is: A data structure for storing documents including application source code. A repository can track and maintain version-control.

GitLab is a complete DevOps platform, delivered as a single application. GitLab provides access to Git repositories, controlled by source code management. With GitLab, developers can: Collaborate, reviewing code, making comments and helping to improve each other’s code. Work from their own local copy of the code. Branch and merge code when required. Streamline testing and delivery with Built-in Continuous Integration (CI) and Continuous Delivery (CD).

### Github Repositories

An organization is a collection of user accounts that owns repositories. Organizations have one or more owners, who have administrative privileges for the organization.

## Week 2

### GitHub Branches

Some best practices : Don’t end the commit message with a period. Keep commit messages under 50 characters – use the extended window for the details. Always write in an “active” voice.

Pull is used to initiate the merging of branches in a way to capture changes. A pull request makes the proposed (committed) changes available for others to review and use. A pull can follow any commits, even if code is unfinished. A pull requires a user to approve the changes.

### Cloning and Forking

Cloning generally refers to creating a copy of a repository on your local machine. Cloned copies can be kept in sync between the two locations. Forking allows you to modify or extend a project without affecting the original project. Frequently, this is used to take an existing project and make it the starting point for your new project.

Collaborating with others involves managing these remote repositories and involves push, pull, and fetch operations to and from them when you need to share work. Use git push to transfer your changes to the remote repo. Use git fetch to transfer any changes from the remote repo to your local repo. It does not merge those changes to the branch you are working on. You can perform a merge manually if you want. Use git pull to transfer any changes from the remote repo to your local repo, and merge them to a branch.

To keep a fork in sync with the original work from a local clone. First, create a local clone of the project. To configure Git to sync your fork: Open a Terminal and change to the directory containing the clone. Type “git remote –v” This gives you the remote repository. Type `git remote add upstream <PASTE>` with the pasted-in directory that you used in creating your clone. Adding upstream adds the original repository as a new remote repository labelled upstream. If you type “git remote –v”, you’ll see the change reflected.

Other commands of interest include “git fetch upstream” to grab upstream branches and “git merge upstream/master” which merges changes into the master branch. You will also see "git pull upstream" used to fetch and merge the remote branch in the same step. “Git pull upstream" reduces the number of steps to sync with a remote branch, but the automatic merges are not always desired.

### Managing GitHub Projects

Multiple roles are involved in managing a project; a developer, an integrator, and a repository administrator.

An integrator in a group project receives changes made by others, reviews and integrates them, responds to pull requests, and publishes the result for others to use. Integrators use the following commands in addition to the ones needed by participants.

The repository administrator structures how the repository is organized and how users interact with the repository. They also manage communities, asset types, relationships, categories and attributes. A repository administrator sets up and maintains access to the repository for developers. They also configure the servers needed for accessing the web services and documentation, define email and index settings, and manage the look and feel of the application. Repository admins can use GitHub actions to automate software workflows including continuous integration and continuous delivery or CICD.
