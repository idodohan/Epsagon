
def prepare_data_for_db(requests_data: dict) -> list:
    """
    :param requests_data: dictionary of requestdata objects
    :return: parses the requestdata object into dictionary
    """
    return [value.__dict__ for key, value in requests_data.items()]
