#!/usr/bin/python

R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End


def help():
    print( """
            -------------------------------------------------------------------------------------
            |                                  Global Option                                    |
            -------------------------------------------------------------------------------------
            |  \033[31mCommand                                      Description \033[1;37m                        |
            |-----------------------------------------------------------------------------------|
            | show modules                    |  Look this modules                              |
            | show options                    |  Show Current Options Of Selected Module        |
            | ipconfig                        |  Network Informasion                            |
            | shell                           |  Execution Command Shell >[ctrl+C exit shell ]  |
            | use                             |  Select Tipe Module For Use                     |
            | set                             |  Select Modules For Use                         |
            | run                             |  Excute modules                                 |
            | update                          |  Update Pentest Framework                       |
            | banner                          |  PTF Banner                                     |
            | about                           |  Informasion Tools                              |
            | credits                         |  Credits && Thanks                              |
            | clear                           |  Clean Pentest input/output                     |
            | exit                            |  Exit the progam                                |
            -------------------------------------------------------------------------------------
  """)
def modules():
    print ("""

            +-----------------------------------------------------------------------------------+
            |                                  Modules                                          |
            -------------------------------------------------------------------------------------
            |  \033[31mCommand                                      Description \033[1;37m                        |
            |-----------------------------------------------------------------------------------|
            | modules/exploits                    |     exploits vulnerability                  |
            | modules/exploitdb                   |     vulnerability Informasion(exploit-db)   |
            | modules/listener                    |     listener with metasploit                |
            | modules/password                    |     password decode                         |
            | modules/post                        |     exploits/scaning                        |
            | modules/scanners                    |     scanners vulnerability                  |
            | modules/tools                       |     hacking  Tools                          |
            -------------------------------------------------------------------------------------
""")

def option():
    print ("""
            +---------------------------------------------------------+
            |                         Options                         |
            -----------------------------------------------------------
            |  \033[31mCommand                     Description \033[1;37m               |
            |---------------------------------------------------------|
            |  set target                | Set Target                 |
            |  run                       | Start Attacks              |
            |  clear                     | Clean Pentest input/output |
            |  back                      | Back To menu               |
            |  exit                      | Exit the progam            |
            -----------------------------------------------------------
""")
def options():
    print ("""
            +---------------------------------------------------------+
            |                         Options                         |
            -----------------------------------------------------------
            |  \033[31mCommand                     Description\033[1;37m                |
            |---------------------------------------------------------|
            | show module                |  show modules              |
            | set                        |  Select module             |
            | back                       |  back to menu              |
            -----------------------------------------------------------
    """)
