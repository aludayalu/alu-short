from joshua.app import App
from joshua.request import Request
from joshua.request import Request
from joshua.response import HttpResponse
from joshua.router import Path
from wsgiref.simple_server import make_server
from aludbms import query,makedb
import os
try:
    open("dirs.aludb")
except:
    makedb.fresh("redirs")
port = 8080
base="<meta http-equiv=\"Refresh\" content=\"0; url="
base2="\" />"
app = App()

def uwu(request: Request):
    cpath=request.path[1:]
    return HttpResponse(request, (base+query.get("redirs", cpath)+base2))
listrs=os.listdir("redirs")
routes = []
for x in listrs:
    estroute='/'+x
    routes.append(Path(estroute,uwu))
app.set_routes(routes)
serverh = make_server("127.0.0.1", port, app)
print('Server Listening On Port ',port)
print('Printing Log')
serverh.serve_forever()
input("Press enter to proceed...")