class Solution:

    def countSeniors(self, details: List[str]) ->int:
        senior_count = 0
        for passenger_info in details:
            age = int(passenger_info[11:13])
            if age > 60:
                senior_count = senior_count + 1
        return senior_count
