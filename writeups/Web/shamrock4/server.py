from bottle import request, route, run, static_file, HTTPResponse
from jwt.exceptions import PyJWTError
import base64
import json
import jwt

ENV="development"
SEC1, SEC2, SEC3, SEC4 =("<REDACTED>", "<REDACTED>", "<REDACTED>", "<REDACTED>")
STRONG_KEY="<REDACTED>"
DEV_KEY="<REDACTED>"

@route('/')
def home():
    return static_file('index.html', root='./views')

@route('/api/endpoint1')
def api1():
    admin = request.query.get('admin')
    if not admin:
        return HTTPResponse(body="No access, missing 'admin' query parameter.", status=401)
    if admin.lower() == 'true':
        return HTTPResponse(body=SEC1, status=200)
    else:
        return HTTPResponse(body="Forbidden, only for admins.", status=403)

@route('/api/endpoint2')
def api2():
    cookie_name = 'session_api2'
    if cookie_name not in request.cookies:
        return HTTPResponse(body="No access, missing 'session_api2' cookie", status=401)
    try:
        session_api2 = json.loads(base64.b64decode(request.cookies[cookie_name]))
    except (json.JSONDecodeError, base64.binascii.Error):
        return HTTPResponse(body="No access, invalid 'session_api2' cookie.", status=401)
    if session_api2.get('admin') is True:
        return HTTPResponse(body=SEC2, status=200)
    else:
        return HTTPResponse(body="Forbidden, only for admins.", status=403)

@route('/api/endpoint3')
def api3():
    auth_header = request.get_header('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
        try:
            # Include alg="none" for test in development, @todo remove in production ofc.
            algs = ['HS256','none']  
            header = jwt.get_unverified_header(token)
            verify_signature = header.get('alg') != 'none'
            claims = jwt.decode(jwt=token, key=STRONG_KEY if verify_signature else None, algorithms=algs, options={"verify_signature": verify_signature})
            if claims.get('admin') is True:
                return HTTPResponse(status=200, body=SEC3)
            else:
                return HTTPResponse(status=403, body="Forbidden, only for admins.")
        except PyJWTError:
            return HTTPResponse(status=401, body="No access, JWT token broken.")
    else:
        return HTTPResponse(status=401, body="No access, missing 'Authorization' header.")

@route('/api/endpoint4')
def api4():
    auth_header = request.get_header('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
        try:
            algs = ['HS256'] # alg="none" removed to prepare for production
            claims = jwt.decode(jwt=token, key=DEV_KEY, algorithms=algs, options={"verify_signature": True})
            if claims.get('admin') is True:
                return HTTPResponse(status=200, body=SEC4)
            else:
                return HTTPResponse(status=403, body="Forbidden, only for admins.")
        except PyJWTError:
            return HTTPResponse(status=401, body="No access, JWT token broken.")
    else:
        return HTTPResponse(status=401, body="No access, missing 'Authorization' header.")

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run(host='0.0.0.0', port=8080)
