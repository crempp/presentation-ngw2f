# Part IV Werkzeug

Basic Werkzeug example.

## Run

Start Nginx

```
$ cd part-IV-werkzeug
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-IV-werkzeug
$ nginx -c $SECTION/nginx/config/nginx.conf
```

Start the Gunicorn server

```
$ cd werkzeug
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