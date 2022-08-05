import os
import jinja2
import webapp2

from google.appengine.ext import db
from google.appengine.ext import ndb

class dbLaptop(db.Model):
    brand = db.StringProperty()
    gen = db.IntegerProperty()

class ndbLaptop(ndb.Model):
    brand = ndb.StringProperty()
    gen = ndb.IntegerProperty()


def create_db_database(brand_list, gen_list, key_list, no_of_records = 10):
    for i in range(len(brand_list)):
        db_l = dbLaptop.get_or_insert(key_list[i])
        db_l.brand = brand_list[i]
        db_l.gen = gen_list[i]
        db_l.put()

def copy_to_ndb(items):
    for item in items:
        key = item.key()
        ndb_l = ndbLaptop.get_or_insert(key.name())
        ndb_l.brand = item.brand
        ndb_l.gen = item.gen
        ndb_l.put()

class MainPage(webapp2.RequestHandler):
    def get(self):
        brand_list = ['hp', 'dell', 'apple', 'acer', 'asus', 'hp', 'acer', 'hp', 'lenovo']
        gen_list = [1, 3, 5, 3, 6, 8, 9, 5, 8]
        key_list = []
        batch_size = 6

        for i in range(len(brand_list)):
            key_list.append('laptop'+str(i+1))

        create_db_database(brand_list, gen_list, key_list)

        query = dbLaptop.gql('')
        items = query.fetch(batch_size)
        copy_to_ndb(items)

        more_results = query.count(batch_size) #the 2 in supplied as arg tests whether there are more than 2 queries left,
        #if yes then it returns 2

        # if query.count() is used without the number '2' the results are strange
        # Stuck on this problem for 2 days but still couldn't figure out
        # also need to ask someone about this

        while more_results==batch_size:
            cursor = query.cursor()
            query = query.with_cursor(cursor)
            more_results = query.count(batch_size)
            print(more_results)
            results = query.fetch(batch_size)
            copy_to_ndb(results)

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)