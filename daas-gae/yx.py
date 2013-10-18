import webapp2
import jinja2
import os
import model
import util
import random
import logging

from google.appengine.ext import ndb

logging.getLogger().setLevel(logging.DEBUG)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainPage(webapp2.RequestHandler):

    def get(self):
        err = ''
        opt = self.request.get('opt')

        # insert
        if opt == 'insert':
            n = random.randrange(0,4)
            company = model.companys[n]
            ancestor = ndb.Key(model.Member, company)
            member = model.Member(parent=ancestor)
            member.first_name = util.RandomString(3)
            length = random.randrange(6, 10)
            member.last_name = util.RandomString(length)
            member.company= company
            member.number = random.randrange(1000)


            is_married = random.randrange(0,1)
            if is_married:
                member.is_married = True
            else:
                member.is_married = False

            length = random.randrange(6, 12)
            member.desc = util.RandomString(length)
            member.put()

        # delete
        elif opt == 'delete':
            id = int(self.request.get('id'))
            company = self.request.get('company')
            ancestor = ndb.Key(model.Member, company)
            member = model.Member.get_by_id(id, ancestor)
            if member:
                member.key.delete()
            else:
                err = 'entity not exists'

        company_name = self.request.get('company_name')
        if company_name:
            parent = ndb.Key(model.Member, company_name)
            members = model.Member.query(ancestor= parent)
        else:
            members = model.Member.query()
            logging.info(members)

        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {
            'members': members,
            'company_name' : company_name,
            'companys' :  model.companys,
            'err' : err
        }

        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage)
    ], debug=True)

