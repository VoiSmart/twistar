from twisted.enterprise import adbapi
from twisted.internet import defer

from twistar.dbobject import DBObject
from twistar.registry import Registry

from sqlite_config import initDB, tearDownDB
#from mysql_config import initDB, tearDownDB
#from postgres_config import initDB, tearDownDB

class User(DBObject):
    HASMANY = ['pictures', 'comments']
    HASONE = ['avatar']
    HABTM = ['favorite_colors']

class Picture(DBObject):
    BELONGSTO = ['user']

class Comment(DBObject):
    BELONGSTO = ['user']

class Avatar(DBObject):
    pass

class FavoriteColor(DBObject):
    HABTM = ['users']    

class Blogpost(DBObject):
    HABTM = [dict(name='categories', join_table='posts_categories')]

class Category(DBObject):
    HABTM = [dict(name='blogposts', join_table='posts_categories')]

class FakeObject(DBObject):
    pass

class Coltest(DBObject):
    pass

class Boy(DBObject):
    HASMANY = [{'name': 'nicknames', 'as': 'nicknameable'}]

class Girl(DBObject):
    HASMANY = [{'name': 'nicknames', 'as': 'nicknameable'}]    

class Nickname(DBObject):
    BELONGSTO = [{'name': 'nicknameable', 'polymorphic': True}]

class Pen(DBObject):
    pass

class Table(DBObject):
    HABTM = ['pens']
    HASMANY = ['rubbers']

class Rubber(DBObject):
    pass

class Role(DBObject):
	BELONGSTO = ['serviceclass']

class Serviceclass(DBObject):
	HASMANY = ['roles']
	BELONGSTO = ['superclass']

class Superclass(DBObject):
	HASONE = ['serviceclass']

Registry.register(Picture, User, Comment, Avatar, FakeObject, FavoriteColor)
Registry.register(Boy, Girl, Nickname)
Registry.register(Blogpost, Category)
Registry.register(Pen, Table, Rubber)
Registry.register(Role, Serviceclass, Superclass)
