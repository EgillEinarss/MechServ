#!/usr/bin/python2.7

# Echo server program
import socket

def html(h,l):
    f = open('placeholder.home.html','w')
    f.write(u'<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><title>Gangleri</title></head><body>')
    f.write(u"The tempature is " + str(h) +u"°<br />The lights are ")
    if l == 1:
        f.write(u"on.")
    else:
        f.write(u"off.")
    f.write(u"</body></html>")
    f.close()

HOST = ''                 # Symbolic name meaning the local host
PORT = 8080              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
#while 1:
#    data = conn.recv(1024)
#    if not data: break
#    print data
#    conn.send(data)
heat = conn.recv(1024)
light = conn.recv(1024)
conn.send("25")
conn.close()