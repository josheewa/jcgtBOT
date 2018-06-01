import socket,time,sys,random
network = 'gamma.elitebnc.org'
port = 1338
channels = ['#GooGleBOT'] #Add as many as you want
nick = 'BOT'
identify = True
password = '11azv86s'
irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# print "Connecting to "+network+" ..."
irc.connect ((network, port))
# print "Changing nick to "+nick+"..."
irc.send ('NICK '+nick+'\r\n')
if identify == True:
        # print "Verifying password..."
        irc.send("PASS %s\n" % (password))
# print "Setting login data..."
# irc.send ('USER '+nick+' '+nick+' '+nick+' :'+nick+' IRC\r\n')
irc.send ('USER '+nick+' * *  :'+nick+'\r\n')
time.sleep(1)
for channel in channels:
        # print "Joining "+channel+"..."
        irc.send ('JOIN '+channel+'\r\n')
        irc.send ('PRIVMSG '+channel+' :'+nick+' Started! Type &help for more\r\n')
        time.sleep(1)
# print nick+" bot started."
while True:
    data = irc.recv(4096)
    if data.find('PING') != -1:
        irc.send('PONG '+data.split()[1]+'\r\n')
    try:
        user = data.split("!",1)[0].replace(":","",1)
        vhost = data.split(" ",1)[0].split("!",1)[1]
        dType = data.split(" ",1)[1].split(" ",1)[0]
        chan = data.split(" ",1)[1].split(" ",1)[1].split(" ",1)[0]
        msg = data.split(" ",1)[1].split(" ",1)[1].split(" ",1)[1].replace(":","",1).replace("\n","",1).replace("\r","",1)
        lowermsg = msg.lower()
        nospacemsg = msg.replace (' ','')
        lowernospacemsg = lowermsg.replace (' ','')
        if lowermsg.count('!qadd') == 0:
                if lowermsg == '&help':
                      irc.send ('PRIVMSG '+chan+' :Please go here to see all commands: https://github.com/LAX18/LAXBOT/wiki/Commands\r\n')
 
    except:
        pass
