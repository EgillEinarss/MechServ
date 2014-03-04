#!/usr/bin/python2.7

# Echo server program
import socket

def makeHtml(h,l):
    hiti = str((float(h)*5.0/1024.0 - 0.5)*0.01)
    if int(l) < 200:
        ljos = u"off."
    else:
        ljos = u"on."
    ljos = ljos + u" Measured voltage was " + str(float(l)/1024.0) + u"V."
    f = open('../templates/pages/placeholder.home.html','w')
    f.write(u'<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><title>Gangleri</title></head><body>')
    f.write(u"The tempature is " + hiti + u" degrees C<br />The lights are ")
    f.write(ljos)
    f.write(u"</body></html>")
    f.close()

HOST = ''                 # Symbolic name meaning the local host
PORT = 8080              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    cmd = raw_input()
    conn.send(cmd)
    if cmd == 'x':
        heat = conn.recv(1024)
        light = conn.recv(1024)
        makeHtml(heat,light)
    elif cmd == 'w' or cmd == 's':
        print 'Speed is ', conn.recv(1024)
    elif cmd == 'q':
        conn.close()
        break

