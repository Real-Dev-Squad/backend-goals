## How to deploy backend on Railway?

- Fork the repository.
- Signup on [Railway](https://railway.app/login)
- Goto [New Project](https://railway.app/new) page
- Choose the "Deploy from GitHub Repo" option
- Choose the forked `website-goals` repository from the dropdown.
  > If the repository is not listed, click on "Configure GitHub App" option and grant repository access for the forked repository.
- Click on "Add Variables" option and click on the "RAW Editor" option.
- Copy the content of `.env.example` file and add the required variable values.
- Goto Settings.
- Add "Start Command" as `python manage.py migrate && gunicorn config.wsgi`.
- Click on "Generate Domain" and add that hostname to `ALLOWED_HOSTS` env variable under the "Variables" tab.
  > For example - `HOSTS=goals-api.railway.app`
- Goto the generated domain and access the backend
