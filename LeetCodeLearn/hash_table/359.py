class Logger_1:
    def __init__(self):
        self.history_len = 10
        self.printed_log = {}

    def is_message_in_log(self, message):
        for value in self.printed_log.values():
            if message in value:
                return True
        return False

    def add_message(self, timestamp, message):
        if timestamp in self.printed_log.keys():
            self.printed_log[timestamp].add(message)
        else:
            self.printed_log[timestamp] = set([message])

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Time Complexity: O(1)
        Space Complexity: O(n), where n is quantity of unique messages in second

        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        for key in list(self.printed_log.keys()):
            if timestamp - key >= 10:
                del self.printed_log[key]

        if self.is_message_in_log(message):
            return False
        else:
            self.add_message(timestamp, message)

        return True


class Logger_2:
    def __init__(self):
        self._msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Time Complexity: O(1)
        Space Complexity: O(n), where n is unique message quantity
        """
        if message not in self._msg_dict.keys():
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timestamp
            return True
        return False


if __name__ == '__main__':
    logger = Logger_2()
    print(f'logger.shouldPrintMessage(1, "foo"); real: true, actual: {logger.shouldPrintMessage(1, "foo")}')
    print(f'logger.shouldPrintMessage(2,"bar"); real: true, actual: {logger.shouldPrintMessage(2,"bar")}')
    print(f'logger.shouldPrintMessage(3,"foo"); real: false, actual: {logger.shouldPrintMessage(3,"foo")}')
    print(f'logger.shouldPrintMessage(8,"bar"); real: false, actual: {logger.shouldPrintMessage(8,"bar")}')
    print(f'logger.shouldPrintMessage(10,"foo"); real: false, actual: {logger.shouldPrintMessage(10,"foo")}')
    print(f'logger.shouldPrintMessage(11,"foo"); real: true, actual: {logger.shouldPrintMessage(11,"foo")}')
