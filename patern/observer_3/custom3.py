from observer3 import *
from time import sleep


pub = Publisher(['lunch', 'dinner'])

bob = Subscriber('Bobik')
ali = Subscriber('Alisa')
joh = Subscriber('Johnatan')
joh = Subscriber('Johnatan')

pub.register('lunch', bob)
pub.register('dinner', ali)
pub.register('lunch', joh)
pub.register('dinner', joh)

pub.dispatch('lunch', 'It`s lunch time')
pub.dispatch('dinner', 'Dinner is served')