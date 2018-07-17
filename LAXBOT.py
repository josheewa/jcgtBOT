import socket,time,sys,random
network = ''
port = 
channels = ['#'] #Add as many as you want
nick = ''
identify = True
password = ''
insults = ["If laughter is the best medicine, your face must be curing the world.", "It's better to let someone think you are an Idiot than to open your mouth and prove it."]
badwords = ['bitch', 'cunt', 'fucc', 'fuck', 'damn', 'shit', 'hell', 'badwordtest',  'h͜͟e̷҉l͘l̢̛o̵̢', 'pussy', 'badword', 'lollypop', 'dirt', 'ass', 'razer', 'jcgt', 'PT_', 'prove', 'vore', 'futanari', '2girls1cup', 'furry']
irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
dis = False
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
        if msg.count ('LAXBOT') > 0 and vhost == "LAX18@202-5-69-158.static.panicbnc.ca" and lowermsg.count ('reconnect') > 0 or msg.count ('LAXBOT') > 0 and vhost == "LAX18@zeta-v4.4.elitebnc.org" and lowermsg.count ('reconnect') > 0:
                irc.send ('PRIVMSG '+chan+' :Im back....\r\n')
                dis = False
        if lowermsg.count('!qadd') == 0 and dis == False:
                if lowermsg == '&help':
                      irc.send ('PRIVMSG '+chan+' :Please go here to see all commands: https://github.com/LAX18/LAXBOT/wiki/Commands\r\n')
                if lowermsg == '&info' or msg == '&about':
                      irc.send ('PRIVMSG '+chan+' :Well, '+user+' , I am LAXBOT v.2, created by LAX18 on 5/25/18\r\n')
                if lowermsg.count('bot') > 0 and lowermsg.count('LAXBOT') > 0:
                      irc.send ('PRIVMSG '+chan+' :BOT?.... did someone say bot???\r\n')
                      irc.send ('PRIVMSG '+chan+' \x01'+'ACTION runs\x01\r\n')
                if lowermsg == "&creator" or lowermsg == "&owner":
                      irc.send ('PRIVMSG '+chan+' :Owner / Creator: LAX18\r\n')
                if lowermsg.count('hi') > 0 and msg.count('LAXBOT') > 0:
                      irc.send ('PRIVMSG '+chan+' :Hello, '+user+'\r\n')
                if lowernospacemsg.count('run') > 0 and msg.count('ACTION') > 0 or lowernospacemsg.count('rusn') > 0 and msg.count('ACTION') > 0:
                      irc.send ('PRIVMSG '+chan+' \x01ACTION chases down '+user+' \x01\r\n')
                if lowernospacemsg.count('hide') > 0 and msg.count('ACTION') > 0  or lowernospacemsg.count('hdies') > 0 and msg.count('ACTION') > 0:
                      irc.send ('PRIVMSG '+chan+' \x01ACTION finds and drags '+user+' out\x01\r\n')
                if lowermsg[:11] == "&releasethe" and msg[11:-12] != "LAXBOT":
                      target = msg[11:-12]
                      irc.send ('PRIVMSG '+chan+' :THE '+target+' CATCHING BOTS HAVE BEEN RELEASED!!!! \x01\r\n')
                if lowermsg == '&hellolaxbot':
                      irc.send ('PRIVMSG '+chan+' :Hello, '+user+'.\r\n')
                if lowermsg[:7] == '&murder' and lowernospacemsg[7:].count('lax') == 0 and lowernospacemsg[7:].count('laxbot') == 0 and lowernospacemsg[7:].count('him') == 0:
                      target = msg[7:]
                      irc.send ('PRIVMSG '+chan+' \x01ACTION finds and kills'+target+'\x01\r\n')
                if lowermsg[:8] == '&promote':
                      product = msg[8:]
                      irc.send ('PRIVMSG '+chan+' :Please use'+product+'. It is a exceptional product\r\n')
                if lowermsg[:7] == '&demote' and lowernospacemsg[7:].count('laxbot') == 0:
                      product = msg[7:]
                      irc.send ('PRIVMSG '+chan+' :Please DO NOT use'+product+'. It is a horrid product\r\n')
                if vhost == "" or vhost == "":
                      if msg[:5] == '&join':
                            newchan = msg[5:]
                            irc.send ('JOIN '+newchan+'\r\n')
                      if msg[:5] == '&quit':
                            newchan = msg[5:]
                            irc.send ('PART '+newchan+' :\r\n')
                      if msg[:5] == '&nick':
                            newnick = msg[6:]
                            irc.send ('NICK :'+newnick+'\r\n')
                      if lowermsg.count('disconnect') > 0 and msg.count ('LAXBOT') > 0:
                            irc.send ('PRIVMSG '+chan+' :Going offline...\r\n')
                            dis = True
                      if lowermsg.count('die') > 0 and msg.count('LAXBOT') > 0:
                            irc.send ('PRIVMSG '+chan+' :Goodbye cruel, cruel, world....\r\n')
                            break
                if msg[:8] == '&torment' and lowermsg[8:].count ('laxbot') == 0:
                      target = msg[8:]
                      entry = random.randint(0,1)
                      irc.send ('PRIVMSG '+chan+' :'+target+': '+insults[entry]+'\r\n')
                for x in badwords:
                      if lowermsg.count(x) > 0:
                            irc.send ('PRIVMSG '+chan+' :'+user+': Please refrain from using that language\r\n')
              # print user+" ("+vhost+") "+dType+" to "+chan+": "+msg
 
    except:
        pass
