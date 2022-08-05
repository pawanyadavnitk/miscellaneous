from google.appengine.ext import ndb
import webapp2

class ndbLaptop(ndb.Model):
    brand = ndb.StringProperty()
    gen = ndb.IntegerProperty()

class ProcessHandler(webapp2.RequestHandler):
    def post(self):
        query = self.request.get('query')
                
        more_results = query.count(2)

        while more_results==2:
            cursor = query.cursor()
            query = query.with_cursor(cursor)
            more_results = query.count(2)
            print(more_results)
            if not more_results==2:
                break
            results = query.fetch(2)
            main.copy_to_ndb(results)

app = webapp2.WSGIApplication([('/process_queries', ProcessHandler)], debug = True)