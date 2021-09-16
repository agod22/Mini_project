#This program recieves a case(array) from client and calls pred_new on the recieved data. Also sends the predicted answer.
import socket
import pickle
import k_nearest_neighbors as knn
import support_vector_machine as svm
import artificial_neural_network as ann


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error " + str(msg) + "\n" + "Retrying...")

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port " + str(address[1]))
    send_msg(conn)
    conn.close()

def send_msg(conn):
    while True:
        msg = "Thank you for connecting"
        conn.send(str.encode(msg))
        response = pickle.loads(conn.recv(2048))
        ans = str(answer1(response))
        conn.send(str.encode(ans))
        return
def answer1(array):
    a = knn.acc()
    b = svm.acc()
    c = ann.acc()
    d = ((a * knn.pred_new(array)) + (b * svm.pred_new(array)) + (c * ann.pred_new(array))) / (a + b + c)
    return 1 if (d>0.5) else 0

def answer2(array,choice):
    if(choice == 1):
        return knn.pred_new(array)
    if(choice == 2):
        return svm.pred_new(array)
    if(choice == 3):
        return ann.pred_new(array)


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()


