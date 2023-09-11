
# streaming-03-bonus-KristenFinley

### Class: STREAMING DATA 44671-80/81FA23
### Assignment: P3-- Optional Bonus
### Name: Kristen Finley
### Date: September 9, 2023
---
## Directions:
Use your skills to create a custom project. Earn up to an additional 10%.
1. Create  your own custom project. Create a new repo named streaming-03-bonus-yourname. (e.g., streaming-03-bonus-case)
1. Create a new producer that reads from your earlier CSV file and writes messages to a new queue every 1-3 seconds.
1. Create a new consumer that reads your messages from this queue, and writes the messages to a new file as they are received.
1. Your README.md must include your name, the date.
1. Your README.md must provide a link to the original data.
1. Your README.md must clearly describe what you did, telling the story of your data, your producer, and your consumer,
1. Your README.md must display a screenshot of the two windows running concurrently. 
1. Add a .gitignore (telling which files and directories NOT to push up to GitHub). 
    - Recommendation:  copy .gitignore from an earlier repo. 
1. These are the important skills you want to demonstrate. Create unique streaming projects, using professional communication. I encourage you to give it a try.
---
## Link to the original data:

---
# Description of Tasks

## Task 1. Copied Over Previously Created Virtual Environment into Workspace

1. In a previous project, a local Python virtual environment ".venv" was created to isolate project's third-party dependencies from other projects.

1. Copied and verified  ".venv" directory  in project workspace.


## Task 2. Activated the Virtual Environment

In the same VS Code terminal window, activated the virtual environment.

`source .venv/bin/activate`

Verified the virtual environment name (.venv) in terminal prompt.

## Task 3. Installed Dependencies into the Virtual Environment using Homebrew and Pip

- Installed Homebrew in terminal with (.venv)
```shell    
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
   - Ran these two commands in your terminal to add Homebrew to your PATH:
```shell
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/kristenfinley/.zprofile

eval "$(/opt/homebrew/bin/brew shellenv)"
```

- To work with RabbitMQ, needed to install the pika library. Used the pip utility to install the libraries listed in requirements.txt into active virtual environment.


```shell
pip freeze > requirements.txt
pip install pika
```
## Task 4. Verify Setup

In your VS Code terminal window, ran the following commands to help verify setup.

```shell
python util_about.py
python util_aboutenv.py
python util_aboutrabbit.py
pip list
````

---
Describe what you did, telling the story of your data: 
- producer: A message with information about netflix shows was prepared and sent to the queue "netflix_queue". 
- consumer: Created a blocking connection to the RabbitMQ server. Used the connection to create a communication channel. Consumed messages from the queue.
---

## Screenshot of the two windows running concurrently 
see screenshot.png