# Part V Flask

Simple Flask example.

## Run

Start Nginx

```
$ cd part-V-flask
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-V-flask
$ nginx -c $SECTION/nginx/config/nginx.conf
```

Start Gunicorn

```
$ cd flask_app
$ gunicorn --workers=2 app:application
```

## Demo

```
$ telnet localhost 8080
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET / HTTP/1.0
```

## Clean up

```
$ nginx -s stop
```