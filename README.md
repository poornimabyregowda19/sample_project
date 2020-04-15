# sample_project
Django project. using multiple env's based on the given environment. (development , production)
and run on gunicorn

##### install djnago-environ
`pip install django-environ`

##### install gunicorn
`pip install gunicorn`

##### create a folder settings inside project directoy 
-- settings  <br />
    .__init__.py  <br />
    .env  <br />
    .env_prod  <br />
    development.py  <br />
    production.py  <br />

##### manage.py and wsgi file. add following configuration
```
 if os.getenv("SIMPLE_SETTINGS") and not os.getenv("SIMPLE_SETTINGS") in ["<project-name>.settings.development",
                                                                         "<project-name>.settings.production"]:
        os.environ.setdefault("SIMPLE_SETTINGS", "project-name>.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<project-name>.settings.development")
```

###### we need to set 'SIMPLE_SETTINGS' in os.envion externally. create .env.system in settings foldere
```
    SIMPLE_SETTINGS='<project-name>.settings.development'
```

###### using gunicorn and systemctl , EnvironmentFile tag create the os environment variables externally

add this file in /etc/systemd/system

```angular2
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=poornima
Group=www-data
WorkingDirectory=/home/poornima/PycharmProjects/cmms
EnvironmentFile=/home/poornima/PycharmProjects/cmms/cmms/settings/.env.system
ExecStart= /home/poornima/PycharmProjects/cmms/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8002 cmms.wsgi


[Install]
WantedBy=multi-user.target
```    

run following commands to start and enable service in systemctl <br/>
`sudo systemctl start gunicorn`
`sudo systemctl enable gunicorn`

check logs in <br/>
`sudo journalctl -u gunicorn`

after starting gunicorn to 0.0.0.0:8002/data it displays the setting envionment presently used based on .env.system file
