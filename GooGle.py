#!/usr/bin/python3
import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.efnet.org" # Server
channel = "#jcgtBOTSMASH" # Channel
botnick = "GooGle" # Your bots nick
adminname = "jcgter" #Your IRC nickname. On IRC (and most other places) I go by OrderChaos so that’s what I am using for this example.
exitcode = "bye " + botnick

ircsock.connect((server, 6697)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot
