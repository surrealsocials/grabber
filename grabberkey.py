

import keyboard
from pynput.mouse import Button, Controller
import numpy as np
import cv2
from PIL import ImageGrab
import os
import pyautogui
import time
import subprocess
from tkinter import *
import threading
import asyncio
#import win32clipboard
import shutil


root = Tk()
root.title("Grabber")
root.iconbitmap('Grabber.ico')
root.geometry("360x240")
root.wm_attributes("-topmost", 1)
name='testing'
menu = Menu(root)
root.config(menu=menu)
#selectedButton = tk.IntVar()
menubar = Menu(root,font="TkMenuFont",bg='white',fg='black')
root.configure(menu = menubar)


def opt():
	options=Canvas(root)
	options.pack(fill="both", expand=True)
	options.configure(background='white')


	

sub_menu = Menu(root,
    activebackground="red",
    activeborderwidth=1,
    activeforeground="#000000",
    background="#d9d9d9",
    borderwidth=1,
    disabledforeground="#a3a3a3",
    foreground="#000000",
    tearoff=0)

sub_menu.add_command(
   compound="left",
   label="Save")
sub_menu1 = Menu(root,
   activebackground="beige",
   activeborderwidth=1,
   activeforeground="#000000",
   background="#d9d9d9",
   borderwidth=1,
   disabledforeground="#a3a3a3",
   foreground="#000000",
   tearoff=0)
menubar.add_cascade(menu=sub_menu1,
   compound="left",
   label="Profile")
sub_menu1.add_command(
   command=opt,
   compound="left",
   label="Change Profile")
sub_menu1.add_command(
   compound="left",
   label="New Profile")
sub_menu12 = Menu(root,
   activebackground="beige",
   activeborderwidth=1,
   activeforeground="#000000",
   background="#d9d9d9",
   borderwidth=1,
   disabledforeground="#a3a3a3",
   foreground="#000000",
   tearoff=0)
menubar.add_cascade(menu=sub_menu12,
   compound="left",
   label="Automation")
sub_menu12.add_command(
   compound="left",
   label="Scripts")
sub_menu123 = Menu(root,
   activebackground="beige",
   activeborderwidth=1,
   activeforeground="#000000",
   background="#d9d9d9",
   borderwidth=1,
   disabledforeground="#a3a3a3",
   foreground="#000000",
   tearoff=0)
menubar.add_cascade(menu=sub_menu123,
   compound="left",
   label="Page")
sub_menu123.add_command(
    compound="left",
    label="Main",
    command=opt)
sub_menu123.add_command(
    compound="left",
    label="Preferences",
    command=opt)






recimg=PhotoImage(file="image/record2.png")
recoff=PhotoImage(file="image/recoff.png")
playimg=PhotoImage(file="image/playimg.png")


def grabberimg(photon):
	account=myentry.get()
	act='click'
	#zzzzos.system('start cmd /c, python grabbertxt.py')
	mouse = Controller()
	flag = 0
	photo=account


	#photon=photon+1
	photofile = ('{}''{}''{}').format(photo,act,photon)
	print (account+'/image/'+photofile+'.png')
	print("imgclick")
	filename = (account+'/image/'+photofile+'.png')             
	filename2 = (photofile+'.png')

	# Read pointer position
	print('The current pointer position is {0}'.format(mouse.position))
	x=mouse.position[0]
	y=mouse.position[1]
	x=x*1
	y=y*1
	pyautogui.moveTo(20, 500)
	time.sleep(2)

	img = ImageGrab.grab(bbox=(x-70, y-70, x+70, y+70)) #x, y, w, h
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
	cv2.imshow("frame", frame)
	cv2.imwrite(filename, frame)
	code = "fac(G,'"+filename2[:-4]+"',t)"
	codefile = open(account+'/'+account+'.txt','a')
	codefile.write(code+'\n')
	codefile.close()
	cv2.destroyAllWindows()
	time.sleep(0.1)
	mouse.position = (x, y,1)
	pyautogui.click(x,y)
	#pyautogui.click(x/150*100,y/150*100)
	cv2.destroyAllWindows()

def keypressed(data):
	account=myentry.get()
	print(account)
	print (data +' added to code')
	code = "pressk(G,'"+data+"')"
	codefile = open(account+'/'+account+'.txt','a')
	codefile.write(code+'\n')
	codefile.close()
	#pyautogui.press(data)\\

def hotkeypressed(key1,key2):
	account=myentry.get()
	print(account)
	print ('hotkey' +' added to code')
	code = "hk2(G,'"+key1+"','"+key2+"')"
	codefile = open(account+'/'+account+'.txt','a')
	codefile.write(code+'\n')
	codefile.close()
	#pyautogui.press(data)

