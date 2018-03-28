import urllib2
import json
import cookielib

def urllib2_request(url, method="GET", cookie="", headers={}, data=None):
    if data:
        data = json.dumps(data)

    cookie_jar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie_jar)
    opener = urllib2.build_opener(handler)
    opener.addheaders.append(['Cookie', 'k1=v1;k2=v2'])
    request = urllib2.Request(url=url, data=data, headers=headers)
    request.get_method = lambda :method
    response = opener.open(request)
    origin = response.read()

    return origin, cookie_jar


