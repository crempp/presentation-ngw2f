def app(environ, start_response):
    """Simplest possible WSGI application object"""
    data = 'Hello, World! (from WSGI)\n'
    status = '200 OK'

    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]

    start_response(status, response_headers)

    return iter([data])

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, application)
    srv.serve_forever()