def module_ex():
    print ("""
            +-----------------------------------------------------------------------------------------------------------------------------------+
            | EXPLOITS                                                                                                                          |
            -------------------------------------------------------------------------------------------------------------------------------------
            |     \033[31mCOMMANDS                                 Rank                                   Description   \033[1;37m                                |
            -------------------------------------------------------------------------------------------------------------------------------------
            | exploit/freer                            | normal    |   Virtual Freer 1.58 - Remote Command Execution                            |
            | exploit/omnivista                        | normal    |   Alcatel-Lucent Omnivista 4760/8770 RCE 0day                              |
            | exploit/abrt_privilege_escalation        | normal    |   ABRT - sosreport Privilege Escalation                                    |
            | exploit/web_delivery                     | good      |   Script Web Delivery                                                      |
            | exploit/apache                           | good      |   Apache exploit                                                           |
            | exploit/shellshock                       | good      |   cgi-bin/vulnerable shellshock                                            |
            | exploit/davtest                          | good      |   Testing tool for webdav server                                           |
            | exploit/phpmailer_injection              | normal    |   PHPMailer Sendmail Argument Injection                                    |
            | exploit/auto_sql                         | good      |   auto with sqlmap                                                         |
            | exploit/ldap_buffer_overflow             | normal    |   Apache module mod_rewrite LDAP protocol Buffer Overflow                  |
            | exploit/vbulletin_rce                    | good      |   vBulletin 5.x 0day pre-quth RCE exploit                                  |
            | exploit/cmsms_showtime2_rce              | normal    |   CMS Made Simple (CMSMS) Showtime2 File Upload RCE                        |
            | exploit/awind_snmp_exec                  | good      |   AwindInc SNMP Service Command Injection                                  |
            | exploit/webmin_packageup_rce             | excellent |   Webmin Package Updates Remote Command Execution                          |
            | exploit/samsung_knox_smdm_url            | good      |   Samsung Galaxy KNOX Android Browser RCE                                  |
            | exploit/cisco_dcnm_upload_2019           | excellent |   Cisco Data Center Network Manager Unauthenticated Remote Code Execution  |
            | exploit/zenworks_configuration           | excellent |   Novell ZENworks Configuration Management Arbitrary File Upload           |
            | exploit/cisco_ucs_rce                    | excellent |   Cisco UCS Director Unauthenticated Remote Code Execution                 |
            | exploit/sonicwall                        | normal    |   Sonicwall SRA <= v8.1.0.2-14sv remote exploit                            |
            | exploit/bluekeep                         | good      |   cve 2019 0708 bluekeep rce                                               |
            | exploit/eternalblue                      | good      |   MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption           |
            | exploit/inject_html                      | normal    |   Inject Html code in all visited webpage                                  |
            | exploit/robots                           | normal    |   robots.txt Detected                                                      |
            | exploit/jenkins_script_console           | good      |   Jenkins-CI Script-Console Java Execution                                 |
            | exploit/php_thumb_shell_upload           | good      |   php shell uploads                                                        |
            | exploit/cpanel_bruteforce                | normal    |   cpanel bruteforce                                                        |
            | exploit/cms_rce                          | normal    |   CMS Made Simple 2.2.7 - (Authenticated) Remote Code Execution            |
            | exploit/joomla_com_hdflayer              | manual    |   joomla exploit hdflayer                                                  |
            | exploit/wp_symposium_shell_upload        | good      |   symposium shell upload                                                   |
            | exploit/joomla0day_com_myngallery        | good      |   exploits com myngallery                                                  |
            | exploit/jm_auto_change_pswd              | normal    |   vulnerability                                                            |
            | exploit/android_remote_access            | expert    |   Remote Acces Administrator (RAT)                                         |
            | exploit/power_dos                        | manual    |   Denial Of Service                                                        |
            | exploit/tp_link_dos                      | normal    |   TP_LINK DOS, 150M Wireless Lite N Router, Model No. TL-WR740N            |
            | exploit/joomla_com_foxcontact            | high      |   joomla foxcontact                                                        |
            | exploit/joomla_simple_shell              | high      |   joomla simple shell                                                      |
            | exploit/joomla_comfields_sqli_rce        | high      |   Joomla Component Fields SQLi Remote Code Execution                       |
            | exploit/inject_javascript                | normal    |   Inject Javascript code in all visited webpage                            |
            | exploit/dns_bruteforce                   | high      |   Dns Bruteforce with nmap                                                 |
            | exploit/dos_attack                       | normal    |   hping3 dos attack                                                        |
            | exploit/shakescreen                      | high      |   Shaking Web Browser content                                              |
            | exploit/bypass_waf                       | normal    |   bypass WAf                                                               |
            | exploit/enumeration                      | high      |   simple enumeration                                                       |
            | exploit/restrict_anonymous               | normal    |   obtain credentials                                                       |
            | exploit/openssl_heartbleed               | high      |   dump openssl_heartbleed                                                  |
            | exploit/samba                            | good      |   Samba EXploits                                                           |
            | exploit/smb                              | good      |   Albitary samba exploit                                                   |
            | exploit/webview_addjavascriptinterface   | good      |   Android Browser and WebView addJavascriptInterface Code Execution        |
            -------------------------------------------------------------------------------------------------------------------------------------
    """)
