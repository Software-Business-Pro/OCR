import tornado.httpserver
import tornado.ioloop
import tornado.web
import pprint
from PIL import Image
from pytesseract import image_to_string
import StringIO
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><form enctype="multipart/form-data" action="/" method="post">'
                   '<input type="file" name="the_file">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
 
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("Nom du fichier :" + self.request.files.items()[0][1][0]['filename'] )
    	self.write(image_to_string(Image.open(StringIO.StringIO(self.request.files.items()[0][1][0]['body']))))
 
application = tornado.web.Application([
    (r"/", MainHandler),
])
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()