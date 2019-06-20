from LINEPYBOTEATER import *
from datetime import datetime, timedelta
from threading import Thread
import time, random, sys, json, codecs, threading, asyncio, glob, re, string, os, six, ast, pytz, atexit, traceback
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

#### INPUT TOKEN HERE ###
tkn1= ""
tkn2= ""
tkn3= ""
tkn4= ""
tkn5= ""


headers= ["CHROMEOS\t2.1.5\tEater\t1", "IOSIPAD\t8.11.0\tEater\t1", "DESKTOPWIN\t5.8.0\tEater\t1", "DESKTOPMAC\t5.8.0\tEater\t1", "WIN10\t5.5.5\tEater\t1", "CLOVAFRIENDS\t5.5.1\tEater\t10.13.2"]
for num in range(len(headers)):
    head= headers[num]
    num= num+1
    print("{}. {}".format(num, head))
appn = int(input("Select Header = "))
appn = headers[appn-1]
print("""Use Token Login???
1. Yes
2. No""")
selct = int(input("Select = "))
if selct == 1:
    eater = LINE(tkn1, appName=appn)
    fighter1 = LINE(tkn2, appName=appn)
    fighter2 = LINE(tkn3, appName=appn)
    assasin1 = LINE(tkn4, appName=appn)
    assasin2 = LINE(tkn5, appName=appn)
elif selct == 2:
    eater = LINE(appName=appn)
    fighter1 = LINE(appName=appn)
    fighter2 = LINE(appName=appn)
    assasin1 = LINE(appName=appn)
    assasin2 = LINE(appName=appn)
else:
    print("Wrong Input!!!")
    sys.exit()

print("============= ARMY READY!!! =============")

############### PREPAIR ############
oepoll = OEPoll(eater)
boteaterid = eater.profile.mid
fighter1id = fighter1.profile.mid
fighter2id = fighter2.profile.mid
assasin1id = assasin1.profile.mid
assasin2id = assasin2.profile.mid
fighterlist = [fighter1, fighter2]
armylist = [boteaterid, fighter1id, fighter2id, assasin1id, assasin2id]
botlist = [eater, fighter1, fighter2, assasin1, assasin2]
protect = False
datapro = {"protect": False,
           "joinkick": False,
           "reinvt": False,
           "js1": [],
           "js2": [],
           "bl": [],
           "admin": []}

##### ADD BOT #####
for bottt in botlist:
    for bott in armylist:
        try:
            bottt.findAndAddContactsByMid(bott)
        except:
            pass


############### FUNC ############
helpmsg= """> BOTEATER SIMPLE PROTECT <
> CallArmy
> AntiJS1 (Patern 1)
> AntiJS2 (Patern 2)
> AntiJS Out
> Protect ON/OFF
> Reinvite ON/OFF
> JoinKick ON/OFF
> Clear BlackList
> Restart
> Speed
> About"""

#### IF WANT REWORK // EDIT DONT REMOVE CREATOR NAME :) ###
aboutmsg= """> BOTEATER SIMPLE PROTECT <
> CREATOR <
Hery Winarto
BotEater

> REWORK <
Yuda Adi Pratama

> VERSION <
V.1 BETA

> BUG <
PLEASE REPORT BUG:
line.me/ti/p/~hertot"""

def attck(grup, target):
    try:
        asd= fighter1.kickoutFromGroup(grup, [target])
        if asd != None:
            boteaterfail
    except:
        try:
            asd= fighter2.kickoutFromGroup(grup, [target])
            if asd != None:
                boteaterfail
        except:
            try:
                asd= eater.kickoutFromGroup(grup, [target])
                if asd != None:
                    boteaterfail
            except:
                pass
    print("> BOTEATER ATTACK <")

def cancl(grup, target):
    try:
        asd= fighter1.cancelGroupInvitation(grup, [target])
        if asd != None:
            boteaterfail
    except:
        try:
            asd= fighter2.cancelGroupInvitation(grup, [target])
            if asd != None:
                boteaterfail
        except:
            try:
                asd= eater.cancelGroupInvitation(grup, [target])
                if asd != None:
                    boteaterfail
            except:
                pass
    print("> BOTEATER CANCEL<")

