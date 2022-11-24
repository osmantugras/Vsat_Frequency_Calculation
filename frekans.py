# Import the required libraries
import tkinter as tk
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("850x500")
win.title("Frequency Calculation")




def cal_exe():
   win1=Tk()
   win1.geometry("1000x55")
   win1.title("Frequency Line")
   w = Canvas(win1, width=1000, height=50)
   w.pack()
   t1=int(a.get()) #Uplink Frequency
   t2=int(b.get()) #Downlink Frequency
   t3=int(c.get()) #Total Bandwidth
   t4=int(x.get()) #Gateway Bandwidth
   t5=int(y.get()) #Remote Bandwidt
   s=(t4+t5)/300   #
   exe=t1-t2
   bwstart=(t1-(t3/2))
   bwstop=(t1+(t3/2))
   CenterGateway=((t1-(t3/2))+(t4/2))
   CenterRemote=((t1+(t3/2))-(t5/2))
   w.create_rectangle(0, 0, 100*t4, 50, fill="red", outline = 'red')
   text=w.create_text(25*t4,10, text="Gateway Center Frequency:" +str(CenterGateway), font=('Calibri 10'), anchor="w", fill="white")
   w.create_rectangle(100*t4, 0, 1000, 50, fill="blue", outline = 'blue')
   text2=w.create_text(1000-100*t4,10, text="Remote Center Frequency:  " +str(CenterRemote), font=('Calibri 10'), anchor="w", fill="white")
   textE="Translation Frequency: " +str(exe)
   label.config(text=textE)
   textS="Start Frequency: " +str(bwstart)
   labelstrt.config(text=textS)
   textStop="Stop Frequency:  " +str(bwstop)
   labelstp.config(text=textStop)
   
   
   

# Create an Entry widget
Label(win, text="Uplink Frequency", font=('Calibri 10')).pack()
a=Entry(win, width=35)
a.pack()
Label(win, text="Downlink Frequency", font=('Calibri 10')).pack()
b=Entry(win, width=35)
b.pack()
Label(win, text="Total Bandwidth", font=('Calibri 10')).pack()
c=Entry(win, width=35)
c.pack()
Label(win, text="Gateway Bandwidth", font=('Calibri 10')).pack()
x=Entry(win, width=35)
x.pack()
Label(win, text="Remote Bandwidth", font=('Calibri 10')).pack()
y=Entry(win, width=35)
y.pack()

label=Label(win, text="Translation Frequency : ", font=('Calibri 15'))
label.pack(pady=20)

labelstrt=Label(win, text="Start Frequency : ", font=('Calibri 15'))
labelstrt.pack(pady=20)

labelstp=Label(win, text="Stop Frequency : ", font=('Calibri 15'))
labelstp.pack(pady=20)

Button(win, text="Calculate", command=cal_exe).pack()
win.mainloop()
