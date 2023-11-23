## Setup

- Create a virtual environment for your Python project. A virtual environment is a self-contained environment that allows you to isolate your project dependencies and avoid conflicts with other projects. Learn more here.
- Install the Python virtualenv package using the command 
```
pip install virtualenv
```
- Create a virtual environment by running the command in the root folder of your repository.
```
virtualenv venv
``` 
- Activate the virtual environment by running the command 
```
source venv/bin/activate
```
- Install the project dependencies by running the command 
```
pip install -r requirements.txt
```
> This will install all the necessary packages listed in the requirements.txt file.
- Setup the env files
```
Create a `.env` file in the root directory, and copy paste the code from the `.env.example` file to it
```
- Install [docker](https://docs.docker.com/get-docker/) 
- Spin up the database
```
docker-compose up db
```
- Set up the database by running the command
```
python manage.py migrate
```
- Finally, start the development server by running the command 
```
python manage.py runserver
```
> This will start a local web server and allow you to access your Django project in a web browser.

By following these steps, you can ensure that your Python project is properly set up with a virtual environment, the necessary dependencies, and a working database. This makes it easier to develop and deploy your project without running into conflicts or issues.