def calltype(data):
	account=myentry.get()
	if data == None:
		pass
	else:
		print (data +' added to code')
		code = "writel(G,'"+data+"')"
		codefile = open(account+'/'+account+'.txt','a')
		codefile.write(code+'\n')
		codefile.close()
		#pyautogui.write(data)

def grabimg(x,y):
	pass

def click(x,y):
	pass


def record():
	account=myentry.get()
	print(account)
	photon=0
	print('recording')
	btnrecord.configure(image=recoff)
	stop_event = threading.Event()
	flag=0
	while flag==0:
		myentry.get()
		if keyboard.is_pressed("esc"): #returns True if "q" is pressed
			print("recording stopped")
			stop_event.set()
			flag=1
			btnrecord.configure(image=recimg)
			codefile = open(account+'/'+account+'.txt','r')
			code=codefile.read()
			print(code)
			#myclickerfile = open(account+'/myclicker.py','w')
			#myclickerfile.write(code)
			#adam	myclickerfile.close()
			codefile.close()
			#shutil.copy('image/temp/','image/'+scriptname)
			#os.rename(('image/temp','temo2'
			modulef=open(account+'/autopymodule.txt','w')
			modulef.close()
			shutil.copy('autopymodule.txt',account+'/autopymodule.py')
			modulef=open(account+'/autopymodule.txt','r')
			modulecode=modulef.read()
			modulef.close()
			codef=open(account+'/'+account+'.txt','r')
			code=codef.read()
			codef.close()
			pythonfile=open(account+'/'+account+'.py','w')
			pythonfile.write(modulecode)
			pythonfile.close()
			pythonfile=open(account+'/'+account+'.py','a')
			pythonfile.write(code)
			pythonfile.close()
			


			#break #break the while loop is "q" is pressed
		if keyboard.is_pressed("ctrl+alt+enter"): #returns True if "q" is pressed
		    print("You pressed enter")
		    key='enter'
		    time.sleep(1)
		    keypressed(key)

		if keyboard.is_pressed("ctrl+alt+shift"):
			print('grabbing image')
			photon = photon+1
			grabberimg(photon)
			txt=creds.get()
			if txt!='':
				calltype(txt)
				pyautogui.write(txt)
				creds.delete(0,END)
		if keyboard.is_pressed("ctrl+shift"): #returns True if "q" is pressed
		    print("You pressed ctrl and shift for tab")
		    key='tab'		
		    time.sleep(1)
		    pyautogui.press(key)
		    keypressed(key)
		if keyboard.is_pressed("ctrl+alt+\\"):
			print('you pressed type')
			calltype()
		if stop_event.is_set():
			#quit()
			pass





def recordstop():
	pyautogui.hotkey("ctrl","q")
	btnrecord=Button(root,
	image = recoff,
	#width=20,
	relief='flat',)
	#command=recordthread)




def recordthread():
	account=myentry.get()
	print(account)
	if account== None:
		quit()
	accountf= open('autoaccount.txt','w')
	accountf.write(account)
	accountf.close()
	os.makedirs(account, exist_ok=True)
	os.makedirs(account+'/image', exist_ok=True)

	accountf= open('autoaccount.txt','r')
	account= accountf.read()
	accountf.close()



	#filecode=pyautogui.prompt('enter name of this form to save as text file')
	#filecode=filecode+'.txt'
	codefile = open(account+'/'+account+'.txt','w')
	codefile.write(r'''


from autopymodule import USERFORM as G
import pyautogui

fac=G.findandclick
farc=G.findandrightclick
fah=G.findandhover
fan=G.findandnothing
ptf=G.presstillfound
writel=G.writedata
clickm=G.clickmouse            
pressk=G.presskey             
hk2=G.hotkeyduo      
hk3=G.hotkeytrio
at=G.alttab
pc=G.pasteclip
cc=G.copyclip
double=G.double
triple=G.triple
mm=G.movemouse
splitfac=G.splitfac

G.speed==1
t=30


#ready=pyautogui.alert('press enter when ready')
#if ready == None:
#    quit()
	    
''')
	codefile.close()
	account=str(myentry.cget("text"))

	#btnrecord.configure(image=recoff)
	if btnrecord.cget('image')=='pyimage1':


		threading.Thread(target=record).start()
		
		#btnstop=Button(root,
			#image = recoff)


myentry=Entry(root)
myentry.place(x=70, y=20, height=30, width=120)


lblkey=Label(root,
	text = 'Title:',
	font="-family {Helvetica} -size 10 -weight bold",
	justify='right',
	)
lblkey.place(x=10, y=15, height=40, width=50)

lbltxt=Label(root,
	text = 'Entry:',
	justify='right',
	)
lbltxt.place(x=10, y=60, height=40, width=50)

#account='start'
#bprint(account)

btnrecord=Button(root,
	image = recimg,
	#width=20,
	relief='flat',
	command=recordthread)
