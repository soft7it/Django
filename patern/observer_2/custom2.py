from observer2 import *
from time import sleep

pub = Publisher()

bob = SubscriberOne('Bobik')
ali = SubscriberTwo('Alisa')
joh = SubscriberOne('Johnatan')

pub.register(bob, bob.update)
pub.register(ali, ali.receive)
pub.register(joh)

pub.dispatch('It`s lunch time')
sleep(2)
pub.unregister(joh)  # delete data
sleep(2)
pub.dispatch('Time for dinner')
