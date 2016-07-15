"""
localurat vindousis hosts failis cvlis
"""
import os
import sys
import win32com.shell.shell as shell

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

with open("C:\Windows\System32\drivers\etc\hosts", "w") as out:
    print >> out, "91.208.144.29	facebooks.com.206799586135980.-2207520000.144047296114404729611440472961144047296114404729611440472961"