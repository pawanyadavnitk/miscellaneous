import webapp2

from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import taskqueue

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

class MainPage(webapp2.RequestHandler):
    def get(self):
        brand_list = ['hp', 'dell', 'apple', 'acer', 'asus', 'hp', 'acer', 'hp', 'lenovo', 'apple']
        gen_list = [1, 3, 5, 3, 6, 8, 9, 5, 8, 8]
        key_list = []

        for i in range(10):
            key_list.append('laptop'+str(i+1))

        create_db_database(brand_list, gen_list, key_list)              

        self.response.write("""
            <form method="post" action="/taskq">
                
                <button>Enqueue Task</button>
            </form>
        """)

class EnqueueTaskHandler(webapp2.RequestHandler):
    def post(self):
        query = dbLaptop.gql('')
        items = query.fetch(2)
        copy_to_ndb(items)

        cursor = query.cursor()
        query = query.with_cursor(cursor) 
        
        task = taskqueue.add(
            url='/process_queries',
            target='worker',
            params={'query': query})

        self.response.write(
            'Task {} enqueued, ETA {}.'.format(task.name, task.eta))

app = webapp2.WSGIApplication([('/', MainPage),
                        ('/taskq', EnqueueTaskHandler)], debug = True)