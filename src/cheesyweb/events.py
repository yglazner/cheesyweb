import logging


EVENTS_MAP = {}


log = logging.getLogger("cheesyweb.events")


def bind(widget, callback):
    EVENTS_MAP[id(widget)] = (widget, callback)
    


def dispatch_event(id):  # @ReservedAssignment
    id = int(id)  # @ReservedAssignment
    
    if id not in EVENTS_MAP:
        log.warn("unwanted event for % str_id")
    
    #dispatch
    w, callback = EVENTS_MAP[id]
    return callback(w)