import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image
from AES import *

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    # Encryption of vote casted using AES

    aes = AES()
    plaintext_str = vote
    plaintext_bytes = plaintext_str.encode('utf-8')[:16]  # Take first 16 bytes
    plaintext = list(plaintext_bytes) + [0] * (16 - len(plaintext_bytes))  # Pad with zeros if shorter
    key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]  # Fixed key

    ciphertext = aes.encrypt(plaintext, key)

# Convert ciphertext list to bytes before sending
    ciphertext_bytes = bytes(ciphertext)
    client_socket.send(ciphertext_bytes) 

    message = client_socket.recv(1024) #Success message

     # Convert received bytes to list of ints for your AES decrypt method
    encrypted_message_list = list(message[:16])  # AES block size = 16 bytes
    decrypted_list = aes.decrypt(encrypted_message_list, key)

    # Convert decrypted bytes back to string
    decrypted_str = bytes(decrypted_list).decode('utf-8', errors='ignore').rstrip('\x00')

    print("Decrypted server message:", repr(decrypted_str))
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "BJP\n\nNarendra Modi", variable = vote, value = "bjp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"bjp",client_socket)).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((45,45),Image.LANCZOS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Congress\n\nRahul Gandhi", variable = vote, value = "cong", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"cong",client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((35,48),Image.LANCZOS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Aam Aadmi Party\n\nArvind Kejriwal", variable = vote, value = "aap", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"aap",client_socket) ).grid(row = 4,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((55,40),Image.LANCZOS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "Shiv Sena\n\nUdhav Thakrey", variable = vote, value = "ss", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"ss",client_socket)).grid(row = 5,column = 1)
    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((50,45),Image.LANCZOS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote, value = "nota", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"nota",client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((45,35),Image.LANCZOS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
