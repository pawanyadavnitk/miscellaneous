import os
import jinja2
import webapp2

from google.appengine.ext import db
from google.appengine.ext import ndb

# jinja_env = jinja2.Environment(
#                     loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
#                     autoescape = True)

class dbLaptop(db.Model):
    brand = db.StringProperty()
    gen = db.IntegerProperty()

class ndbLaptop(ndb.Model):
    brand = ndb.StringProperty()
    gen = ndb.IntegerProperty()

def create_db_database(brand_list, gen_list, key_list, no_of_records = 10):
    for i in range(10):
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

brand_list = ['hp', 'dell', 'apple', 'acer', 'asus', 'hp', 'acer', 'hp', 'lenovo', 'apple']
gen_list = [1, 3, 5, 3, 6, 8, 9, 5, 8, 8]
key_list = []

for i in range(10):
    key_list.append('laptop'+str(i+1))

create_db_database(brand_list, gen_list, key_list)

#query = db.GqlQuery('SELECT * FROM dbLaptop')
query = dbLaptop.gql("")
items = query.fetch(2)
copy_to_ndb(items)

more_results = query.count(2)
# if query.count() is used without the number '1' the results are strange
# Stuck on this problem for 2-3 days but still couldn;'t figure out
# also need to ask someone about this

while more_results==2:
    cursor = query.cursor()
    query = query.with_cursor(cursor)
    more_results = query.count(2)
    if not (more_results==2):
        break
    results = query.fetch(2)
    copy_to_ndb(results)

class MainPage(webapp2.RequestHandler):
    def get(self):
        # template = jinja_env.get_template("index.html")
        # template_values = { 'all_queries': all_queries}
        # self.response.out.write(template.render(template_values))
        pass

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)