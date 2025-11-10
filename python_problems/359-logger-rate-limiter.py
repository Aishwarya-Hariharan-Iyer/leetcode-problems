class Logger(object):

    def __init__(self):
        self.last_message_tracker = dict({})
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        last_timestamp = self.last_message_tracker.get(message, -1)
        if last_timestamp == -1 or timestamp - last_timestamp >= 10:
            self.last_message_tracker[message] = timestamp
            return True
        else:
            return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
