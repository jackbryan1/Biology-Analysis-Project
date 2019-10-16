def average_len(records):
        """Returns the average len for records"""
        RecordLength = [len(i) for i in records]
        return sum(RecordLength) / len(RecordLength)
