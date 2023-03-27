# How to deploy backend on Railway?

1. Fork the [website-goals](https://github.com/Real-Dev-Squad/website-goals) repository.
2. Signup on [Railway](https://railway.app/login)
3. Goto [New Project](https://railway.app/new) page
4. Choose the "Deploy from GitHub Repo" option
5. Choose the forked `website-goals` repository from the dropdown. If the repository is not listed, click on "Configure GitHub App" option and grant repository access for the forked repository.
6. Click on "Add Variables" option and click on the "RAW Editor" option. Copy the content of `.env.example` file and add the required variable values.
7. Goto Settings. 
8. Update the "Root Directory" to `/api` and add "Start Command" as `python manage.py migrate && gunicorn django_jsonapi.wsgi`.
9. Click on "Generate Domain" and add that hostname to `HOSTS` env variable under the "Variables" tab.
For example - `HOSTS=goals-api.railway.app`
10. Goto the generated domain and access the backend