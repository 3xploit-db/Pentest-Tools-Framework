#!/usr/bin/python
import signal
import sys
import os
from ptf import main
import time
from core import exploit
from core import help
from core import scanner
from core import postex
from core import password
from core import exploitdb
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
def clean():
    os.system('clear')

#EXPLOITS
def exploits():
        ex = raw_input(""+N+"Pentest>> ("+B+"modules/exploits"+N+"): ")
        if ex == 'show options':
            help.options()
            exploits()
        elif ex =='show module':
             help.module_ex()
             exploits()
        elif ex == 'back':
             main()
        elif ex =='set exploit/tp_link_dos':
            exploit.tp_link_dos()
            exploits()
        elif ex =='set exploit/freer':
            exploit.freer()
            exploits()
        elif ex =='set exploit/davtest':
            exploit.davtest()
            exploits()
        elif ex =='set exploit/phpmailer_injection':
            exploit.phpmailer_injection()
            exploits()
        elif ex =='set exploit/web_delivery':
            exploit.web_delivery()
            exploits()
        elif ex  =='set exploit/php_thumb_shell_upload':
             exploit.php()
             exploits()
        elif ex =='set exploit/ldap_buffer_overflow':
            exploit.ldap()
            exploits()
        elif ex =='set exploit/robots':
             exploit.robots_txt()
             exploits()
        elif ex =='set exploit/jenkins_script_console':
            exploit.jenkins_script_console()
            exploits()
        elif ex =='set exploit/joomla_comfields_sqli_rce':
            exploit.joomla_comfields_sqli_rce()
            exploits()
        elif ex =='set exploit/webview_addjavascriptinterface':
            exploit.webview_addjavascriptinterface()
            exploits()
        elif ex == "set exploit/cpanel_bruteforce":
             exploit.cpanel()
             exploits()
        elif ex == "set exploit/abrt_privilege_escalation":
            exploit.abrt()
            exploits()
        elif ex =='set exploit/sonicwall':
            exploit.sonicwall()
            exploits()
        elif ex =='set exploit/cisco_dcnm_upload_2019':
            exploit.cisco()
            exploits()
        elif ex =='set exploit/zenworks_configuration':
            exploit.zenworks()
            exploits()
        elif ex == "set exploit/inject_javascript":
             exploit.java()
             exploits()
        elif ex =='set exploit/vbulletin_rce':
            exploit.vbul()
            exploits()
        elif ex == "set exploit/joomla_com_hdflayer":
             exploit.joomla()
             exploits()
        elif ex == "use exploit/wp_symposium_shell_upload":
             exploit.shell()
             exploits()
        elif ex == "set exploit/joomla0day_com_myngallery":
             exploit.jomday()
             exploits()
        elif ex == "set exploit/joomla_simple_shell":
             exploit.jomsi()
             exploits()
        elif ex =="set exploit/omnivista":
            exploit.omnivista()
            exploits()
        elif ex == "set exploit/joomla_com_foxcontact":
             exploit.jomfox()
             exploits()
        elif ex == "set exploit/jm_auto_change_pswd":
             exploit.jmauto()
             exploits()
        elif ex =='set exploit/eternalblue':
            exploit.eternalblue()
            exploits()
        elif ex =='set exploit/samsung_knox_smdm_url':
            exploit.knok()
            exploits()
        elif ex =='set exploit/cisco_ucs_rce':
            exploit.cisco_rce()
            exploits()
        elif ex =='set exploit/webmin_packageup_rce':
            exploit.webmin_packageup_rce()
            exploits()
        elif ex =='set exploit/awind_snmp_exec':
            exploit.awind_snmp_exec()
            exploits()
        elif ex =='set exploit/cmsms_showtime2_rce':
            exploit.cmsms_showtime2_rce()
            exploits()
        elif ex =='set exploit/bluekeep':
            exploit.bluekeep()
            exploits()
        elif ex == "set exploit/power_dos":
             exploit.dos()
             exploits()
        elif ex =='set exploit/apache':
            exploit.apache()
            exploit()
        elif ex == "set exploit/android_remote_access":
             exploit.android()
             exploits()
        elif ex == "set exploit/dns_bruteforce":
             exploit.dns_b()
             exploits()
        elif ex == "set exploit/dos_attack":
             exploit.hping3()
             exploits()
        elif ex == "set exploit/inject_html":
             exploit.html11()
             exploits()
        elif ex == "set exploit/shakescreen":
             exploit.shake()
             exploits()
        elif ex =="set exploit/auto_sql":
            exploit.auto_sql()
            exploits()
        elif ex == "set exploit/bypass_waf":
             exploit.waf()
             exploits()
        elif ex == "set exploit/enumeration":
             exploit.enum()
             exploits()
        elif ex =='set exploit/shellshock':
            exploit.shellshock()
            exploits()
        elif ex =="set exploit/restrict_anonymous":
             exploit.res()
             exploits()
        elif ex =='set exploit/vbulletin':
             exploit.vb()
             exploits()
        elif ex =='set exploit/openssl_heartbleed':
            exploit.ssl()
            exploits()
        elif ex =='set exploit/cms_rce':
            exploit.cms()
            exploits()
        elif ex =='set exploit/samba':
            exploit.smb()
            exploits()
        elif ex =='set exploit/smb':
            exploit.smb1()
            exploits()
        elif ex == 'clear':
             clean()
             exploits()
        elif ex =='exit':
             print
             print""+G+"Thanks for using PTF"
             print
             exit()
        else:
            print "Wrong Command => ", ex
            print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
            exploits()

