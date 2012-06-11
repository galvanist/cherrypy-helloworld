import cherrypy
import os

#workaround of cherrypy loopback check for heroku
#http://stackoverflow.com/a/9271296
def fake_wait_for_occupied_port(host, port): return
cherrypy.process.servers.wait_for_occupied_port = fake_wait_for_occupied_port

class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True
    
    def hello(self,world='World'): #e.g. /hello/heroku/
        return "Hello "+world
    hello.exposed = True

cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': int(os.environ.get('PORT', '5000')),
})

cherrypy.quickstart(HelloWorld())