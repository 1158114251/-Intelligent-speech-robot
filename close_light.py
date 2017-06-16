# telnet program example
import socket, select, string, sys
import time 
import os
def prompt() :
    print("333")
    sys.stdout.write('<You> ')
    sys.stdout.flush()
 
#main function
if __name__ == "__main__":
     
  #  if(len(sys.argv) < 3) :
   #     print ('Usage : python telnet.py hostname port')
    #    sys.exit()
     
    host = "www.bigiot.net"
    port = 8181
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print ('Unable to connect')
        sys.exit()
     
    print ('Connected to remote host. Start sending messages')
    checkinBytes=bytes('{\"M\":\"checkin\",\"ID\":\"2068\",\"K\":\"7b0361f93\"}\n')
    s.sendall(checkinBytes)
    time.sleep(1)
    checkinBytes=bytes('{\"M\":\"say\",\"ID\":\"D2315\",\"C\":\"play\"}\n')
    s.sendall(checkinBytes)
    time.sleep(1)
#    os.system("mplayer wav/close_light.mp3")
    prompt()
    s.close()
