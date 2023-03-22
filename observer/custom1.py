from observer1 import Publisher, Subscriber

pub = Publisher()

bob = Subscriber('Bobik')
ali = Subscriber('Alisa')
joh = Subscriber('Johnatan')

pub.register(bob)
pub.register(ali)
pub.register(joh)

pub.dispatch('It`s lunch time')
pub.unregister(joh)  # delete data
pub.dispatch('Time for dinner')
