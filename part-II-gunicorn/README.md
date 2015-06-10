# Part II Gunicorn

Basic Gunicorn example.

## Run

Start Nginx

```
$ cd part-II-gunicorn
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-II-gunicorn
$ nginx -c $SECTION/nginx/config/nginx.conf
```

Start Gunicorn

```
$ cd gunicorn
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