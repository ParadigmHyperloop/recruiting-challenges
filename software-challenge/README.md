# Paradigm Software - Recruitment Challenge
## Intro
Welcome to Paradigm! If you are here, chances are you are interested in working on our software team. This challenge is meant to introduce you to our typical workflow. The goal is for you to set up a simple development environment, implement some code that we have scaffolded for you, and submit it to us for a code review.

## Development Environment Setup
### Text Editor
Before you get into writing some code, you need to have somewhere to write that code! As a team, we generally prefer [Visual Studio Code](https://code.visualstudio.com/) for our editing purposes, but you can use any text editor you want ([list of popular text editors](https://www.techradar.com/best/best-text-editors)).

### Git
In software development, code changes happen a lot, whether it is a new feature, or an old bug. In order to keep track of those changes, [git](https://en.wikipedia.org/wiki/Git) is used. Git is what is referred to as a Version Control System (VCS), and is the most ubiquitous VCS used in industry today. The first part of the challenge will be for you to get git working on your system. If you are on MacOS/Linux, this is easy, as you already have git most likely. Open a shell prompt, and type `git --version`, if this returns a version number, you are good to go! If you are on windows, you can install git from [here](https://gitforwindows.org/). MacOS/Linux users who don't already have git installed should be able to figure it out with a simple google search.

## Cloning the Repository

Along with git itself, there are also multiple hosting services which allow you to store your git repositories (directory containing all the code for your project) on their server, so that multiple developers are able to contribute code simultaneously. Paradigm uses Github for this (you are on our github right now if you're reading this!). For this part of the task, you will have to "clone" our repository to your computer, and then create a "branch" to work out of. In git, each repository has a "master" branch (think like branch on a tree) where the release code lives. When adding features or fixing bugs, a branch is created off of master, code is developed, and then after it is complete, is merged into master. By the end of this part of the challenge, you should have:
 - Cloned our repository to your computer
 - Created a branch to work out of - You can name your branch like this: "feature/*team number*/recruitment-challenge"

This can all be accomplished with some simple git commands in a shell. If you run into trouble, do what Software Developers do all the time and consult google, and [Stack Overflow](https://stackoverflow.com/).

## Writing the Code

Finally, for the actual coding part of the challenge, you will have to implement a python class that will be used to keep track of the current position of the hypothetical tunnel boring machine for the "Not-a-Boring" competition. Most of the implementation details will be left to you, and there are python docstrings which outline the parameter and return types
