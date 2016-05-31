'''
Created on May 31, 2016

@author: yglazner
'''
from cheesyweb import *

def f(b):
    print("was clicked! %s" % b)
    return {"yay!!!"}

class HelloWorld(View):
    title = "Hello World"
    url = "/HelloWorld"
    content = BoxLayout(
                        Label("Yo Dude!"),
                        Button("Click Me", onclick=f),
                        Table(headers=["User", "Money"],
                              rows=[['user%s' % i, i*i] for i in range(1, 100)]),
                        
                        vertical=True
                        )

def main():
    app = App()
    app.add(HelloWorld())
    
    app.start(port=9000, reloader=True)
    
if __name__ == '__main__':
    main()