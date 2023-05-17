# django-docker

- Sample project to run django app using docker.

### Installation Steps:

- Clone the repository

- Create virtual environment at the directory where venv is already ignore at .gitignore file

```
pip install virtualenv
```
```
cd /to/project/directory
```
```
virtualenv -p=python3.8 venv
```

- Activate the virtual environment & install requirements

```
source /venv/bin/activate
```
```
pip install -r requirements.txt
```

- Generate a local settings file local.py same as resumex/settings/example-production.py


- Run the following command for database migrations:

```
python manage.py migrate
```

- Build docker image and run the project:

```
sudo docker-compose build

sudo docker-compose up -d

sudo docker-compose down
```

