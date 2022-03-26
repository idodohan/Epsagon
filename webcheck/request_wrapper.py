import time

import requests
from .request_data import RequestData, RequestsData
import uuid
from functools import wraps

requests_data = RequestsData()


def requests_get_decorator(basic_get_function):
    """
    a decorator for the basic get function
    :param basic_get_function: request.get function as a parameter
    :return:
    """

    @wraps(basic_get_function)
    def wrapped_get_function(url: str, params=None, **kwargs):
        """
        the actual wrapper of the function
        :param url:
        :param params:
        :param kwargs:
        :return:
        """
        start_time = time.time()

        # calls the GET function
        res = basic_get_function(url, params=params, **kwargs)

        # additional data for the request_data object
        duration = res.elapsed.microseconds/10e6
        target_url = url
        status_code = res.status_code
        request_id = uuid.uuid4().hex

        # creates the request data object with all the necessary data
        request_data = RequestData(start_time=start_time,
                                   duration=duration,
                                   target_url=target_url,
                                   status_code=status_code,
                                   request_id=request_id)

        # adds it to the data dict (temporary data of the sdk... later will be added to the db)
        requests_data.add_request_data_to_dict(request_data)

        return basic_get_function(url, params=params, **kwargs)

    return wrapped_get_function

# wraps the get function
requests.get = requests_get_decorator(requests.get)
















def get_data() -> dict:
    """
    :return: calls the requests_data get_data function. eventually returns the data collected from the sdk
    """
    return requests_data.get_data()
