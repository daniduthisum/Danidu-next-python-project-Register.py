from tkinter import *
from tkinter.font import names
from tkinter.ttk import *

root=Tk()
root.title("Tech World DT")
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text="DT TECH Registration form",font="arial 15 bold").grid(row=0, column=3)


#Field Name
Name=Label(root, text="Name")
Gender=Label(root, text="Gender")
Website=Label(root, text="Website")
Email=Label(root, text="Email")
Contact=Label(root, text="Contact")

# Packing Fields
Name.grid(row=1, column=2)
Gender.grid(row=2, column=2)
Website.grid(row=3, column=2)
Email.grid(row=4, column=2)
Contact.grid(row=5, column=2)

# Variable for storing data
Namevalue = StringVar
Gendervalue = StringVar
Websitevalue = StringVar
Emailvalue = StringVar
Contactvalue = StringVar
chekvalue = IntVar

# Creatind entry field
Nameentry =Entry(root, textvariable=Namevalue)
Genderentry =Entry(root, textvariable=Gendervalue)
Websiteentry =Entry(root, textvariable=Websitevalue)
Emailentry =Entry(root, textvariable=Emailvalue)
Contactentry =Entry(root, textvariable=Contactvalue)

# Packing entry fields
Nameentry.grid(row=1, column=3)
Genderentry.grid(row=2, column=3)
Websiteentry.grid(row=3, column=3)
Emailentry.grid(row=4, column=3)
Contactentry.grid(row=5, column=3)

#Creating Chekbox
chekbtn= Checkbutton(text="remember me?" , variable= chekvalue)
chekbtn.grid(row=6 , column= 3)

# Submit button
Button(text="submit", command=getvals).grid(row=7, column=3)

root.mainloop()
