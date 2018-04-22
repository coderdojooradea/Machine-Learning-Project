from picamera import PiCamera
import time
import sys
import os
BASENAME='image'
BASEEXT='.jpg'
WIDTH=300
HEIGHT=300
def InWord(haysack,needle):
	if haysack.find(needle)!=-1:
		return True
	return False
def FilterByWord(ls,word):
	ret=[]
	for i in ls:
		if InWord(i,word):
			ret.append(i)
	return ret
def ExtractNumber(word):
	num=0
	ret=0
	while word[num].isdigit()==False:
		num+=1
	while word[num].isdigit()==True:
		ret=ret*10+int(word[num])
		num+=1
	return ret
if len(sys.argv)<2:
	print('Error Please Give An Argument')
	sys.exit()
camera=PiCamera()
camera.color_effects = (128,128)
camera.resolution=(WIDTH,HEIGHT)
num=int(sys.argv[1])
path=str(sys.argv[2])
filepaths=os.listdir(path)
filepaths=FilterByWord(filepaths,BASEEXT)
filepaths=FilterByWord(filepaths,BASENAME)
filenums=[]
for f in filepaths:
	filenums.append(ExtractNumber(f))
filenums.sort()
basenum=0
if len(filenums)>0:
	basenum=filenums[len(filenums)-1]
basenum+=1
for i in range(0,num):
	camera.capture(path+BASENAME+str(i+basenum)+BASEEXT)
	print('Saved as '+path+BASENAME+str(i+basenum)+BASEEXT)
	time.sleep(0.2)

