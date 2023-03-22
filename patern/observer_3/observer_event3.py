class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got mesage "{}" '.format(self.name, message))

class Publisher:
    def __init__(self, events):
        self.subscribers = {event : dict()
                            for event in events}
    def get_subsribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):    # rec new data
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subsribers(event)[who] = callback

    def unregister(self, event, who):      # delete data
        del self.get_subsribers(event)[who]

    def dispatch(self, event, message):        # provide info
        for subscriber, callback in self.get_subsribers(event).items():
            callback(message)
######################################################
