'''
Created on May 31, 2016

@author: yglazner
'''
import unittest
import threading
from cheesyweb import *
import logging
import time
import requests
_app = None
log = logging.getLogger("Logger")
def stop_threaded():
    if not _app: return
    if _app.running:
        _app.stop()

def _run(app):
    global _app
    _app = app
    log.info("Starting %s"%app)
    app.start(port=8085)

def run_threaded(app):
    threading.Thread(target=_run, args=(app,)).start()


class Test(unittest.TestCase):


    def setUp(self):
        stop_threaded() #just in case
        self.app = App()
        self._setup_views()
        run_threaded(self.app)
        time.sleep(0.2)
        
    def _setup_views(self):
        
        class HelloWorld(View):
            title = "hello world"
            url = "hello/"
            content = Label("Hello world!!!11")
            
        self.app.add(HelloWorld())
                    
    def tearDown(self):
        stop_threaded()


    def testName(self):
        r = (requests.get('http://localhost:8085/hello/'))

        self.assertEqual(r.status_code, 200)
        r.content


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    logging.basicConfig(level=logging.DEBUG)
    unittest.main(argv=['', '-v'])