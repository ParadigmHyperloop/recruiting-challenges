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
 - Created a branch to work out of - You can name your branch like this: "feature/*name*/fall2020/recruitment-challenge"

This can all be accomplished with some simple git commands in a shell. If you run into trouble, do what Software Developers do all the time and consult google, and [Stack Overflow](https://stackoverflow.com/).

## Writing the Code

Finally, for the actual coding part of the challenge, you will have to implement a python class that will be used to keep track of the current position of the hypothetical tunnel boring machine for the "Not-a-Boring" competition. Most of the implementation details will be left to you, and there are python docstrings which outline the parameter and return types. You should be working out of the branch that you created, and periodically "committing" your code using git so that it keeps track of your changes.

## Submitting the Code

Once you have completed the coding section, it is now time to submit your code. To do this, you will submit a "Pull Request" to the github repository. This essentially will begin the process of code review, and in our actual development process this is where changes would be made based off of review comments. After review, the code would then be merged into our master branch. All you will need to do is to open a Pull Request, and provide a small description of your changes, and what they do (assume the reviewer has no prior knowledge of your code!).

Note: Make sure to format your pull request title as follows: "name/fall2020/recruitment-challenge/submission"

Note: You can also include photos of any workings, and any notes/ideas you had while completing this experiment! Simply add and commit the photo before you create your pull request.


## Appendix
As many of the applicants will not have much experience with OOP (what is that ???), so here are some quick notes! However, I would encourage you to google and or read ahead in your engi 3891 course notes 
to learn more, these notes are very sparse.

Main Points:
* OOP - Object Oriented Programming
* Keep data and ways to interact with that data together 
* A class is like a blueprint for an object (often classes represent real world objects)
* Can create many instances of a class, with different parameters! 
* An instance of a class **is** an object.

Example
```
class Car(): // Car blueprint!
    def __init__(self, make, model, max_speed, tire_size, is_coupe):
        """ Function that every class has - called a constructor! Initializes  the properties of the car, whenc reating an instance of the class - parameters are passed in! """
        self.make = make
        self.model = model
        self.max_speed = max_speed
        self.tire_size = tire_size
        self.is_coupe = is_coupe
        self.speed = 100
        self.position = 0,0,0

    Below are examples of methods, ways of interacting with the data stored in the class.
    They are just functions that are defined in a class.

    def accelerate():

    def brake():

    def park()

    def autopilot():

    def activate_cruise():

    def change_tire():

    def activate_vtec():

To create an instance of the class, you simply call the constructor and provide the following arguments: make, model, max_speed, tire_size, is_coupe

Civic = Car("Honda", "Civic", 1000, 20, True)

You can then view the value of the variables in the class, and call methods:

car_name = Civic.name
car_max_speed = Civic.maxspeed

Civic.drive_forward()
Civic.park()
Civic.activate_vtec()
```
# GLHF !
