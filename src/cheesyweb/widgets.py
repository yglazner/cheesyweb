from . import events

class Widget(object):
    
    def render(self):
        raise Exception("No render method defined on %s"%type(self))

VIEW_TEMPLATE = '''
<HTML>
<HEAD>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<TITLE>{title}</TITLE>
</HEAD>
<BODY>
{content}
</BODY>
</HTML>
'''

class View(Widget):
    title = ""
    content = None
    
    def render(self):
        return VIEW_TEMPLATE.format(title=self.title,
                                    content=self.content.render())

class Label(Widget):
    
    def __init__(self, text=""):
        self.text = text
        
    def render(self):
        return "<p>%s</p>"% self.text
    
class Button(Widget):
    def __init__(self, text, onclick=lambda b:None):
        self.text = text
        #self.onclick = onclick
        events.bind(self, onclick)

        
    def render(self):
        return """<button type='button' onclick='$.post("/events/%s", {})'>
                   %s
                  </button>
                """ % (str(id(self)), self.text, )

class Table(Widget):
    def __init__(self, headers, rows):
        self.headers = headers
        self.rows = rows
    
    def render(self):
        return """ <TABLE>
                    <THEAD>
                     <TR>
                     %s
                     </TR>
                    </THEAD>
                    <TBODY> 
                     %s
                    </TBODY> 
                   </TABLE>
               """ % (" ".join("<TH>%s</TH>" % s for s in self.headers),
                      "\n".join("<TR>%s</TR>" % " ".join("<TD>%s</TD>" % f for f in r) 
                                for r in self.rows
                                )
                      )
        