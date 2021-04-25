import codecs
import os
import mimetypes
import posixpath
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
from DBOperations import *
import random
import datetime,time
from http import cookies
#cgi:common gateway interface :
#HTTPServer : dinlenecek port numarası
#BaseHTTPRequestHandler : Requestleri yönetmek için

tasklist = ['Task 1','Task 2','Task 3']



def load_binary(file):
    with open(file, 'rb') as file:
        return file.read()

def add_tags(tag,word):
    return "<%s>%s</%s>" % (tag,word,tag)


authorizedKeys = {}


class requestHandler(BaseHTTPRequestHandler): #BaseHTTPRequestHandler sınıfından kalıtım ile alınıyor.
    def do_GET(self):
        print(self.path)
        print('TEST--------------------------')
        cookie = self.headers.get('Cookie') #.items olursa 6. index.
        if cookie:
            print('cookie:{},user:{}'.format(cookie,authorizedKeys[cookie]))
        print('TEST--------------------------')
        #encode edilecek dosya tipleri : application/javascript,text/css,text/html (utf-8)
        if not (self.path.startswith('/bootstrap-shop')): #gönderilecek bütün dosyalar bu dizin içerisinde
            self.path = "/bootstrap-shop" + self.path
        if self.path == '/bootstrap-shop/registersuccess':
            self.path = '/bootstrap-shop/registersuccess.html'
            #self.do_GET()
        if self.path == '/bootstrap-shop/registerfailed':
            self.path = '/bootstrap-shop/registerfailed.html'
            #self.do_GET()
        if self.path == '/bootstrap-shop/loginsuccess': #Giriş başarılı olmuşsa cookie değerini kontrol ediyorum.
            cookie = self.headers.get('Cookie')  # .items olursa 6. index.
            if cookie: #Test
                print('cookie:{}'.format(cookie))
                self.path = '/bootstrap-shop/loginsuccess.html'
                self.do_GET()
            else:
                self.send_error(401,'You are not authorized to login to this page.')
            #self.do_GET()
        if self.path == '/bootstrap-shop/loginfailed':
            self.path = '/bootstrap-shop/loginfailed.html'
            #self.do_GET()

        filepath = self.path[1:]
        try:
            #request ile gelen dosya yolu.başında '/' işareti ile geldiği için / değerini almıyorum.
            mimetype, _ = mimetypes.guess_type(filepath)
            if (mimetype == 'text/html' or mimetype == 'text/css' or mimetype == 'application/javascript'): #metin içerikliler encode edilerek gönderilmeli
                try:
                    file = codecs.open(filepath, "r", "utf-8")
                except:
                    print("Error while opening file.")
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
        if self.path == '/user/login': #Giriş işleri
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                control = loginControl(fields)
            if control: #Giriş başarılı
                self.send_response(301)
                c = cookies.SimpleCookie()
                random_id = random.randint(0, 1000000000) + int(time.time())
                authorizedKeys[random_id] = {fields.get('inputEmail')[0]}
                c["unique_id"] = random_id  # tell the browser to store a cookie
                c["unique_id"]["path"] = "/bootstrap-shop"
                c["has_visited_before"] = "yes"  # tell the browser to store a cookie
                # set a cookie with a custom expiration date.. this cookie will self-destruct in year
                expiration = datetime.datetime.now() + datetime.timedelta(days=365)
                c["semi-permanent-cookie"] = "here it is"
                c["semi-permanent-cookie"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S EST")
                test = c.output()
                self.send_header('Cookie',c)
                self.send_header('content-type', 'text/html')
                self.send_header('Location', '/bootstrap-shop/loginsuccess')
                self.end_headers()
            else:
                self.send_response(301)
                self.send_header('content-type','text/html')
                self.send_header('Location','/bootstrap-shop/loginfailed')
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
                self.send_response(301)
                self.send_header('content-type', 'text/html')
                self.send_header('Location', '/bootstrap-shop/registersuccess')
                self.end_headers()
            else: #Kayıt başarısız. : False
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location','/bootstrap-shop/registerfailed')
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





