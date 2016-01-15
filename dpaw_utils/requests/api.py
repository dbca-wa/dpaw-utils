import requests

session_key_header = "X_SESSION_KEY"
http_session_key_header = "HTTP_" + session_key_header

def _set_session_key(user_request,kwargs):
    """
    Get the session key from user request for sso
    if not found, return None
    """
    if not user_request:
        return 

    session_key = None
    request_name = user_request.__module__ + "." + user_request.__class__.__name__
    try:
        if request_name[0:7] == "bottle.":
            session_key = user_request.get_header(session_key_header,user_request.get_header(http_session_key_header,None))
        elif request_name[0:7] == "django.":
            session_key = user_request.META.get(http_session_key_header,user_request.META.get(session_key_header,None))
    except:
        pass

    if not session_key:
        #Try to use the default way to retrieve the session key
        try:
            session_key = user_request.META.get(http_session_key_header,user_request.META.get(session_key_header,None))
        except:
            pass

    if session_key:
        cookies = kwargs.get("cookies",{})
        cookies["_dpaw_wa_gov_au_sessionid"] = session_key
        kwargs["cookies"] = cookies

    return 

def options(url, **kwargs):
    """ A wrapper of requests.set.
    This method will automatically add user's session key as the cookie to enable sso 

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    _set_session_key(user_request,kwargs)

    return requests.options(url,**kwargs)

def head(url, **kwargs):
    """ A wrapper of requests.head.
    This method will automatically add user's session key as the cookie to enable sso 

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    _set_session_key(user_request,kwargs)

    return requests.head(url,**kwargs)


def get(user_request,url, **kwargs):
    """ A wrapper of requests.get.
    This method will automatically add user's session key as the cookie to enable sso 

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    _set_session_key(user_request,kwargs)
    
    return requests.get(url,**kwargs)

def post(url, data=None, json=None, **kwargs):
    """ A wrapper of requests.post.
    This method will automatically add user's session key as the cookie to enable sso 

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    _set_session_key(user_request,kwargs)

    return requests.post(url,data,json,**kwargs)

def put(url, data=None, **kwargs):
    """ A wrapper of requests.put.
    This method will automatically add user's session key as the cookie to enable sso 

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    _set_session_key(user_request,kwargs)

    return requests.put(url,data,**kwargs)

def patch(url, data=None, **kwargs):
    """ A wrapper of requests.patch.
    This method will automatically add user's session key as the cookie to enable sso 

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    _set_session_key(user_request,kwargs)

    return requests.patch(url,data,**kwargs)

def delete(url, **kwargs):
    """ A wrapper of requests.delete.
    This method will automatically add user's session key as the cookie to enable sso 

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    _set_session_key(user_request,kwargs)

    return requests.delete(url,**kwargs)
