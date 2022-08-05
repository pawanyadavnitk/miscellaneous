import os
import jinja2
import webapp2

from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
                    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
                    autoescape = True)

class Laptop(ndb.Model):
    brand = ndb.StringProperty()
    gen = ndb.IntegerProperty()

Laptop(brand="hp", gen=1).put()
Laptop(brand="dell", gen=2).put()
Laptop(brand="asus", gen=6).put()
Laptop(brand="hp", gen=7).put()
Laptop(brand="lenovo", gen=3).put()
Laptop(brand="hp", gen=8).put()
Laptop(brand="asus", gen=1).put()
Laptop(brand="samsung", gen=9).put()
Laptop(brand="hp", gen=5).put()
Laptop(brand="dell", gen=6).put()
Laptop(brand="lenovo", gen=5).put()
Laptop(brand="acer", gen=4).put()
Laptop(brand="dell", gen=2).put()
Laptop(brand="asus", gen=6).put()


class MainPage(webapp2.RequestHandler):
    def get(self):
        query = Laptop.query()
        #self.response.out.write(query)
        items = query.fetch(10)
        template = jinja_env.get_template("index.html")
        template_values = { 'items': items }

        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