def module_sec():
    print ("""
            +------------------------------------------------------------------------------------------------------------------------------------+
            | SCANNERS                                                                                                                           |
            --------------------------------------------------------------------------------------------------------------------------------------
            |     \033[31mCOMMANDS                                         Rank                                   Description   \033[1;37m                         |
            --------------------------------------------------------------------------------------------------------------------------------------
            | scanner/subdo                                      | normal |       Subdomains Enumerations                                        |
            | scanner/load_balancing                             | normal |       Enumerate a domain and Detected whether it has load balancing  |
            | scanner/enumiax                                    | good   |       protocol username enumeration                                  |
            | scanner/wordpress_user_dislosure                   | normal |       wordpress 5.3 User Disclosure                                  |
            | scanner/botnet_scanning                            | normal |       Bootnet Scanning, first need to find the botnet IP             |
            | scanner/check_ssl_certificate                      | normal |       SSL Certificate                                                |
            | scanner/http_services                              | normal |       Gather page titles from HTTP services                          |
            | scanner/dnsrecon                                   | normal |       Record enumeration                                             |
            | scanner/sslscan                                    | normal |       SSL Scanner                                                    |
            | scanner/port_check                                 | manual |       All Port scaning                                               |
            | scanner/ssl_cert                                   | normal |       Nmap script ssl-cert                                           |
            | scanner/dns_zone_transfer                          | normal |       Dns Zone transfer                                              |
            | scanner/dns_bruteforce                             | normal |       Dns Bruteforce                                                 |
            | scanner/zone_walking                               | normal |       Zone walking                                                   |
            | scanner/web_services                               | normal |       Get HTTP headers of web services                               |
            | scanner/http_enum                                  | normal |       Find web apps from known paths                                 |
            | scanner/ddos_reflectors                            | normal |       Scan for UDP DDOS reflectors                                   |
            | scanner/grabbing_detection                         | normal |       Lighter banner grabbing detection                              |
            | scanner/discovery                                  | normal |       Scan selected ports - ignore discovery                         |
            | scanner/bluekeep                                   | good   |       CVE-2019-0708 BlueKeep Microsoft Remote Desktop RCE Check      |
            | scanner/drupal_scan                                | good   |       drupal scanner                                                 |
            | scanner/eternalblue                                | good   |       SMB RCE Detection                                              |
            | scanner/header                                     | good   |       header Scanner with nmap                                       |
            | scanner/firewalk                                   | good   |       firewalk                                                       |
            | scanner/whois                                      | high   |       whois                                                          |
            | scanner/dmitry                                     | good   |       Information Gathering Tool                                     |
            | scanner/admin_finder                               | normal |       Admin finder                                                   |
            | scanner/heartbleed                                 | normal |       heartbleed scanner vulnerability                               |
            | scanner/wordpress_scan                             | normal |       wordpress scanner                                              |
            | scanner/ssl_scanning                               | good   |       SSL Vulnerability Scanning                                     |
            | scanner/dns_bruteforce                             | normal |       dns bruteforce                                                 |
            | scanner/nmap_scanner                               | normal |       port scanners nmap                                             |
            | scanner/https_discover                             | normal |       https discover                                                 |
            | scanner/smb_scanning                               | good   |       scan vulnerable SMB server                                     |
            | scanner/joomla_vulnerability_scanners              | high   |       vulnerability                                                  |
            | scanner/mysql_empty_password                       | good   |       mysql empty password Detected                                  |
            | scanner/joomla_scanners_v.2                        | good   |       joomla scaning                                                 |
            | scanner/joomla_scanners_v3                         | normal |       joomla scaning                                                 |
            | scanner/jomscan_v4                                 | good   |       scan joomla                                                    |
            | scanner/webdav_scan                                | normal |       webdav scan vulnerable                                         |
            | scanner/joomla_sqli_scanners                       | high   |       vulnerability scanners                                         |
            | scanner/lfi_scanners                               | good   |       lfi bug scan                                                   |
            | scanner/port_scanners                              | manual |       port scan                                                      |
            | scanner/dir_search                                 | high   |       directory webscan                                              |
            | scanner/dir_bruteforce                             | good   |       directory Scanning                                             |
            | scanner/wordpress_user_scan                        | good   |       get wordpress username                                         |
            | scanner/cms_war                                    | high   |       FULL SCAN ALL WEBSITES                                         |
            | scanner/usr_pro_wordpress_auto_find                | norma  |       find user vulnerability                                        |
            | scanner/nmap_vuln                                  | normal |       vulnerability Scanner                                          |
            | scanner/xss_scaner                                 | normal |       Detected vulnerability xss                                     |
            | scanner/spaghetti                                  | high   |       Web Application Security Scanner                               |
            | scanner/dnslookup                                  | normal |       dnslookup scan                                                 |
            | scanner/reverse_dns                                | normal |       Reverse Dns Lookup                                             |
            | scanner/domain_map                                 | normal |       scanner domain map                                             |
            | scanner/dns_report                                 | normal |       dns report                                                     |
            | scanner/find_shared_dns                            | normal |       find shared dns                                                |
            | scanner/golismero                                  | normal |       scan vulnerability with golismero                              |
            | scanner/dns_propagation                            | low    |       dns propagation                                                |
            | scanner/find_records                               | normal |       find records                                                   |
            | scanner/cloud_flare                                | normal |       cloud flare                                                    |
            | scanner/extract_links                              | normal |       links extract                                                  |
            | scanner/web_robot                                  | normal |       web robots scanner                                             |
            | scanner/enumeration                                | normal |       http-enumeration                                               |
            | scanner/ip_locator                                 | good   |       ip Detected LOcator                                            |
            --------------------------------------------------------------------------------------------------------------------------------------
    """)
