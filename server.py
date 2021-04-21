import codecs
import os
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
from DBOperations import *
#cgi:common gateway interface :
#HTTPServer : dinlenecek port numarası
#BaseHTTPRequestHandler : Requestleri yönetmek için

tasklist = ['Task 1','Task 2','Task 3']



def load_binary(file):
    with open(file, 'rb') as file:
        return file.read()

def add_tags(tag,word):
    return "<%s>%s</%s>" % (tag,word,tag)





class requestHandler(BaseHTTPRequestHandler): #BaseHTTPRequestHandler sınıfından kalıtım ile alınıyor.
    def do_GET(self):
        print(self.path)
        #encode edilecek dosya tipleri : application/javascript,text/css,text/html (utf-8)
        try:
            filepath =  self.path[1:] #request ile gelen dosya yolu.başında '/' işareti ile geldiği için / değerini almıyorum.
            mimetype, _ = mimetypes.guess_type(filepath)
            if (mimetype == 'text/html' or mimetype == 'text/css' or mimetype == 'application/javascript'): #metin içerikliler encode edilerek gönderilmeli
                file = codecs.open(filepath, "r", "utf-8")
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(file.read().encode())
                print('MIMETYPE:{}'.format(mimetype))
            else: #metin içerikli olmayanlar(binary) encode edilmeden gönderilmeli.
                file = load_binary(filepath)
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(file)
                print('MIMETYPE:{}'.format(mimetype))

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
                control = loginControl(fields)
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/bootstrap-shop/loginhandle.html')
            self.end_headers()
        if self.path == '/user/register': #Kayıt işlemleri
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            dataControl = () #registerControl fonksiyonundan dönen değeri karşılayacak.->(True|False,Message)
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                dataControl = registerControl(fields)
            if dataControl[0]: #Kayıt başarılı : True
                with open('bootstrap-shop/loginhandle.html','r') as file:
                    data = file.readlines() #bütün satırları data değişkenine atıyorum. data-->list
                self.send_response(301)
                self.send_header('content-type','text/html')
                self.end_headers()
                #data[178] = '<h3>{}</h3>'.format(dataControl[1])
                data[178] = add_tags('h3',dataControl[1])
                eachInASeparateLine = "\n".join(data)
                self.wfile.write(eachInASeparateLine.encode())

            else: #Kayıt başarısız. : False
                with open('bootstrap-shop/loginhandle.html','r') as file:
                    data = file.readlines() #bütün satırları data değişkenine atıyorum. data-->list
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                #self.send_header('Location','/signup-failed')
                self.end_headers()
                data[178] = '<h3>{}</h3>'.format(dataControl[1]) #sayfaya fonksiyondan dönen başarılı başarısız mesajı yazıyorum.
                eachInASeparateLine = "\n".join(data)
                self.wfile.write(eachInASeparateLine.encode())



def main():
    PORT = 8000
    server = HTTPServer(('',PORT),requestHandler)
    print('Server running on port {0}'.format(PORT))
    mimetype, _ = mimetypes.guess_type('/freshshop/index.html')
    print(mimetype)
    server.serve_forever() # Program durdurulana kadar çalış


if __name__ == '__main__':
    main()





