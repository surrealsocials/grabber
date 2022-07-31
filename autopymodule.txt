#autopymodule.py
import pyautogui
import time
import pyscreeze
import pymsgbox
import pytweening
from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)

#set speed for form (1 is fastest)
global speed

speed=0.5


class USERFORM:

	#init#
	speed=5
	def __init__(self,fname,lname,byear,speed):
		self.fname=fname
		self.lname=lname
		self.byear=byear
		self.speed=speed
		speed=2
      
	#finding pictures


	def findandclick(self,imagefile,maxloops):
		self.imagefile=imagefile
		self.maxloops=maxloops
		imagefile = 'image/'+imagefile+'.png'
		flag = 0
		loopc= 0
		while flag == 0:
			print('looking for '+imagefile)
			if pyautogui.locateOnScreen(imagefile,confidence=0.7) == None:
				loopc=loopc+1
				if loopc == maxloops:
					flag=1
			else:
				buttonNextlocation = pyautogui.locateOnScreen(imagefile,confidence=0.7)
				print(Style.BRIGHT + Back.GREEN + Fore.WHITE+'located '+imagefile)
				flag=1
				buttonx, buttony = pyautogui.center(buttonNextlocation)
				pyautogui.click(buttonx, buttony)



	def findandclickold(self,imagefile,maxloops):
		self.imagefile=imagefile
		self.maxloops=maxloops
		pyautogui.moveTo(100,500)
		backupneeded=''
		backup=''
		backupfile=''
		imagefile = 'image/'+imagefile+'.png'
		flag = 0
		loopc= 0
		while flag == 0:
			print('looking for '+imagefile)
			if pyautogui.locateOnScreen(imagefile,confidence=0.7) == None:
				loopc=loopc+1
				
				if loopc == maxloops:
					flag=1
					#pyautogui.alert('click enter to find '+self.imagefile+' yourself?')
				if loopc==5:
					backupneeded=imagefile
					#backup= pyautogui.prompt('cant find '+imagefile+ '. add a backup image name or click enter to keep trying?')
					if backup ==None or backup=='':
						print('hi')
					else:
						backupfile= 'image/'+backup+'.png'
						imagefile=backupfile
						print(Style.BRIGHT + Back.BLUE + Fore.WHITE+'trying '+imagefile)

			else:
				time.sleep(0.5)
				buttonNextlocation = pyautogui.locateOnScreen(imagefile,confidence=0.7)
				print(Style.BRIGHT + Back.GREEN + Fore.WHITE+'located '+imagefile)
				buttonx, buttony = pyautogui.center(buttonNextlocation)
				pyautogui.click(buttonx, buttony)
				flag=(1)
				time.sleep(speed)

		if backupneeded == imagefile:
			print('backup file needed for '+backupneeded+'.png')

	def findandrightclick(self,imagefile,maxloops):
		self.imagefile=imagefile
		self.maxloops=maxloops
		pyautogui.moveTo(0,500)
		backupneeded=''
		backup=''
		backupfile=''
		imagefile = 'image/'+imagefile+'.png'
		flag = 0
		loopc= 0
		while flag == 0:
			print('looking for '+imagefile)
			if pyautogui.locateOnScreen(imagefile,confidence=0.7) == None:
				loopc=loopc+1
				
				if loopc == maxloops:
					flag=1
					pyautogui.alert('click enter to find '+self.imagefile+' yourself?')
				if loopc==5:
					backupneeded=imagefile
					#backup= pyautogui.prompt('cant find '+imagefile+ '. add a backup image name or click enter to keep trying?')
					if backup ==None or backup=='':
						print('hi')
					else:
						backupfile= 'image/'+backup+'.png'
						imagefile=backupfile
						print(Style.BRIGHT + Back.BLUE + Fore.WHITE+'trying '+imagefile)


			else:
				buttonNextlocation = pyautogui.locateOnScreen(imagefile,confidence=0.7)
				print(Style.BRIGHT + Back.GREEN + Fore.WHITE+'located '+imagefile)
				buttonx, buttony = pyautogui.center(buttonNextlocation)
				pyautogui.rightClick(buttonx, buttony)
				flag=(1)
				time.sleep(speed)

		if backupneeded == imagefile:
			print('backup file needed for '+backupneeded+'.png')

	def findandhover(self,imagefile,onclickimg,maxloops):
		self.onclickimg=onclickimg
		onclickimg='image/'+onclickimg+'.png'
		self.imagefile=imagefile
		self.maxloops=maxloops
		backupneeded=''
		backup=''
		imagefile = 'image/'+imagefile+'.png'
		flag = 0
		loopc= 0
		while flag == 0:
			if pyautogui.locateOnScreen(imagefile,confidence=0.7) == None:
				print('looking for '+imagefile)
				loopc=loopc+1
				if loopc==5:
				    pyautogui.alert('cant find '+imagefile+' try getting new snip')
				if loopc==maxloops:
				    flag=1
				    pyautogui.alert('do it yourself')
			else:
				buttonNextlocation = pyautogui.locateOnScreen(imagefile,confidence=0.7)
				print('located '+imagefile)
				buttonx, buttony = pyautogui.center(buttonNextlocation)
				pyautogui.moveTo(buttonx, buttony)
				flag=1
				#time.sleep(speed)
				
				if onclickimg != '':
					buttonNextlocation = pyautogui.locateOnScreen(onclickimg,confidence=0.7)
					print(Style.BRIGHT + Back.GREEN + Fore.WHITE+'located '+ onclickimg)
					buttonx, buttony = pyautogui.center(buttonNextlocation)
					pyautogui.click(buttonx, buttony)
					#time.sleep(speed)
					
                
	def findandnothing(self,imagefile,maxloops):
		self.maxloops=maxloops
		self.imagefile=imagefile
		imagefile = 'image/'+imagefile+'.png'
		flag = 0
		loopc=0
		while flag == 0:
		    if pyautogui.locateOnScreen(imagefile,confidence=0.7) == None:
		        print('looking for '+imagefile)
		        loopc=loopc+1
		        if loopc==5:
		        		pass
		            #pyautogui.alert('cant find '+imagefile+' try getting new snip')
		        if loopc==maxloops:
		            flag=1
		            pyautogui.alert('do it yourself')

		    else:
		        print('located '+imagefile)
		        flag=1
		        time.sleep(speed)

	def presstillfound(self,key,imagefile,maxloops):
		self.key=key
		self.maxloops=maxloops
		self.imagefile=imagefile
		flag=0
		loopc=0
		while flag == 0:
		    if pyautogui.locateOnScreen(imagefile,confidence=0.7) == None:
		        print('looking for '+imagefile)
		        pyautogui.presskey(key)
		        loopc=loopc+1
		        if loopc==5:
		            pyautogui.alert('cant find '+imagefile+' try getting new snip')
		        if loopc==maxloops:
		            flag=1
		            pyautogui.alert('do it yourself')
		    else:
		        buttonNextlocation = pyautogui.locateOnScreen(imagefile,confidence=0.7)
		        print('located '+imagefile)
		        buttonx, buttony = pyautogui.center(buttonNextlocation)
		        pyautogui.click(buttonx, buttony)
		        flag=(1)
		        time.sleep(self.speed)

	#keys

	def writedata(self,writedata):
	    print('writing line')
	    self.writedata=writedata
	    pyautogui.write(writedata)
	    time.sleep(speed)
           
	def presskey(self,keyselect):
	    print('pressing key')
	    self.keyselect=keyselect
	    pyautogui.press(keyselect)
	    time.sleep(speed)
	      
	def hotkeyduo(self,k1,k2):
	    print('hot key duo')
	    k1=k1
	    k2=k2
	    kgroup=k1+','+k2
	    pyautogui.hotkey(k1,k2)
	    time.sleep(speed)
   	    
	def hotkeytrio(self,k1,k2,k3):
	    print('hot key trio')
	    self.k1=k1
	    self.k2=k2
	    self.k3=k3
	    kgroup=k1+','+k2+','+k3
	    pyautogui.hotkey(kgroup)
	    time.sleep(speed)
	    
	def alttab(self):
	    pyautogui.hotkey ('alt', 'tab', interval=0.1)
	    time.sleep(speed)
    #clipboard
	def pasteclip(self):
	    print('pasting')
	    pyautogui.hotkey ('ctrl', 'v', interval=0.1)
	    time.sleep(speed)
	
	def copyclip(self):
	    print('copying')
	    pyautogui.hotkey ('ctrl', 'c', interval=0.1)
	    time.sleep(speed)
	#mouses
	def clickmouse(self):
		print('clicking mouse')
		pyautogui.click()
		time.sleep(speed)
	def movemouse(self,x,y):
		print('moving mouse')
		self.x=x
		self.y=y
		pyautogui.move(x, y) 
		time.sleep(speed)
	#decisions
	def double(self):
		print('doubleclicking')
		pyautogui.doubleClick()
		time.sleep(speed)
	def triple(self):
		print('tripleclicking')
		pyautogui.tripleClick()
		time.sleep(speed)
	def splitfac(self,imageA,imageB,maxloops):
		print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "SPLIT")
		self.imageA=imageA
		self.imageB=imageB
		self.maxloops=maxloops
		imageA = 'image/'+imageA+'.png'
		imageB= 'image/'+imageB+'.png'
		flag=0
		loopc=0
		while flag==0:
			if pyautogui.locateOnScreen(imageA,confidence=0.7) != None:
				flag = 1
				self.findandclick(self,self.imageA,self.maxloops)          
			else:
				if pyautogui.locateOnScreen(imageB,confidence=0.7) != None:
					flag = 1
					self.findandclick(self,self.imageB,self.maxloops)
				else:
					print(Style.BRIGHT + Back.YELLOW+ Fore.WHITE + self.imageA + ' and '+self.imageB +' could not be found')
					loopc=loopc+1
					if loopc==self.maxloops:
						flag=1
						print(Style.BRIGHT + Back.RED + Fore.WHITE +'CANT FIND EITHER')
						pyautogui.alert('starting next command')
                        
USERFORM.speed==1
#############create instance
fac=USERFORM.findandclick
farc=USERFORM.findandrightclick
fah=USERFORM.findandhover
fan=USERFORM.findandnothing
ptf=USERFORM.presstillfound
writel=USERFORM.writedata
clickm=USERFORM.clickmouse            
pressk=USERFORM.presskey             
hk2=USERFORM.hotkeyduo      
hk3=USERFORM.hotkeytrio
at=USERFORM.alttab
pc=USERFORM.pasteclip
cc=USERFORM.copyclip
triple=USERFORM.triple
mm=USERFORM.movemouse
splitfac=USERFORM.splitfac