def post():
   print("""
            +----------------------------------------------------------------------------------------------------------+
            | POST                                                                                                     |
            ------------------------------------------------------------------------------------------------------------
            |            \033[31mCOMMANDS                                 Rank                 Description   \033[1;37m                  |
            ------------------------------------------------------------------------------------------------------------
            |  post/enumeration                                 | normal |     http-enumeration                        |
            |  post/vbulletin                                   | high   |     exploits                                |
            |  post/wordpress_user_scan                         | good   |     scanners                                |
            |  post/aix_hashdump                                | good   |     AIX Gather Dump Password Hashes         |
            |  post/dir_search                                  | high   |     scanners                                |
            |  post/cms_war                                     | high   |     scanners                                |
            |  post/usr_pro_wordpress_auto_find                 | normal |     scanners                                |
            |  post/android_remote_access                       | good   |     exploits                                |
            |  post/samba                                       | good   |     exploits                                |
            ------------------------------------------------------------------------------------------------------------
""")
def pas():
    print( """
            +----------------------------------------------------------------------------------------------------------+
            | PASSWORD                                                                                                 |
            ------------------------------------------------------------------------------------------------------------
            |            \033[31mCOMMANDS                                 Rank                 Description   \033[1;37m                  |
            ------------------------------------------------------------------------------------------------------------
            | password/base64_decode                            | good  |      base64 decode                           |
            | password/md5_decrypt                              | good  |      md5 decrypt                             |
            | password/sha1_decrypt                             | good  |      sha1 decrypt                            |
            | password/sha256_decrypt                           | good  |      sha256 decrypt                          |
            | password/sha384_decrypt                           | good  |      sha384 decrypt                          |
            | password/sha512_decrypt                           | good  |      sha512 decrypt                          |
            | password/ssh_bruteforce                           | good  |      ssh password bruteforce                 |
            ------------------------------------------------------------------------------------------------------------
    """)

