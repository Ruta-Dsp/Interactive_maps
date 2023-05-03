## usefull commands

### GIT
1. check the status of your cloned repo --> **git status**
    check which is the current branch --> **git branch**

2. pull from production to make sure you are up to date --> **git pull**

3. create a new branch for your commit --> **git checkout -b name**

4. add new files to your commit --> **git add .**

5. commit your changes --> **git commit -m “message”**

6. push to production --> **git push** 

7. approve the PR --> go on GitHub (website) and merge the PR

8. go back to the main branch --> **git checkout main** 



### Use virtual environment

2. create a new virtual environment (only needed once) --> **python -m venv env**

3. activate the virtual env on win --> **.\env\Scripts\activate**

4. install all the packages needed for the project --> **pip3 install -r requirements.txt**
   install all the packages needed for the project --> **pip3 install -r requirements.txt --user**

5. add new packages to requirements.txt if needed --> **pip list** (list all the packages installed in the environemnt)

## Create the requirements.txt with all the package used in the env

For Unix : pip3 freeze > requirements.txt 
For Windos: pip freeze > requirements.txt

## Create the requirements.txt with only package used in the scripts inside the folder
pipreqs --encoding=utf-8 /percorso/alla/cartella/progetto