##############
#SCANNERS
#############
def scan():
        sen = raw_input(""+N+"Pentest>> ("+B+"modules/scanners"+N+"): ")
        if sen == 'show options':
            help.options()
            scan()
        elif sen == 'show module':
              help.module_sec()
              scan()
        elif sen == 'back':
             main()
        elif sen == "set scanner/usr_pro_wordpress_auto_find":
             scanner.wordpress()
             scan()
        elif sen =="set scanner/subdo":
            scanner.subdos()
            scan()
        elif sen =='set scanner/enumiax':
            scanner.enumiax()
            scan()
        elif sen =='set scanner/dnsrecon':
            scanner.dnsrecon()
            scan()
        elif sen =='set scanner/dns_zone_transfer':
            scanner.dns_zone_transfer()
            scan()
        elif sen =='set scanner/dns_bruteforce':
            scanner.dns_bruteforce()
            scan()
        elif sen =='set scanner/zone_walking':
            scanner.zone_walking()
            scan()
        elif sen =='set scanner/sslscan':
            scanner.sslscan()
            scan()
        elif sen =='set scanner/ssl_cert':
            scanner.ssl_cert()
            scan()
        elif sen =='set scanner/check_ssl_certificate':
            scanner.ssl_check()
            scan()
        elif sen == "set scanner/cms_war":
             scanner.cms()
             scan()
        elif sen =='set scanner/load_balancing':
            scanner.load_balancing()
            scan()
        elif sen =='set scanner/admin_finder':
            scanner.finder()
            scan()
        elif sen == "set scanner/wordpress_user_scan":
             scanner.wordpress_scan()
             scan()
        elif sen =="set scanner/port_check":
            scanner.port_check()
            scan()
        elif sen == "set scanner/dir_search":
             scanner.dirse()
             scan()
        elif sen == "set scanner/lfi_scanners":
             scanner.lfi()
             scan()
        elif sen == "set scanner/port_scanners":
             scanner.port()
             scan()
        elif sen == "set scanner/joomla_sqli_scanners":
             scanner.joomla_sql()
             scan()
        elif sen == "set scanner/jomscan_v4":
             scanner.joomscan()
             scan()
        elif sen =='set scanner/botnet_scanning':
            scanner.botnet_scanning()
            scan()
        elif sen == "set scanner/joomla_scanners_v3":
             scanner.scan_v3()
             scan()
        elif sen =='set scanner/drupal_scan':
            scanner.drupal_scan()
            scan()
        elif sen =='set scanner/grabbing_detection':
            scanner.grabbing_detection()
            scan()
        elif sen =='set scanner/discovery':
            scanner.discovery()
            scan()
        elif sen =='set scanner/http_services':
            scanner.http_services()
            scan()
        elif sen =='set scanner/web_services':
            scanner.web_services()
            scan()
        elif sen =='set scanner/http_enum':
            scanner.http_enum()
            scan()
        elif sen =='set scanner/ddos_reflectors':
            scanner.ddos_reflectors()
            scan()
        elif sen =='set scanner/wordpress_scan':
            scanner.wordpress1()
            scan()
        elif sen =='set scanner/webdav_scan':
            scanner.webdav()
            scan()
        elif sen =='set scanner/mysql_empty_password':
            scanner.mysql()
            scan()
        elif sen == "set scanner/joomla_scanners_v.2":
             scanner.scan_v2()
             scan()
        elif sen == "set scanner/joomla_vulnerability_scanners":
             scanner.jomvull()
             scan()
        elif sen == "set scanner/jdownloads_scanners":
             scanner.jdown()
             scan()
        elif sen =='set scanner/firewalk':
            scanner.firewalk()
            scan()
        elif sen == "set scanner/header":
            scanner.header()
            scan()
        elif sen == "set scanner/nmap_scanner":
             scanner.nmap_sc()
             scan()
        elif sen == "set scanner/nmap_vuln":
             scanner.nmap_vul()
             scan()
        elif sen == "set scanner/xss_scaner":
             scanner.xss()
             scan()
        elif sen == "set scanner/spaghetti":
             scanner.spaghetti()
             scan()
        elif sen == "set scanner/ssl_scanning":
             scanner.ssl()
             scan()
        elif sen =="set scanner/smb_scanning":
             scanner.smb()
             scan()
        elif sen =='set scanner/dns_bruteforce':
            scanner.dbrute()
            scan()
        elif sen == 'set scanner/dnslookup':
             scanner.dnslok()
             scan()
        elif sen =='set scanner/dmitry':
            scanner.dmitry()
            scan()
        elif sen =='set scanner/golismero':
            scanner.golismero()
            scan()
        elif sen == 'set scanner/domain_map':
             scanner.domain_map()
             scan()
        elif sen == 'set scanner/dns_report':
             scanner.dns_report()
             scan()
        elif sen == 'set scanner/find_shared_dns':
             scanner.find_shared_dns()
             scan()
        elif sen =='set scanner/reverse_dns':
            scanner.dns_reverse()
            scan()
        elif sen == 'set scanner/dns_propagation':
             scanner.dns_propagation()
             scan()
        elif sen == 'set scanner/find_records':
             scanner.find_records()
             scan()
        elif sen == 'set scanner/cloud_flare':
             scanner.cloud_flare()
             scan()
        elif sen =='set scanner/ip_locator':
            scanner.iploc()
            scan()
        elif sen =='set scanner/whois':
            scanner.who()
            scan()
        elif sen == 'set scanner/extract_links':
             scanner.extract_links()
             scan()
        elif sen == 'set scanner/web_robot':
             scanner.web_robot()
             scan()
        elif sen =='set scanner/wordpress_user_dislosure':
            scanner.disclosure()
            scan()
        elif sen == 'set scanner/bluekeep':
            scanner.bluekeep()
            scan()
        elif sen =='set scanner/eternalblue':
            scanner.eternalblue()
            scan()
        elif sen =='set scanner/enumeration':
            scanner.num()
            scan()
        elif sen =='set scanner/heartbleed':
            scanner.heartbleed()
            scan()
        elif sen =='set scanner/https_discover':
            scanner.https_discover()
            scan()
        elif sen =='set scanner/dir_bruteforce':
            scanner.finderdir()
            scan()
        elif sen == 'clear':
            clean()
            scan()
        elif sen =='exit':
             print
             print""+G+"Thanks for using PTF"
             print
             exit()
        else:
            print "Wrong Command => ", sen
            print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
            scan()
