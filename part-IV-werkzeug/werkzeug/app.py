from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    result = ['Hello, World! (from Werkzeug)\n']
    return Response(result, mimetype='text/html')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, application, use_reloader=True)