def db():
    print( """
            +-----------------------------------------------------------------------------------+
            |EXPLOITDB                                                                          |
            -------------------------------------------------------------------------------------
            |  \033[31mCommand                                      Description \033[1;37m                        |
            |-----------------------------------------------------------------------------------|
            |  exploitdb/exploits                  |    Informasion exploits vulnerability      |
            |  exploitdb/shellcode                 |    Informasion shellcode                   |
            -------------------------------------------------------------------------------------
    """)
def apache_module():
    print("""
    +---------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Apache_Modules                                                                                                                                           |
    -----------------------------------------------------------------------------------------------------------------------------------------------------------
    |         \033[31m Description                                                                                                       Command \033[1;37m                     |
    -----------------------------------------------------------------------------------------------------------------------------------------------------------
    | Apache (Windows x86) - Chunked Encoding (Metasploit)                                                             | exploits/windows_x86/remote/16782.rb |
    | Apache Commons FileUpload and Apache Tomcat - Denial of Service                                                  | exploits/multiple/dos/31615.rb       |
    | Apache Continuum - Arbitrary Command Execution (Metasploit)                                                      | exploits/linux/remote/39945.rb       |
    | Apache CouchDB - Arbitrary Command Execution (Metasploit)                                                        | exploits/linux/remote/45019.rb       |
    | Apache Jetspeed - Arbitrary File Upload (Metasploit)                                                             | exploits/java/remote/39643.rb        |
    | Apache Roller - OGNL Injection (Metasploit)                                                                      | exploits/java/remote/29859.rb        |
    | Apache Spark - (Unauthenticated) Command Execution (Metasploit)                                                  | exploits/java/remote/45925.rb        |
    | Apache Struts - 'ParametersInterceptor' Remote Code Execution (Metasploit)                                       | exploits/multiple/remote/24874.rb    |
    | Apache Struts - ClassLoader Manipulation Remote Code Execution (Metasploit)                                      | exploits/multiple/remote/33142.rb    |
    | Apache Struts - Developer Mode OGNL Execution (Metasploit)                                                       | exploits/java/remote/31434.rb        |
    | Apache Struts - Dynamic Method Invocation Remote Code Execution (Metasploit)                                     | exploits/linux/remote/39756.rb       |
    | Apache Struts - REST Plugin With Dynamic Method Invocation Remote Code Execution (Metasploit)                    | exploits/multiple/remote/39919.rb    |
    | Apache Struts - includeParams Remote Code Execution (Metasploit)                                                 | exploits/multiple/remote/25980.rb    |
    | Apache Struts 2 - DefaultActionMapper Prefixes OGNL Code Execution (Metasploit)                                  | exploits/multiple/remote/27135.rb    |
    | Apache Struts 2 - Namespace Redirect OGNL Injection (Metasploit)                                                 | exploits/multiple/remote/45367.rb    |
    | Apache Struts 2 - Struts 1 Plugin Showcase OGNL Code Execution (Metasploit)                                      | exploits/multiple/remote/44643.rb    |
    |                                                                                                                  |                                      |
    -----------------------------------------------------------------------------------------------------------------------------------------------------------
        """)
