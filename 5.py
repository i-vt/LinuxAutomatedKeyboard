#Works on Python 3.10.6, pynput Version: 1.7.6

import time
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()


#seconds

intKeyAcrc = 92 + random.randrange(4) # 92/100 letters will be typed accurately, 8% will be deleted & retyped
intPermaError = 0 + random.randrange(0)#0/1000 letters will be permanently incorrect
intClickSpeed = 350 + random.randrange(40) # characters per minute (median is 187 for average human)
#1000 = 681-478 characters a minute
#500 = 330-262 character a minute
#350 = 246 - 187 charcters a minute
intVar = 5+random.randrange(55) # 10% variation for accuracy & CPM


def plsDelay():
	intVariation1 = intClickSpeed*intVar
	intRandom1 = random.randint(-1*intVariation1, intVariation1)/100
	time.sleep(30/(intClickSpeed+intRandom1))
	#time.sleep(1)
def plsPress(objPassed):
	plsDelay()
	keyboard.press(objPassed)


def plsRelease(objPassed):
	plsDelay()
	keyboard.release(objPassed)


def plsPressKey(strPassed):
	plsPress(strPassed)
	plsRelease(strPassed)

def plsShiftPK(strPassed):
	plsPress(Key.shift)
	plsPressKey(strPassed)
	plsRelease(Key.shift)
strAll = "qwertyuiopasdfghjklzxcvbnm`1234567890-=[]\\;',./"
def plsMakeAndFixTypo():
	strRandom1 = strAll[random.randint(0,len(strAll)-1)]
	plsPressKey(strRandom1)
	plsDelay()
	plsPressKey(Key.backspace)
	
def plsMakeATypo():
	strRandom1 = strAll[random.randint(0,len(strAll)-1)]
	plsPressKey(strRandom1)


def plsType(strPassed):
	strSC = "~!@#$%^&*()_+{}|:\"<>?" # shift chacater
	strNSC = "`1234567890-=[]\\;',./" #No shift character
	strCap = "QWERTYUIOPASDFGHJKLZXCVBNM"
	strSpecial = "\n\t"
	for int1 in range(len(strPassed)):
		#print(strTypeThis[int1])
		str1 = strPassed[int1]
		#turns upper case into a click
		if random.randint(0,100) > intKeyAcrc: plsMakeAndFixTypo()
		if random.randint(0,1000) > (1000 - intPermaError): plsMakeATypo()
		if str1.isupper():
			plsShiftPK(str1.lower())
		elif str1 in strSC:
			int1 = strSC.index(str1)
			str2 = strNSC[int1]
			plsShiftPK(str2)
		elif str1 in strSpecial:
			if str1 == "\n": plsPressKey(Key.enter)
			if str1 == "\t": plsPressKey(Key.tab)
		else:
			plsPressKey(str1)	

def plsParseFile(strPassed):
	openFile = open(strPassed, "r")
	strReturn = ""
	for objLine in openFile:
		strReturn += objLine
	return strReturn



str1 = plsParseFile("index.html")
time.sleep(intDelayBeforeTyping)
plsType(str1)



#time.sleep(99999)

