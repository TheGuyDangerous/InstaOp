#!/usr/bin/env python3
import time #line:2
from colorama import Fore ,Back ,Style ,init #line:3
init (autoreset =True )#line:4
def startMessage ():#line:5
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter the OP vaala Code To Unlock The Tool : ")#line:6
    OOOO0OO000OO0OOOO ="guydangerous"#line:7
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :#line:8
        print (Fore .RED +'[X] Wrong Code , Correct code is guydangerous')#line:9
        startMessage ()#line:10
    else :#line:11
        print (Fore .GREEN +"Successfully Unlocked Tool! Created By Sannidhya")#line:12
        pass #line:13
if __name__ =="__main__":#line:14
    startMessage ()#line:15
from libs .check_modules import check_modules #line:16
from sys import exit #line:17
from os import _exit #line:18
check_modules ()#line:19
from os import path #line:20
from libs .logo import print_logo #line:21
from libs .utils import print_success #line:22
from libs .utils import print_error #line:23
from libs .utils import ask_question #line:24
from libs .utils import print_status #line:25
from libs .attack import report_profile_attack #line:26
from libs .attack import report_video_attack #line:27
from multiprocessing import Process #line:28
def chunks (O000O0O0OO000O0OO ,OOOOO0OOO00OO00OO ):#line:29
    ""#line:30
    for OOO0OO00O000OOO0O in range (0 ,len (O000O0O0OO000O0OO ),OOOOO0OOO00OO00OO ):#line:31
        yield O000O0O0OO000O0OO [OOO0OO00O000OOO0O :OOO0OO00O000OOO0O +OOOOO0OOO00OO00OO ]#line:32
def profile_attack_process (O0OOOOO00O0OO000O ,OOOOO0000OO00OOOO ):#line:33
    if (len (OOOOO0000OO00OOOO )==0 ):#line:34
        for _OOO00O0000O000O00 in range (10 ):#line:35
            report_profile_attack (O0OOOOO00O0OO000O ,None )#line:36
        return #line:37
    for OO00OO0OOOOO0OOOO in OOOOO0000OO00OOOO :#line:38
        report_profile_attack (O0OOOOO00O0OO000O ,OO00OO0OOOOO0OOOO )#line:39
def video_attack_process (O0O00O00O00OOO00O ,O0OO000OO0000OO0O ):#line:40
    if (len (O0OO000OO0000OO0O )==0 ):#line:41
        for _OOOO0O00000OOO0O0 in range (10 ):#line:42
            report_video_attack (O0O00O00O00OOO00O ,None )#line:43
        return #line:44
    for O0O0000OOO0OOO00O in O0OO000OO0000OO0O :#line:45
        report_video_attack (O0O00O00O00OOO00O ,O0O0000OOO0OOO00O )#line:46
def video_attack (OO0O00000000OOOOO ):#line:47
    OO000OO00000OO0O0 =ask_question ("Enter the link of the video you want to report")#line:48
    print (Style .RESET_ALL )#line:49
    if (len (OO0O00000000OOOOO )==0 ):#line:50
        for OO00O000OO0O0OO00 in range (5 ):#line:51
            O0OO00O0OO00OOO0O =Process (target =video_attack_process ,args =(OO000OO00000OO0O0 ,[],))#line:52
            O0OO00O0OO00OOO0O .start ()#line:53
            print_status (str (OO00O000OO0O0OO00 +1 )+". Transaction Opened!")#line:54
            if (OO00O000OO0O0OO00 ==5 ):print ()#line:55
        return #line:56
    OO0OOOOOOO0OOO000 =list (chunks (OO0O00000000OOOOO ,10 ))#line:57
    print ("")#line:58
    print_status ("Video complaint attack is on!\n")#line:59
    OO00O000OO0O0O000 =1 #line:60
    for OOOOO0O0OOO00O000 in OO0OOOOOOO0OOO000 :#line:61
        O0OO00O0OO00OOO0O =Process (target =video_attack_process ,args =(OO000OO00000OO0O0 ,OOOOO0O0OOO00O000 ,))#line:62
        O0OO00O0OO00OOO0O .start ()#line:63
        print_status (str (OO00O000OO0O0O000 )+". Transaction Opened!")#line:64
        if (OO00O000OO0O0O000 ==5 ):print ()#line:65
        OO00O000OO0O0O000 =OO00O000OO0O0O000 +1 #line:66