def mod():
    print ("""
            +------------------------------------------------------------------------------------------------------------------------------------+
            | LISTENERS MODULES                                                                                                                  |
            --------------------------------------------------------------------------------------------------------------------------------------
            |     \033[31mCOMMANDS                                         Rank                                   Description   \033[1;37m                         |
            --------------------------------------------------------------------------------------------------------------------------------------
            |  android_meterpreter_reverse_tcp                    | good  |      Android Meterpreter, Android Reverse TCP Stager                 |
            |  android_meterpreter_reverse_https                  | good  |      Android Meterpreter, Android Reverse HTTPS Stager               |
            |  java_jsp_shell_reverse_tcp                         | good  |      Java JSP Command Shell, Reverse TCP Inline                      |
            |  linux_x64_meterpreter_reverse_https                | good  |      linux/x64/meterpreter_reverse_https                             |
            |  linux_x64_meterpreter_reverse_tcp                  | good  |      Linux Meterpreter, Reverse TCP Inline                           |
            |  linux_x64_shell_reverse_tcp                        | good  |      Linux Command Shell, Reverse TCP Stager                         |
            |  osx_x64_meterpreter_reverse_https                  | good  |      OSX Meterpreter, Reverse HTTPS Inline                           |
            |  osx_x64_meterpreter_reverse_tcp                    | good  |      OSX Meterpreter, Reverse TCP Inline                             |
            |  php_meterpreter_reverse_tcp                        | good  |      PHP Meterpreter, PHP Reverse TCP Stager                         |
            |  python_meterpreter_reverse_https                   | good  |      Python Meterpreter Shell, Reverse HTTPS Inline                  |
            |  python_meterpreter_reverse_tcp                     | good  |      python/meterpreter_reverse_tcp                                  |
            |  windows_x64_meterpreter_reverse_https              | good  |      Windows Meterpreter Shell, Reverse HTTPS Inline (x64)           |
            |  windows_x64_meterpreter_reverse_tcp                | good  |      Windows Meterpreter Shell, Reverse TCP Inline x64               |
            |  cmd_windows_reverse_powershell                     | good  |      Windows Command Shell, Reverse TCP (via Powershell)             |
            +------------------------------------------------------------------------------------------------------------------------------------+
        """)
def list():
     print("""
            -------------------------------------------------------------------------------------
            |                                   Options                                         |
            -------------------------------------------------------------------------------------
            |  \033[31mCommand                                      Description \033[1;37m                        |
            |-----------------------------------------------------------------------------------|
            | show options                    |  Show Current Options Of Selected Module        |
            | show module                     |  show this modules                              |
            | set                             |  Select Module  For Use                         |
            | back                            |  back                                           |
            -------------------------------------------------------------------------------------
  """)

def jancok():
     print("""
             -------------------------------------------------------------------------------------
             |                                   Options                                         |
             -------------------------------------------------------------------------------------
             |  \033[31mCommand                                      Description \033[1;37m                        |
             |-----------------------------------------------------------------------------------|
             | show options                    |  Show Current Options Of Selected Module        |
             | set target                      |  set target                                     |
             | run                             |  Excute modules                                 |
             | back                            |  back                                           |
             | exit                            |  exit the progam                                |
             -------------------------------------------------------------------------------------
   """)
def tool1():
    print("""
            +---------------------------------------------------------+
            |                         Options                         |
            -----------------------------------------------------------
            |  \033[31mCommand                     Description\033[1;37m                |
            |---------------------------------------------------------|
            | show module                |  show modules              |
            | example                    |  ex use module tools       |
            | set                        |  Select module             |
            | back                       |  back to menu              |
            -----------------------------------------------------------
""")
def module_tool():
    print("""
            +------------------------------------------------------------------------------------+
            |Tools                                                                               |
            --------------------------------------------------------------------------------------
            |  \033[31mCommand                                      Description \033[1;37m                         |
            |------------------------------------------------------------------------------------|
            |  atscan                              | Advanced dork Search & Mass Exploit Scanner |
            |  sublist3r                           | sublist3r                                   |
            |  sn1per                              | Sn1per                                      |
            |  socialbox                           | SocialBox fb,ig,gmail,Twitter Bruteforce    |
            |  searchsploit                        | searchsploit exploit-db                     |
            |  xsstrike                            | xsstrike                                    |
            |  xsser                               | exploit and report XSS vulnerabilities      |
            |  wifigod                             | wifi attack                                 |
            --------------------------------------------------------------------------------------
    """)
def optionsdb():
        print("""
              +-----------------------------------------------------------------------+
              |                               OPTIONS                                 |
              -------------------------------------------------------------------------
              |  \033[31mCommand                                Description      \033[1;37m             |
              -------------------------------------------------------------------------
              | show module                     |  Lock this modules exploitdb        |
              | searchsploit                    |  searchsploit exploit-db            |
              | set                             |  set modules exploitdb              |
              | back                            |  back menu                          |
              -------------------------------------------------------------------------
""")
