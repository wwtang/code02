

import socket

print "Creating socket"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done"


#find the port number of the target host
print "looking up port number"
port = socket.getservbyname("http", 'tcp')
print "Done"

print port


# we need a host name and port numnber
print "Connecting socket to server"
s.connect(("www.google.com", port))
print "Done"



print "Connected from", s.getsockname()
print "Connected to",s.getpeername()
