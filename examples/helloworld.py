'''
Created on May 31, 2016

@author: yglazner
'''
from cheesyweb import *

class HelloWorld(View):
    title = "Hello World"
    url = "/HelloWorld"
    content = Label("Yo Dude!")

def main():
    app = App()
    app.add(HelloWorld())
    
    app.start(port=9000, reloader=True)
    
if __name__ == '__main__':
    main()