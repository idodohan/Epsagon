from . import request_wrapper


def get_data() -> dict:
    """
    :return: calls the wrapper get_data function. eventually returns the data collected from the sdk
    """
    return request_wrapper.get_data()