def invt(grup, target):
    try:
        fighter1.findAndAddContactsByMid(target)
        asd= fighter1.inviteIntoGroup(grup, [target])
        if asd != None:
            boteaterfail
    except:
        try:
            fighter2.findAndAddContactsByMid(target)
            asd= fighter2.inviteIntoGroup(grup, [target])
            if asd != None:
                boteaterfail
        except:
            try:
                eater.findAndAddContactsByMid(target)
                asd= eater.inviteIntoGroup(grup, [target])
                if asd != None:
                    boteaterfail
            except:
                pass
    print("> BOTEATER INVITE <")

def backp(grup, target):
    try:
        fighter1.inviteIntoGroup(grup, [target])
        if target == fighter1id:
            fighter1.acceptGroupInvitation(grup)
        if target == fighter2id:
            fighter2.acceptGroupInvitation(grup)
        if target == boteaterid:
            eater.acceptGroupInvitation(grup)
    except:
        try:
            fighter2.inviteIntoGroup(grup, [target])
            if target == fighter1id:
                fighter1.acceptGroupInvitation(grup)
            if target == fighter2id:
                fighter2.acceptGroupInvitation(grup)
            if target == boteaterid:
                eater.acceptGroupInvitation(grup)
        except:
            try:
                eater.inviteIntoGroup(grup, [target])
                if target == fighter1id:
                    fighter1.acceptGroupInvitation(grup)
                if target == fighter2id:
                    fighter2.acceptGroupInvitation(grup)
                if target == boteaterid:
                    eater.acceptGroupInvitation(grup)
            except:
                pass
    print("> BOTEATER BACKUP <")
                
def lockqr(grup):
    G = eater.getGroup(grup)
    G.preventedJoinByTicket = True
    try:
        asd= fighter1.updateGroup(G)
        if asd != None:
            boteaterfail
    except:
        try:
            asd= fighter2.updateGroup(G)
            if asd != None:
                boteaterfail
        except:
            try:
                asd= eater.updateGroup(G)
                if asd != None:
                    boteaterfail
            except:
                pass
    print("> BOTEATER LOCKQR <")

def jsattck1(grup, target):
    try:
        assasin1.acceptGroupInvitation(grup)
        assasin1.kickoutFromGroup(grup, [target])
        assasin1.inviteIntoGroup(grup, [boteaterid])
        eater.acceptGroupInvitation(grup)
    except:
        pass
    print("> BOTEATER JS1ATTACK <")

def jsattck2(grup, target):
    try:
        fighter1.inviteIntoGroup(grup, [assasin2id])
        assasin2.acceptGroupInvitation(grup)
        assasin2.kickoutFromGroup(grup, [target])
        assasin2.inviteIntoGroup(grup, [boteaterid])
        eater.acceptGroupInvitation(grup)
    except:
        try:
            fighter2.inviteIntoGroup(grup, [assasin2id])
            assasin2.acceptGroupInvitation(grup)
            assasin2.kickoutFromGroup(grup, [target])
            assasin2.inviteIntoGroup(grup, [boteaterid])
            eater.acceptGroupInvitation(grup)
        except:
            try:
                eater.inviteIntoGroup(grup, [assasin2id])
                assasin2.acceptGroupInvitation(grup)
                assasin2.kickoutFromGroup(grup, [target])
                assasin2.inviteIntoGroup(grup, [boteaterid])
                eater.acceptGroupInvitation(grup)
            except:
                pass
    print("> BOTEATER JS2ATTACK <")

def black(target):
    if target not in datapro["bl"]:
        datapro["bl"].append(target)
    
