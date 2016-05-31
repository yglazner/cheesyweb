'''
Created on May 31, 2016

@author: yglazner
'''
import bottle

class App(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.app = bottle.Bottle()
        self.views = []
        self.base = '/'
        self.running = False
        
    def start(self, host='127.0.0.1', port=80, debug=False, reloader=True):
        self.running = True
        self.app.run(host=host, port=port, debug=debug, reloader=reloader)
        
        
    def stop(self):
        self.app.close()
        self.running = False
        
        
    def get_url(self, view):
        if view.url.startswith('/'):
            return view.url
        return self.base + self.view.url
    
    
    def add(self, view):        
        self.views.append(view)
        self.app.get(self.get_url(view))(view.render)
        
        