import os
import jinja2
import webapp2

from google.appengine.ext import db
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
                    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
                    autoescape = True)

# class Laptop(db.Model):
#     brand = db.StringProperty()
#     gen = db.IntegerProperty()

# Laptop(brand="hp", gen=1, id="laptop1").put()
# Laptop(brand="dell", gen=2, id="laptop2").put()
# Laptop(brand="asus", gen=6).put()
# Laptop(brand="hp", gen=7).put()
# Laptop(brand="lenovo", gen=3).put()
# Laptop(brand="hp", gen=8).put()
# Laptop(brand="asus", gen=1).put()
# Laptop(brand="samsung", gen=9).put()
# Laptop(brand="hp", gen=5).put()
# Laptop(brand="dell", gen=6).put()
# Laptop(brand="lenovo", gen=5).put()
# Laptop(brand="acer", gen=4).put()
# Laptop(brand="dell", gen=2).put()
# Laptop(brand="asus", gen=6, id="laptop14").put()

class dbLaptop(db.Model):
    brand = db.StringProperty()
    gen = db.IntegerProperty()

brand_list = ['hp', 'dell', 'apple', 'acer', 'asus', 'hp', 'acer', 'hp', 'lenovo', 'apple']
gen_list = [1, 3, 5, 3, 6, 8, 9, 5, 8, 8]
key_list = []

for i in range(10):
    key_list.append('laptop'+str(i+1))

for i in range(10):
    db_l = dbLaptop.get_or_insert(key_list[i])
    db_l.brand = brand_list[i]
    db_l.gen = gen_list[i]
    db_l.put()

class ndbLaptop(ndb.Model):
    brand = ndb.StringProperty()
    gen = ndb.IntegerProperty()

for i in range(10):
    db_l = dbLaptop.get_by_key_name(key_list[i])
    ndb_l = ndbLaptop.get_or_insert(key_list[i])
    ndb_l.brand = db_l.brand
    ndb_l.gen = db_l.gen
    ndb_l.put()

class MainPage(webapp2.RequestHandler):
    def get(self):
        # query = Laptop.all()
        # items = query.fetch(10)
        query = ndbLaptop.query()
        items = query.fetch(10)
        template = jinja_env.get_template("index.html")
        template_values = { 'items': items}

        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
