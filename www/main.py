#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp.util import run_wsgi_app


    
class MainHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write('<form action="login" method="post"><p><input value="user" id="user" name="user" type="text" /></p><p><input value="pass" id="pass" name="pass" type="password" /></p><p><input type="submit" /></p></form>')
		self.response.out.write("test")
	
class LoginHandler(webapp.RequestHandler):
	def post(self):
		self.response.out.write(self.request.get("user"))


def main():
  application = webapp.WSGIApplication([('/', MainHandler),
  										('/login', LoginHandler),
  										('/display', DisplayHandler)],
                                       debug=True)
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
