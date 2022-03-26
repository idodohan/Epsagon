

class Queries:
    """
    this class is responsible for the database queries
    """
    def __init__(self, db):
        self.db = db

    def get_data_by_id(self, request_id) -> dict | str:
        """
        :param request_id: uuid of the request
        :return: returns the corresponding object
        """
        try:
            return self.db.find({"request_id": request_id})[0]
        except:
            return "ID doesnt exist..."

    def get_data_by_timeframe(self, start_time: float, end_time: float) -> list:
        """
        :param start_time:
        :param end_time:
        :return: returns a list of requests that occurred between start_time and end_time
        """
        return list(self.db.find({"start_time": {"$gt": start_time, "$lt": end_time}}))

    def get_most_commonly_visited_website(self) -> list:
        """
        returns a list of most commonly visited websites. thats because i wanted to support a case where there are multiple
        websites with the same count of visits
        :return:
        """
        by_count_list = list(self.db.aggregate([{"$sortByCount": "$target_url"}]))
        most_common_url = by_count_list[0]
        most_common_urls = [x['_id'] for x in by_count_list if x['count'] == most_common_url['count']]
        return most_common_urls