############### LOOP ############
def boteater(op):
    try:
        if op.type == 11: #QR
            if datapro["protect"] == True:
                if op.param2 not in datapro["admin"] + armylist:
                    t1 = Thread(target=attck, args=(op.param1, op.param2))
                    t1.start()
                    t2 = Thread(target=lockqr, args=(op.param1,))
                    t2.start()
                    t3 = Thread(target=black, args=(op.param2,))
                    t3.start()
                    
        if op.type == 17: #JOIN
            if datapro["joinkick"] == True:
                if op.param2 not in datapro["admin"] + armylist:
                    t4 = Thread(target=attck, args=(op.param1, op.param2))
                    t4.start()
            if op.param2 in datapro["bl"]:
                    t5 = Thread(target=attck, args=(op.param1, op.param2))
                    t5.start()
        if op.type == 13: #INVITE
            if datapro["protect"] == True:
                if op.param2 not in datapro["admin"] + armylist:
                    t6 = Thread(target=attck, args=(op.param1, op.param2))
                    t6.start()
                    t7 = Thread(target=cancl, args=(op.param1, op.param3))
                    t7.start()
                    t8 = Thread(target=black, args=(op.param2,))
                    t8.start()
                    
        if op.type == 19: #KICK
            if datapro["protect"] == True:
                if op.param2 not in datapro["admin"] + armylist:
                    t9 = Thread(target=attck, args=(op.param1, op.param2))
                    t9.start()
                    t10 = Thread(target=black, args=(op.param2,))
                    t10.start()
                if op.param3 in armylist:
                    t11 = Thread(target=backp, args=(op.param1, op.param3))
                    t11.start()
            if datapro["reinvt"] == True:
                if op.param2 not in datapro["admin"] + armylist:
                    if op.param3 not in armylist:
                        t12 = Thread(target=invt, args=(op.param1, op.param3))
                        t12.start()
            if op.param1 in datapro["js1"]:
                t13 = Thread(target=jsattck1, args=(op.param1, op.param2))
                t13.start()
                t14 = Thread(target=black, args=(op.param2,))
                t14.start()
                
        if op.type == 32: #CANCEL
            if datapro["protect"] == True:
                if op.param2 not in datapro["admin"] + armylist:
                    t15 = Thread(target=attck, args=(op.param1, op.param2))
                    t15.start()
                    t16 = Thread(target=black, args=(op.param2,))
                    t16.start()
            if op.param1 in datapro["js2"]:
                t17 = Thread(target=jsattck2, args=(op.param1, op.param2))
                t17.start()
                t18 = Thread(target=black, args=(op.param2,))
                t18.start()
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            msg.from_ = msg._from
            sender = msg._from
            cmd = text.lower()
            if msg.toType == 0 and sender != boteaterid: to = sender
            else: to = receiver
            if msg.text is None:
                return
            else:
                if cmd == "protect on":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            datapro["protect"] = True
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "protect off":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            datapro["protect"] = False
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "joinkick on":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            datapro["joinkick"] = True
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "joinkick off":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            datapro["joinkick"] = False
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "reinvite on":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            datapro["reinvt"] = True
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "reinvite off":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            datapro["reinvt"] = False
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "antijs1":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            try:
                                eater.inviteIntoGroup(to, [assasin1id])
                            except:
                                try:
                                    fighter1.inviteIntoGroup(to, [assasin1id])
                                except:
                                    try:
                                        fighter2.inviteIntoGroup(to, [assasin1id])
                                    except:
                                        print("Fail Invite Antijs1")
                            datapro["js1"].append(to)
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "antijs2":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            datapro["js2"].append(to)
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "callarmy":
                    if msg.toType == 2:
                        if sender in armylist + datapro["admin"]:
                            G = fighter1.getGroup(to)
                            G.preventedJoinByTicket = False
                            eater.updateGroup(G)
                            Ticket = eater.reissueGroupTicket(to)
                            for army in fighterlist:
                                try:
                                    army.acceptGroupInvitationByTicket(to, Ticket)
                                except:
                                    pass
                            G.preventedJoinByTicket = True
                            eater.updateGroup(G)
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "speed":
                    start = time.time()
                    eater.sendMessage(to, "Loading Speed...")
                    elapsed_time = time.time() - start
                    eater.sendMessage(to, "{}".format(str(elapsed_time)))
                if cmd == "restart":
                    if sender in armylist + datapro["admin"]:
                        eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                        os.execl(sys.executable, sys.executable, *sys.argv)
                if cmd == "clear blacklist":
                    if sender in armylist + datapro["admin"]:
                        datapro["bl"] = []
                        eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "antijs out":
                    if sender in armylist + datapro["admin"]:
                        if msg.toType == 2:
                            try:
                                assasin1.leaveGroup(to)
                            except:
                                pass
                            try:
                                assasin2.leaveGroup(to)
                            except:
                                pass
                            eater.sendMessage(to, "> Boteater Notif < \nSuccess!!!")
                if cmd == "help":
                    eater.sendMessage(to,helpmsg)
                if cmd == "about":
                    eater.sendMessage(to,aboutmsg)
    except Exception as error:
    	print(error)

def run():
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   boteater(op)
                   oepoll.setRevision(op.revision)
        except Exception as e:
            print (e)

if __name__ == "__main__":
    run()
