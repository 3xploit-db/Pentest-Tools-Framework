# -*- coding: utf-8 -*-
import random
import os,sys
import time
from time import sleep
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End

banner1 ="""\033[1;32m
                               #########
                           #################             #
                         ######################         #
                        #########################      #
                      ############################
                     ##############################
                     ###############################
                    ###############################
                    ##############################
                                    #    ########   #
                      \033[31m ##        ### \033[1;32m       ####   ##
                                            ###   ###
                                          ####   ###
                     ####          ##########   ####
                     #######################   ####
                       ####################   ####
                        ##################  ####
                          ############      ##
                             ########        ###
                            #########        #####
                          ############      ######
                         #####       ########
                        ########      #########
                             ###       #########
                            ######    ############
                           #######################
                           #   #   ###  #   #   ##
                           ########################
                            ##     ##   ##     ##

\033[1;m"""
banner2 =("""
\033[1;36m
┌══════════════════════════════════════════════════════════════┐
█             ====                            ====             █
█                   PENTESTS TOOLS FRAMEWORK                   █
█    =====                                           =====     █
└══════════════════════════════════════════════════════════════┘     \033[1;m"""

)
banner3 = """\033[1;36m
         ::::::::: ::::::::::: ::::::::::
        :+:    :+:    :+:     :+:
       +:+    +:+    +:+     +:+
      +#++:++#+     +#+     :#::+::#
     +#+           +#+     +#+
    #+#           #+#     #+#
   ###           ###     ###
                        (PENTESTS TOOLS FRAMEWORK)
\033[1;m
"""
banner4 = ("""
    \033[1;31m
          ....      ..         .....              .....
     +^""888h. ~"888h    .H8888888h.  ~-.   .H8888888x.  '`+
    8X.  ?8888X  8888f   888888888888x  `> :888888888888x.  !
   '888x  8888X  8888~  X~     `?888888hx~ 8~    `"*88888888''
   '88888 8888X   "88x: '      x8.^''*88*''  !      .  `f''''
    `8888 8888X  X88x.   `-:- X8888x        ~:...-` :8L <)88:
      `*` 8888X '88888X       488888>          .   :888:>X88!
     ~`...8888X  "88888     .. `"88*        :~"88x 48888X ^`
      x8888888X.   `%8'   x88888nX"      . <  :888k'88888X
     '%''*8888888h.   '   !"*8888888n..  :    d8888f '88888X
     ~    888888888!`   '    "*88888888*    :8888!    ?8888>
          X888^'''              ^"***"`     X888!      8888~
          `88f \033[1;36m [Pentest Tools Framework]\033[1;31m  '888       X88f
           88                =               '%8:     .8*"
           ""             ==   ==              ^----~"`

""")
stream = (banner1, banner2, banner3, banner4 )
def banner():
	print random.choice(stream)
def info():
                                                                                            # #
    print("""\033[1;31m
    +---------------------------------------------------------------------+
    |                      Pentest Tools Framework                        |
    |                        \033[32m    V2.2[Beta]  \033[1;31m                             |
    |                                                                     |
    | \033[0;33mEmails:xzhack206@gmail.com\033[1;31m                                          |
    | \033[0;33mTelegram:@WongNdesoCok  \033[1;31m                                            |
    | Report Bugs and ask questions[**] xzhack206@gmail.com               |
    |          \033[1;37m Pentest Tools Framework  Copyright (C) 2019\033[1;31m               |
    +---------------------------------------------------------------------+\n"""+N+"")
def ptf():
    print
    print ""+N+"         =[ "+O+"Pentest v2.2[Beta]                         "+N+"]"
    print "  + -- --=[ "+B+"            MODULES \033[0;33m(7)                    "+N+"]"
    print "  + -- --=[ "+R+"49 exploits 61 scanners  9 post            "+N+"]"
    print "  + -- --=[ "+R+"7 password 14 listeners exploit-db         "+N+"]"
    print "  + -- --=[ "+R+"8 Tools                                    "+N+"]\n"

def credits():
    def credit(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random() * 0.3)
    print""+G+"""
                                         Credits & Thanks"""
    sleep(0.4)
    print""+B+""
    credit('\t\t\t[nmap Security Scanner]')
    print""+R+""
    sleep(0.4)
    credit('\t\t\t[metasploit-framework]')
    print""+O+""
    sleep(0.4)
    credit('\t\t\t[exploit-db]')
    print""+G+""
    sleep(0.4)
    credit('\t\t\t[offensive-security]')
    print""+B+""
    sleep(0.4)
    credit('\t\t\t[Github]')
    print""+R+""
    sleep(0.4)
    credit('\t\t\t[ https://xerosecurity.com]')
    print""+N+""
def exits():
    def exit(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random() * 0.9)
    print""+G+""
    sleep(0.4)
    print""+B+""
    exit('--[+] Thanks for using PTF [+]--')
    print""+R+""
