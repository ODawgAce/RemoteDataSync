class DataProcessor:
    def __init__(self, data):
        self.data = data

    def count_by_user(self):
        counts = {}
        for item in self.data:
            user_id = item.get("userId")
            counts[user_id] = counts.get(user_id, 0) + 1
        return counts