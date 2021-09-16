import socket
import pickle

'''s = socket.socket()
host = '127.0.0.1'
port = 9999

s.connect((host,port))

data = s.recv(1024)
print(data.decode('utf-8'))'''

def send_data(y):
    s = socket.socket()
    host = '127.0.0.1'
    port = 9999

    s.connect((host,port))

    data = s.recv(1024)
    print(data.decode('utf-8'))
    print(y)
    #y = [57,1,0,144,193,1,1,141,0,3.4,1,2,3] #This array needs to be entered through the app interface.
    msg = pickle.dumps(y)
    s.send(msg)
    ans = s.recv(1024)
    ans = int(ans) # answer to be shown in the app
    return ans
    s.close()
