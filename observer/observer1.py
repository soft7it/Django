class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print ('{} got mesage "{}" '.format(self.name, message))
        
class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):    # rec new data
        self.subscribers.add(who)

    def unregister(self, who):      # delete data
        self.subscribers.discard(who)

    def dispatch(self, message):        # provide info
        for subscriber in self.subscribers:
            subscriber.update(message)        