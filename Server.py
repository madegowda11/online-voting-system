import socket
import threading
import dframe as df
from threading import Thread
from dframe import *
from AES import *

lock = threading.Lock()

# Fixed AES key (must match client)
AES_KEY = [0x00, 0x01, 0x02, 0x03,
           0x04, 0x05, 0x06, 0x07,
           0x08, 0x09, 0x0a, 0x0b,
           0x0c, 0x0d, 0x0e, 0x0f]

aes = AES()  # Initialize AES instance


def encrypt_message(msg):
    """Encrypts a plaintext message (string) using AES and returns bytes."""
    msg_bytes = msg.encode('utf-8')[:16]                   # Truncate to 16 bytes
    msg_block = list(msg_bytes) + [0] * (16 - len(msg_bytes))  # Zero pad if shorter
    cipher_block = aes.encrypt(msg_block, AES_KEY)
    return bytes(cipher_block)


def decrypt_message(encrypted_bytes):
    """Decrypts a received AES-encrypted message (bytes) and returns string."""
    encrypted_list = list(encrypted_bytes[:16])             # Take 16-byte AES block
    decrypted_list = aes.decrypt(encrypted_list, AES_KEY)
    decrypted_str = bytes(decrypted_list).decode('utf-8', errors='ignore').rstrip('\x00')
    return decrypted_str



def client_thread(connection):

    encrypted_data = connection.recv(1024)
    data_str = decrypt_message(encrypted_data)              # 🔓 Decrypt received data
    log = data_str.split(' ')

    try:
        log[0] = int(log[0])

        if(df.verify(log[0],log[1])):                                #3 Authenticate
            if(df.isEligible(log[0])):
                print('Voter Logged in... ID:'+str(log[0]))
                connection.send("Authenticate".encode())
            else:
                print('Vote Already Cast by ID:'+str(log[0]))
                connection.send("VoteCasted".encode())
        else:
            print('Invalid Voter')
            connection.send("InvalidVoter".encode())
            return

    except:
        print('Invalid Credentials')
        connection.send("InvalidVoter".encode())
        return


    data = connection.recv(1024)
    vote_str = decrypt_message(data)
    print("Vote Received from ID: "+str(log[0])+"  Processing...")
    lock.acquire()
    #update Database
    if(df.vote_update(data.decode(),log[0])):
        print("Vote Casted Sucessfully by voter ID = "+str(log[0]))
        connection.send("Successful".encode())
    else:
        print("Vote Update Failed by voter ID = "+str(log[0]))
        connection.send("Vote Update Failed".encode())
                                                                        #5

    lock.release()
    connection.close()


def voting_Server():

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send("Connection Established".encode())   ### 1
        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    voting_Server()
