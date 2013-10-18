from google.appengine.ext import ndb

companys = ['yxtech', 'google', 'oracle', 'ibm']

class Member(ndb.Model):
    first_name = ndb.StringProperty(indexed=True, required=True)
    last_name = ndb.StringProperty(indexed=True, required=True)
    company = ndb.StringProperty(indexed=False, required=True)
    number = ndb.IntegerProperty()
    is_married = ndb.BooleanProperty()
    desc = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
