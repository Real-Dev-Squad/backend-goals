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
or depending on your operating system.
```
venv/bin/activate
``` 
- Configure your IDE to use the Python interpreter from your virtual environment. This ensures that your project dependencies are properly recognized and used. Here is a guide for VS Code.
- Install the project dependencies by running the command 
```
pip install -r requirements.txt
```
- Spin up the postgresql server, the container
```
docker-compose -f /deploy/compose.yml up -d
```
- Setup the env files
```
Create a `.env` file in the root directory, and copy paste the code from the `sample.env` file to it
```

> This will install all the necessary packages listed in the requirements.txt file.
- Create a `.env` file in the root folder and copy paste the content from the .env.example.
- Set up the database by running the commands 
```
python manage.py makemigrations
```
```
python manage.py migrate
```
> These commands create and apply database migrations based on the models defined in your project.
- Create an admin user by running the command 
```
python manage.py createsuperuser
```
> This will allow you to access the Django admin panel and perform administrative tasks.
- Finally, start the development server by running the command 
```
python manage.py runserver
```
> This will start a local web server and allow you to access your Django project in a web browser.

By following these steps, you can ensure that your Python project is properly set up with a virtual environment, the necessary dependencies, and a working database. This makes it easier to develop and deploy your project without running into conflicts or issues.