btnrecord.place(x=205, y=10, height=50, width=50)
#btnrecord.pack()

def playback():
	account = myentry.get()
	os.system('cd '+account+'&python '+account+'.py')
btnplay=Button(root,
	image = playimg,
	#width=20,
	relief='flat',
	command=playback)
btnplay.place(x=255, y=10, height=50, width=50)

creds=Entry(root)
creds.place(x=70, y=65, height=30, width=165)

fname = 'morgs'
lname = 'thompson'
bday = '12'
bmonth = 'may'
byear= '1988'

def clickselect():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.hotkey('ctrl','a',interval=0.1)
	hotkeypressed('ctrl','a')

btnselect=Button(root)
btnselect.configure(text='select')
btnselect.configure(command= clickselect)
btnselect.place(x=10, y=110, height=40, width=90)

def clickcopy():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.hotkey('ctrl','c',interval=0.1)
	hotkeypressed('ctrl','c')

btncopy=Button(root)
btncopy.configure(text='copy')
btncopy.configure(command= clickcopy)
btncopy.place(x=110, y=110, height=40, width=90)

def clickpaste():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.hotkey('ctrl','v',interval=0.1)
	hotkeypressed('ctrl','v')

btnpaste=Button(root)
btnpaste.configure(text='paste')
btnpaste.configure(command= clickpaste)
btnpaste.place(x=210, y=110, height=40, width=90)

def clickenter():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.press('enter')
	keypressed('enter')

btnenter=Button(root)
btnenter.configure(text='enter')
btnenter.configure(command= clickenter)
btnenter.place(x=10, y=160, height=40, width=90)

def clicktab():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.press('tab')
	keypressed('tab')


btntab=Button(root)
btntab.configure(text='tab')
btntab.configure(command= clicktab)
btntab.place(x=110, y=160, height=40, width=90)

def clickdelete():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.press('delete')
	keypressed('delete')

btndelete=Button(root)
btndelete.configure(text='delete')
btndelete.configure(command= clickdelete)
btndelete.place(x=210, y=160, height=40, width=90)

def clickpup():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.press('pagegup')
	keypressed('pagegup')

btnup=Button(root)
btnup.configure(text='^')
btnup.configure(command= clickpup)
btnup.place(x=310, y=110, height=40, width=20)

def clickpdown():
	pyautogui.hotkey('alt','tab',interval=0.1)
	pyautogui.press('pagedown')
	keypressed('pagedown')

btndown=Button(root)
btndown.configure(text='v')
btndown.configure(command= clickpdown)
btndown.place(x=310, y=160, height=40, width=20)

def clear():
	creds.delete(0,END)
btnclear=Button(root)
btnclear.configure(text='x')
btnclear.configure(command= clear)
btnclear.configure(foreground= 'red')
btnclear.configure(font="-family {Helvetica} -size 9 -weight bold")
btnclear.place(x=270, y=65, height=30, width=30)




btndc=Checkbutton(root)
btndc.configure(text='DC')
btndc.configure(font="-family {Helvetica} -size 8")
btndc.place(x=300, y=75, height=30, width=60)



class canv():


	def __init__(self,main=None):
		self.main=main
		self.main=Canvas(root)
		self.main.pack(fill="both", expand=True)
		self.main.configure(background='white')
		self.fill=True

		self.close=Button(self.main)
		self.close.configure(text='x')
		self.close.configure(command= self.closer)
		self.close.configure(font="-family {Helvetica} -size 10 -weight bold")
		self.close.place(x=238, y=65, height=30, width=30)

	def closer(self):
		self.main.destroy()

def settingsopen():
	
	set=canv('settings')
	




def insert():
	txt=creds.get()
	if txt!='':
		calltype(txt)
		pyautogui.hotkey('alt','tab')
		pyautogui.write(txt)
		creds.delete(0,END)
btninsert=Button(root)
btninsert.configure(text='>')
btninsert.configure(command= insert)
btninsert.configure(font="-family {Helvetica} -size 10 -weight bold")
btninsert.place(x=238, y=65, height=30, width=30)
menubar.add_cascade(menu=sub_menu,
   compound="left",
   label="File")
sub_menu.add_command(
   compound="left",
   label="Load",
   command=settingsopen)



'''
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print (data)

		self.main=main
		self.main = Tk()
		self.main.title("Grabber")
		self.main.iconbitmap('Grabber.ico')
		self.main.geometry("360x240")
		self.main.wm_attributes("-topmost", 1)
		self.name='mainlite'

		self.framer=Tk.frame(self.main)

		self.close=Button(self.main)
		self.close.configure(text='>')
		self.close.configure(command= self.closer)
		self.close.configure(font="-family {Helvetica} -size 10 -weight bold")
		self.close.place(x=238, y=65, height=30, width=30)
'''	
root.mainloop()

 


					
										