def post():
    while True:
        pos = raw_input(""+N+"Pentest>> ("+B+"modules/post"+N+"): ")
        if pos =='show options':
            help.options()
            post()
        elif pos == 'show module':
              help.post()
              post()
        elif pos == 'back':
             main()
        elif pos == "set post/wordpress_user_scan":
             postex.wordpress_scan()
             post()
        elif pos == "set post/dir_search":
             postex.dirse()
             post()
        elif pos == "set post/cms_war":
             postex.cms()
             post()
        elif pos == "set post/usr_pro_wordpress_auto_find":
             postex.wordpress()
             post()
        elif pos =='set aix_hashdump':
            postex.aix_hashdump()
            post()
        elif pos == "set post/android_remote_access":
             postex.android()
             post()
        elif pos =='set post/vbulletin':
             postex.vb()
             post()
        elif pos =='set post/enumeration':
            postex.num()
            post()
        elif pos =='set post/samba':
            postex.smb()
            post()
        elif pos == 'clear':
            clean()
            post()
        elif pos =='exit':
             print
             print""+G+"Thanks for using PTF"
             print
             exit()
        else:
            print "Wrong Command => ", pos
            print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
            post()
        pass

def pas1():
    pas = raw_input(""+N+"Pentest>> ("+B+"modules/password"+N+"): ")
    if pas =='show options':
        help.options()
        pas1()
    elif pas == 'show module':
         help.pas()
         pas1()
    elif pas =='set password/base64_decode':
         password.base64()
         pas1()
    elif pas =='set password/sha1_decrypt':
        password.sha1()
        pas1()
    elif pas =='set password/sha384_decrypt':
        password.sha384()
        pas1()
    elif pas =='set password/sha512_decrypt':
        password.sha512()
        pas1()
    elif pas =='set password/sha256_decrypt':
        password.sha256()
        pas1()
    elif pas =='set password/md5_decrypt':
         password.md5()
         pas1()
    elif pas =='set password/ssh_bruteforce':
        password.ssh_bruteforce()
        pas1()
    elif pas == 'clear':
        clean()
        pas1()
    elif pas =='exit':
         print
         print""+G+"Thanks for using PTF"
         print
         exit()

    elif pas == 'back':
         main()
    else:
        print "Wrong Command => ", pas
        print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
        pas1()

