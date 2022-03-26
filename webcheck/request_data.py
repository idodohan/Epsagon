
class RequestData:
    """
    represents a single request data
    """
    def __init__(self, start_time: float, duration: float, target_url: str, status_code: int, request_id: hex):
        self.start_time = start_time
        self.duration = duration
        self.target_url = target_url
        self.status_code = status_code
        self.request_id = request_id


class RequestsData:
    """
    represents a container for the requestdata objects
    """
    def __init__(self):
        self.requests_data_dict = {}

    def add_request_data_to_dict(self, request_data: RequestData) -> None:
        self.requests_data_dict[request_data.request_id] = request_data

    def get_data(self) -> dict:
        """
        :return: returns the data collected from the sdk
        """
        return self.requests_data_dict
