import codecs
import os
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
#cgi:common gateway interface :
#HTTPServer : dinlenecek port numarası
#BaseHTTPRequestHandler : Requestleri yönetmek için

tasklist = ['Task 1','Task 2','Task 3']

class requestHandler(BaseHTTPRequestHandler): #BaseHTTPRequestHandler sınıfından kalıtım ile alınıyor.
    def do_GET(self):
        print(self.path)

        try:
            filepath =  self.path[1:] #request ile gelen dosya yolu.başında '/' işareti ile geldiği için / değerini almıyorum.
            file = codecs.open(filepath, "r", "utf-8")
        except IOError:
            self.send_error(404, 'File Not Found: %s ' % filepath)
            return
        self.send_response(200)
        output = file.read()
        mimetype, _ = mimetypes.guess_type(filepath)
        self.send_header('Content-type', mimetype)
        self.end_headers()
        self.wfile.write(output.encode())



def main():
    PORT = 8000
    server = HTTPServer(('',PORT),requestHandler)
    print('Server running on port {0}'.format(PORT))
    mimetype, _ = mimetypes.guess_type('/freshshop/index.html')
    print(mimetype)
    server.serve_forever() # Program durdurulana kadar çalış


if __name__ == '__main__':
    main()





