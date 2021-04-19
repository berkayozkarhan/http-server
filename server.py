import codecs
import os
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
#cgi:common gateway interface :
#HTTPServer : dinlenecek port numarası
#BaseHTTPRequestHandler : Requestleri yönetmek için

tasklist = ['Task 1','Task 2','Task 3']



def load_binary(file):
    with open(file, 'rb') as file:
        return file.read()


class requestHandler(BaseHTTPRequestHandler): #BaseHTTPRequestHandler sınıfından kalıtım ile alınıyor.
    def do_GET(self):
        print(self.path)

        try:
            filepath =  self.path[1:] #request ile gelen dosya yolu.başında '/' işareti ile geldiği için / değerini almıyorum.
            mimetype, _ = mimetypes.guess_type(filepath)
            if mimetype == 'image/png' or mimetype == 'image/jpeg':
                file = load_binary(filepath)
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(file)
            else:
                file = codecs.open(filepath, "r", "utf-8")
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(file.read().encode())
        except IOError:
            self.send_error(404, 'File Not Found: %s ' % filepath)
            return

    def do_POST(self):
        print("POST:{}".format(self.path))
        if self.path == '/user/login':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                eMail = fields.get('inputEmail')
                password = fields.get('inputPassword')
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/bootstrap-shop/loginhandle.html')
            self.end_headers()


def main():
    PORT = 8000
    server = HTTPServer(('',PORT),requestHandler)
    print('Server running on port {0}'.format(PORT))
    mimetype, _ = mimetypes.guess_type('/freshshop/index.html')
    print(mimetype)
    server.serve_forever() # Program durdurulana kadar çalış


if __name__ == '__main__':
    main()





