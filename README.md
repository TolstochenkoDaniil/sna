# Description

## Design and implementation

### Functional

Web application provides to user features described below:

- Access to the educational content of methods aimed to overcome social network addiction

- Track their progress of hours spent in social media

- Compare efficiency of the proposed methods on interactive graph and watch statistic in real time

- **(Coming)** Start timer to notify user via emails of time spent in social media

### Non functional

- Web application is totally free

- Intuitive design

- Easy and light registration process (only email and name)

- Any time access (deployed in cloud server)

## Setup

```sh
git clone https://github.com/TolstochenkoDaniil/sna.git .
```

Create virtual environment

```sh
python -m venv env
```

And activate it

```sh
source env/scripts/activate
```

Install dependencies

```sh
pip install -r requirements.txt
```

Application is hosted on google cloud, so to run app locally with database connection follow this [tutorial](https://cloud.google.com/python/django/appengine)

To start app locally do the following from project directory

```sh
python sna/manage.py makemigrations
python sna/manage.py migrate
python sna/manage.py runserver
```

After that app will be accessible at [localhost](http://127.0.0.1:8000/)

To provide sensitive data do

```sh
cd sna/sna
touch .env
```

Put any variables used in `./sna/sna/settings.py` like this  
`DEBUG = 0`
