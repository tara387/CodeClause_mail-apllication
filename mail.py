from tkinter import *
import smtplib

#main screen
master = Tk()
master.title('GUI python email App')

#functions
def send():
    try:
        username= temp_username.get()
        password= temp_pasword.get()
        to= temp_receiver.get()
        subject= temp_subject.get()
        body=temp_body.get()
        if username==""or password==""or subject==""or body=="":
            notif.config(text='all fiends required',fg="red")
            return
        else:
          finalmessage = 'subject:{}\n\n{}'.format(subject,body)
          server = smtplib.SMYP('smtp.gmail.com',587)
          server.starttls()
          server.login(username,password)
          server.sendmail(username,tp,finalmessage)
          notif.config(text='Email has been sent',fg='green')
                              
    except:
       notif.config(text="Error sending email",fg="red")
    
def reset():
    print("reset")
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    BodyEntry.delete(0,'end')
    

#Graphics
Label(master,text="GUI email App",font=('calibri',15)).grid(row=0,sticky=N)
Label(master,text="use the form below to send an email",font=('calibri',11)).grid(row=1,sticky=W,padx=5)



Label(master,text="email",font=('calibri',11)).grid(row=2,sticky=W,padx=5)
Label(master,text="password",font=('calibri',11)).grid(row=3,sticky=W,padx=5)
Label(master,text="To",font=('calibri',11)).grid(row=4,sticky=W,padx=5)
Label(master,text="subject",font=('calibri',11)).grid(row=5,sticky=W,padx=5)
Label(master,text="body",font=('calibri',11)).grid(row=6,sticky=W,padx=5)

notif = Label(master,text="",font=('calibri',11))
notif.grid(row=7,sticky=S,padx=5)


#storage

temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

#entries
usernameEntry= Entry(master,textvariable=temp_username)
usernameEntry.grid(row=2,column=0)
passwordEntry= Entry(master,show = "*",textvariable=temp_password)
passwordEntry.grid(row=3,column=0)
receiverEntry= Entry(master,textvariable=temp_receiver)
receiverEntry.grid(row=4,column=0)
subjectEntry= Entry(master,textvariable=temp_subject)
subjectEntry.grid(row=5,column=0)
BodyEntry= Entry(master,textvariable=temp_body)
BodyEntry.grid(row=6,column=0)



#Buttons
Button(master,text="send",command=send).grid(row=7,sticky=W,pady=15,padx=5)
Button(master,text="reset",command=reset).grid(row=7,sticky=W,pady=45,padx=45)


master.mainloop()




