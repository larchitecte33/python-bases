from irc_class import *
import os
import random

## IRC Config
server = "irc.root-me.org" # Provide a valid server IP/Hostname
port = 6667
reponseAEteEnvoyee = False
channel = "#root-me_challenge"
botnick = "candy"
botnickpass = "guido"
botpass = "<%= @guido_password %>"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send("USER "+ botnick + "\n")
irc.send("NICK "+ botnick +"\n")
irc.send("JOIN "+ channel +"\n")
irc.send("PRIVMSG candy !ep1\r\n")

while not reponseAEteEnvoyee:
    text = irc.get_response()
    print(text)
 
#    irc.send(channel, "!ep1 -rep")
    reponseAEteEnvoyee = True