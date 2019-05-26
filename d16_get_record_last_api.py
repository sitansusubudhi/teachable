# class Log(object):
#     def __init__(self, n):
#         self._log = []
#         self.n = n

#     def record(self, order_id):
#         if len(self._log) >= self.n:
#             self._log.pop(0)
#         self._log.append(order_id)

#     def get_last(self, i):
#         return self._log[-i]

class Log(object):
    def __init__(self, n):
        self.n = n
        self._log = []
        self._cur = 0

    def record(self, order_id):
        if len(self._log) == self.n:
            self._log[self._cur] = order_id
        else:
            self._log.append(order_id)
        self._cur = (self._cur + 1) % self.n

    def get_last(self, i):
        return self._log[self._cur - i]

api_object = Log(3)
api_object.record(12)
api_object.record(13)
api_object.record(14)
api_object.record(15)

print(api_object.get_last(3))