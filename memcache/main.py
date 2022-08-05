import os
import jinja2
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import memcache

class Laptop(ndb.Model):
    brand = ndb.StringProperty()
    gen = ndb.IntegerProperty()

jinja_env = jinja2.Environment(
                        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

lp = Laptop.get_or_insert('laptop1')
lp.brand = "hp"
lp.gen = 9
lp.put()

lp = Laptop.get_or_insert('laptop2')
lp.brand = "dell"
lp.gen = 6
lp.put()
def query_for_data(key):
    return Laptop.get_by_id(key)

def get_data(key):
    data = memcache.get(key)
    flag = True
    if data is not None:
        return data,flag
    else:
        flag = False
        data = query_for_data(key)
        memcache.add(key, data)
    return data,flag

class MainPage(webapp2.RequestHandler):
    def get(self):

        entity_list = []
        key = 'laptop2'
        # entity = memcache.get(key)
        # if entity is None:
        #     entity = Laptop.get_by_id(key)
        #     memcache.add(key, entity)

        (entity, flag) = get_data(key)
        if flag==True:
            print("data from memcache")
        else:
            print("data queried")
        entity_list.append(entity)

        template = jinja_env.get_template('index.html')
        template_values = { 'entity_list': entity_list }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)