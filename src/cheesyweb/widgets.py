
class Widget(object):
    
    def render(self):
        raise Exception("No render method defined on %s"%type(self))

VIEW_TEMPLATE = '''
<HTML>
<HEAD>
<TITLE>{title}</TITLE>
</HEAD>
<BODY>
{content}
</BODY>

</HTML>
'''

class View(object):
    title = ""
    content = None
    
    def render(self):
        return VIEW_TEMPLATE.format(title=self.title,
                                    content=self.content.render())

class Label(object):
    
    def __init__(self, text=""):
        self.text = text
        
    def render(self):
        return "<p>%s</p>"% self.text