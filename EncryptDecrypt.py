from tkinter import *

import random

# Vigenère cipher for encryption and decryption
import base64

# creating root object
root = Tk()

# defining size of window
root.geometry("3000x6000")

# title of window
root.title("Message Cryptography")

Tops = Frame(root, width=2600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, height=1200, width=6000, relief=SUNKEN)
f1.pack(side=LEFT)


lblInfo = Label(Tops, font=('algeria', 90, 'bold'),
                text="CRYPTIC MESSAGING",
                fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)


# Initializing variables
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


lblText = Label(Tops,font=('calibri', 20, 'bold'),
               text="MODE: 'e' for ENCRYPTION and 'd' for DECRYPTION", bd=16, anchor="w") 
lblText.grid(row=8, column=0)


lblText2 = Label(Tops,font=('calibri', 20, 'bold'),
               text="use same Secret Key for ENCRYPTION and DECRYPTION", bd=16, anchor="w") 
lblText2.grid(row=9, column=0)


lbljustforspace = Label(f1, font=('calibri', 20, 'bold'),
               text="             ", bd=16, anchor="w")
lbljustforspace.grid(row=0, column=0)


# labels for the message
lblMsg = Label(f1, font=('calibri', 20, 'bold'),
               text="ENTER YOUR MESSAGE", bd=16, anchor="w")
lblMsg.grid(row=0, column=1)



# Input box for the message
txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=5, insertwidth=4,
               bg="powder blue", justify='left')
txtMsg.grid(row=0, column=2)


# labels for the Secret key
lblkey = Label(f1, font=('calibri', 20, 'bold'),
               text="ENTER SECRET KEY", bd=16, anchor="w")
lblkey.grid(row=1, column=1)


# Input box for the Secret key
txtkey = Entry(f1, font=('arial', 16, 'bold'),  show="*",
               textvariable=key, bd=5, insertwidth=3,
               bg="powder blue", justify='left')
txtkey.grid(row=1, column=2)


# labels for the mode
lblmode = Label(f1, font=('calibri', 20, 'bold'),
                text="ENTER MODE", bd=16, anchor="sw")
lblmode.grid(row=2, column=1)


# entry box for the mode
txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=5, insertwidth=3,
                bg="powder blue", justify='left', width=2)
txtmode.grid(row=2, column=2)


# labels for the Output
lblResult = Label(f1, font=('calibri', 20, 'bold'),
                  text="OUTPUT", bd=16, anchor="w")
lblResult.grid(row=0, column=5)


# entry box for the output
txtResult = Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=5, insertwidth=4,
                  bg="powder blue", justify='left')
txtResult.grid(row=0, column=6)



# encode funtion for Encryption
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# decode function for Decryption
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)
        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


#Results function to call encode or decode function depending upon the mode
def Results():
    msg = Msg.get()
    k = key.get()
    m = mode.get()
    if (m == 'e'):
        Result.set(encode(k, msg))
    elif (m == 'd'):
        Result.set(decode(k, msg))
    else:
        Result.set("Invalid Mode!!!")


# exit function is called, when quit button is pressed
def qExit():
    root.destroy()


# Reset Fuction is called, when clear button is pressed
def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# BOTTON SECTION
lblNothing = Label(f1, font=('calibri', 20, 'bold'),
               text="                        ", bd=16, anchor="w")
lblNothing.grid(row=0, column=11)

# Encrypt/Decrypt button
btnTotal = Button(f1, padx=14, pady=5, bd=8, fg="black",
                  font=('arial', 12, 'bold'), width=10,
                  text="Encrypt/Decrypt", bg="lime green",
                  command=Results).grid(row=0,column=12)


# clear button
btnReset = Button(f1, padx=14, pady=5, bd=8,
                  fg="black", font=('arial', 12, 'bold'),
                  width=10, text="Clear", bg="yellow",
                  command=Reset).grid(row=1,column=12)

# quit button
btnExit = Button(f1, padx=14, pady=5, bd=8,
                 fg="black", font=('arial', 12, 'bold'),
                 width=10, text="Quit", bg="red",
                 command=qExit).grid(row=2,column=12)

# keeps window alive
root.mainloop()