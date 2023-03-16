# ##############  Provider  ###############
# [app] <------ proxy(intercept/logger) ----->
class Box:

    # LIGHTweight proxy
    def __getattr__(self, name):
        print(f'You are trying to acces "{name}"')

    def __setattr__(self, name, value):
        print(f"You are trying to set '{name}'={value}")
    # LIGHTweight proxy

# #########  Consumer  ##################################
b = Box()
b.value = 100  # write
b.x = 100   # write
# v = b.x    # read the value from the box -- for __getattr__

# [app] ----> write proxy ----> [Box]
# [app] <---- read proxy <---- [Box]