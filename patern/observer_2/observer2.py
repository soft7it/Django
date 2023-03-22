class SubscriberOne:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got mesage "{}" '.format(self.name, message))

class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print('{} got mesage "{}" '.format(self.name, message))


class Publisher:
    def __init__(self):
        self.subscribers = dict()

    def register(self, who, callback=None):    # rec new data
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):      # delete data
        del self.subscribers[who]

    def dispatch(self, message):        # provide info
        for subscriber, callback in self.subscribers.items():
            callback(message)
