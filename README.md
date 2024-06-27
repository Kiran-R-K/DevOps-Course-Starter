# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Trello API

This app uses Trello to connect using the Trello API you will need to get  an account [`https://trello.com/`](https://trello.com/) with an API token, API key and Board ID.

Once you have these save a copy of `.env.template` as `.env` in the project root folder with your API token, API key and Board ID. Make sure this file is in the `.gitignore` file so that the details aren't saved to git.

## Running the App with poetry

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Building and Running the App with Docker

Make sure you have docker installed

### Development

To build the container run:
```bash
$ docker build --tag todo-app:dev --target development .
```

To run the container run:
```bash
$ docker run --publish 5000:5000 --env-file .env --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app. The container will have hot reloading

### Production

To build the container run:
```bash
$ docker build --tag todo-app:prod --target production .
```

To run the container run:
```bash
$ docker run --publish 5000:5000 --env-file .env todo-app:prod
```

## Testing the App

Tests are run using pytest, this will have been installed when you ran `poetry install`. It was installed using:
```bash
$ poetry add pytest
``` 

You can run the tests by running:
```bash
$ poetry run pytest
``` 

## Deploying the App to a Virtual Machine

Note: the deployment files will not be kept up to date - so they will need to be updated before deployment

To deploy the app using virtual machines - you will need a control node VM and a host VM (or multiple host VMs).

Install ansible on the control node, copy the files in the ansible folder into the control node VM.
Add the IP address(es) of your host node(s) to the `inventory.yaml` file
Open a terminal in the control node and run:
```bash
$ ansible-playbook playbook.yml -i inventory.yml
```
You will need to have the `TRELLO_API_KEY` and `TRELLO_API_TOKEN` available, and input them when prompted.

The todoapp should then be running at `{host_ip}:5000`