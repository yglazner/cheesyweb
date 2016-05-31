'''
Created on May 31, 2016

@author: yglazner
'''
from .widgets import Widget

class Layout(Widget):
    pass


class BoxLayout(Layout):
    '''
    classdocs
    '''


    def __init__(self, *widgets, vertical=True):
        '''
        Constructor
        '''
        self.vertical = vertical
        self.widgets = widgets
        
        
    def render(self):
        if self.vertical:
            return """<TABLE>
                        <TBODY>
                        %s
                        </TBODY>    
                      </TABLE>""" % ("\n".join("<tr><TD>%s</TD></tr>" % w.render() for 
                                               w in self.widgets))
        else:
            return """<TABLE>
                        <TBODY>
                        <TR>
                        %s
                        </TR>
                        </TBODY>    
                      </TABLE>""" % ("\n".join("<TD>%s</TD>" % w.render() for 
                                               w in self.widgets))
        
        