def exploit_db():
    db = raw_input(""+N+"Pentest>> ("+B+"modules/exploitdb"+N+"): ")
    if db =='show options':
        help.optionsdb()
        exploit_db()
    elif db =='set exploitdb/exploits':
        exploitdb.explo()
        exploit_db()
    elif db =='set exploitdb/shellcode':
        exploitdb.shel()
        exploit_db()
    elif db =='searchsploit':
        exploitdb.searchsploit()
        exploit_db()
    elif db == 'show module':
         help.db()
         exploit_db()
    elif db =='exit':
         print
         print""+G+"Thanks for using PTF"
         print
         exit()
    elif db == 'clear':
        clean()
        exploit_db()
    elif db == 'back':
         main()
    else:
        print "Wrong Command => ", db
        print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
        exploit_db()


def listener():
    while True:
        map =raw_input(""+N+"Pentest>> ("+B+"modules/listener"+N+"): ")
        if map == 'show options':
            help.list()
            listener()
        elif map =='show module':
            help.mod()
            listener()
        elif map =='exit':
             print
             print""+G+"Thanks for using PTF"
             print
             exit()
        elif map == 'back':
            main()
        elif map =='clear':
            clean()
            listener()
        elif map =='set android_meterpreter_reverse_tcp':
            exploit.android_meterpreter_reverse_tcp()
            listener()
        elif map =='set java_jsp_shell_reverse_tcp':
            exploit.java_jsp_shell_reverse_tcp()
            listener()
        elif map =='set linux_x64_meterpreter_reverse_https':
            exploit.linux_x64_meterpreter_reverse_https()
            listener()
        elif map =='set linux_x64_meterpreter_reverse_tcp':
            exploit.linux_x64_meterpreter_reverse_tcp()
            listener()
        elif map =='set linux_x64_shell_reverse_tcp':
            exploit.linux_x64_shell_reverse_tcp()
            listener()
        elif map =='set osx_x64_meterpreter_reverse_https':
            exploit.osx_x64_meterpreter_reverse_https()
            listener()
        elif map =='set osx_x64_meterpreter_reverse_tcp':
            exploit.osx_x64_meterpreter_reverse_tcp()
            listener()
        elif map =='set php_meterpreter_reverse_tcp':
            exploit.php_meterpreter_reverse_tcp()
            listener()
        elif map =='set python_meterpreter_reverse_https':
            exploit.python_meterpreter_reverse_https()
            listener()
        elif map =='set python_meterpreter_reverse_tcp':
            exploit.python_meterpreter_reverse_tcp()
            listener()
        elif map =='set windows_x64_meterpreter_reverse_https':
            exploit.windows_x64_meterpreter_reverse_https()
            listener()
        elif map =='set windows_x64_meterpreter_reverse_tcp':
            exploit.windows_x64_meterpreter_reverse_tcp()
            listener()
        elif map =='set cmd_windows_reverse_powershell':
            exploit.cmd_windows_reverse_powershell()
            listener()
        elif map =='set android_meterpreter_reverse_https':
            exploit.android_meterpreter_reverse_https()
            listener()

        else:
            print "Wrong Command => ", map
            print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
            listener()
def tools():
    map =raw_input(""+N+"Pentest>> ("+B+"modules/tools)"+N+"): ")
    if map == 'show options':
        help.tool1()
        tools()
    elif map =='show module':
        help.module_tool()
        tools()
    elif map =='example':
        print("""
             +----------------------------------------------------------+
             | how to use arguments setup (--help)                      |
             | example: Pentest>> (modules/tools)(xsstrike)): -u target |
             +----------------------------------------------------------+
         """)
        tools()
    elif map =='exit':
         print
         print""+G+"Thanks for using PTF"
         print
         exit()
    elif map =='set atscan':
        exploit.atscan()
        tools()
    elif map =='set wifigod':
        exploit.wifigod()
        tools()
    elif map =='set sublist3r':
        exploit.sublist3r()
        tools()
    elif map =='set sn1per':
        exploit.snip3r()
        tools()
    elif map =='set xsstrike':
        exploit.xsstrike()
        tools()
    elif map =='set socialbox':
        exploit.socialbox()
        tools()
    elif map =='set searchsploit':
        exploit.searchsploit()
        tools()
    elif map =='set xsser':
        exploit.xsser()
        tools()
    elif map == 'back':
        main()
    elif map =='clear':
        clean()
        tools()
    else:
        print "Wrong Command => ", map
        print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
        tools()