def profile_attack (OO00O0OOO00OOO0O0 ):#line:67
    OOOO0O00000OOO00O =ask_question ("Enter the username of the person you want to report")#line:68
    print (Style .RESET_ALL )#line:69
    if (len (OO00O0OOO00OOO0O0 )==0 ):#line:70
        for O00O00O00000OO0OO in range (5 ):#line:71
            O00000O000OOOOOO0 =Process (target =profile_attack_process ,args =(OOOO0O00000OOO00O ,[],))#line:72
            O00000O000OOOOOO0 .start ()#line:73
            print_status (str (O00O00O00000OO0OO +1 )+". Transaction Opened!")#line:74
        return #line:75
    OO00OOO0OO00OOOOO =list (chunks (OO00O0OOO00OOO0O0 ,10 ))#line:76
    print ("")#line:77
    print_status ("Profile complaint attack is starting!\n")#line:78
    O0OOOO0O00OOOOO0O =1 #line:79
    for OOOO0O00O0000OO00 in OO00OOO0OO00OOOOO :#line:80
        O00000O000OOOOOO0 =Process (target =profile_attack_process ,args =(OOOO0O00000OOO00O ,OOOO0O00O0000OO00 ,))#line:81
        O00000O000OOOOOO0 .start ()#line:82
        print_status (str (O0OOOO0O00OOOOO0O )+". Transaction Opened!")#line:83
        if (O0OOOO0O00OOOOO0O ==5 ):print ()#line:84
        O0OOOO0O00OOOOO0O =O0OOOO0O00OOOOO0O +1 #line:85
def main ():#line:86
    print_success ("Modules loaded!\n")#line:87
    O0OOO0O00OOO00O0O =ask_question ("Would you like to use a proxy? [Y / N]")#line:88
    O00O0OO00OOO0OO00 =[]#line:89
    if (O0OOO0O00OOO00O0O =="Y"or O0OOO0O00OOO00O0O =="y"):#line:90
        O0OOO0O00OOO00O0O =ask_question ("Would you like to collect your proxies from the internet? [Y / N]")#line:91
        if (O0OOO0O00OOO00O0O =="Y"or O0OOO0O00OOO00O0O =="y"):#line:92
            print_status ("PLEASE USE VPN AS YOU ARE USING THIS TOOL ON ANDROID")#line:93
        elif (O0OOO0O00OOO00O0O =="N"or O0OOO0O00OOO00O0O =="n"):#line:94
            print_status ("PLEASE USE VPN AS YOU ARE USING THIS TOOL ON ANDROID")#line:95
            pass #line:96
    elif (O0OOO0O00OOO00O0O =="N"or O0OOO0O00OOO00O0O =="n"):#line:97
        pass #line:98
    else :#line:99
        print_error ("Answer not understood, exiting!")#line:100
        exit ()#line:101
    print ("")#line:102
    print_status ("1 - Report Profile.")#line:103
    print_status ("2 - Report a video.")#line:104
    OOO0O0000OOO0O0OO =ask_question ("Please select the complaint method")#line:105
    print ("")#line:106
    if (OOO0O0000OOO0O0OO .isdigit ()==False ):#line:107
        print_error ("The answer is not understood.")#line:108
        exit (0 )#line:109
    if (int (OOO0O0000OOO0O0OO )>2 or int (OOO0O0000OOO0O0OO )==0 ):#line:110
        print_error ("The answer is not understood.")#line:111
        exit (0 )#line:112
    if (int (OOO0O0000OOO0O0OO )==1 ):#line:113
        profile_attack (O00O0OO00OOO0OO00 )#line:114
    elif (int (OOO0O0000OOO0O0OO )==2 ):#line:115
        video_attack (O00O0OO00OOO0OO00 )#line:116
if __name__ =="__main__":#line:117
    print_logo ()#line:118
    try :#line:119
        main ()#line:120
        print (Style .RESET_ALL )#line:121
    except KeyboardInterrupt :#line:122
        print ("\n\n"+Fore .RED +"[*] Program is closing!")#line:123
        print (Style .RESET_ALL )#line:124
        _exit (0 )