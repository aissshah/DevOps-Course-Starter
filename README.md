# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

You will need a trello account and a board set-up. The board lists must also be called _To-Do_, _Doing_ and _Done_. To find out the board name, look at the url of the board and pick out the 8-character board ID.

## Running the App

### Locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Using Docker

The application can be run using Docker. Ensure you have [docker](https://docs.docker.com/get-docker/) installed to run the app this way.

#### Development Version

```sh
docker build --target development --tag todo-app:dev .
docker run --env-file ./.env -p 5100:5000 -it --mount type=bind,source="$(pwd)"/todo_app,target=/src/todo_app todo-app:dev
```

Visit [`http://localhost:5100/`](http://localhost:5100/) in your web browser to view the app. This version hot-reloads so you can see your changes.

#### Production Version

```sh
docker build --target production --tag todo-app:prod .
docker run --env-file ./.env -p 5200:8000 -it todo-app:prod
```

Go to [http://0.0.0.0:5200](http://0.0.0.0:5200) to see the application running.

#### Test Version

```sh
docker build --target test --tag todo-app:test .
docker run -it todo-app:test
```

The test logs should appear in the terminal.

## Testing the app

Unit tests can be run from the terminal by running `poetry run pytest`.