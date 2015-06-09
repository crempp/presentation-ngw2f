# Part V Flask

simple Flask example.

## Run

Start Gunicorn

```
$ cd gunicorn
$ gunicorn --workers=2 app:app
```

In a new window start nginx

```
$ export SECTION=/Users/crempp/projects/presentation-ngw2f/part-III-gunicorn
$ nginx -c $SECTION/nginx/config/nginx.conf
$ nginx -s stop
```

Go to Flask directly: http://127.0.0.1:8000/

Go to Flask through Nginx: http://127.0.0.1:8080/

or

```
$ telnet localhost 8080
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET / HTTP/1.0
```