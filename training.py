import os
import cv2
import codecs
import sys

argv={}
for d in range(1,len(sys.argv)):
	d=d.split("=")
	argv[d[0]]=d[1]


POS_NAME="p"
if 'WIDTH' in argv:
	POS_WIDTH=argv["WIDTH"]
else:
	POS_WIDTH=50

if 'HEIGHT' in argv:
	POS_HEIGHT=argv["HEIGHT"]
else:
	POS_HEIGHT=50

NEG_NAME="n"

if 'NUMSTAGES' in argv:
	NUMSTAGES=argv["NUMSTAGES"]
else:
	NUMSTAGES=20

if 'METHOD' in argv:
	METHOD=argv["METHOD"]
else:
	METHOD="HAAR" #HAAR, LBP


OUT_TEXT=""
POS_NUM=0
for f in os.listdir(POS_NAME):
	NFL=POS_NAME+"/"+str("%05d"%(POS_NUM))+".png"
	os.rename(POS_NAME+"/"+f, NFL)
	img=cv2.imread(NFL)
	img=cv2.resize(img, (POS_WIDTH,POS_HEIGHT))
	cv2.imwrite(NFL,img)
	print(NFL)
	OUT_TEXT+=POS_NAME+"/"+f+" 1 0 0 "+str(img.shape[1])+" "+str(img.shape[0])+"\n"
	POS_NUM+=1

f=codecs.open(POS_NAME+".txt","w")
f.write(OUT_TEXT)
f.close()

OUT_TEXT=""
NEG_NUM=0
for f in os.listdir(NEG_NAME):
	NFL=NEG_NAME+"/"+str("%05d"%(NEG_NUM))+".png"
	os.rename(NEG_NAME+"/"+f, NFL)
	print(NFL)
	OUT_TEXT+=NFL+"\n"
	NEG_NUM+=1

f=codecs.open(NEG_NAME+".txt","w")
f.write(OUT_TEXT)
f.close()


print("===opencv_createsamples===")
opencv_createsamples="opencv_createsamples.exe"
opencv_createsamples+=" -info "+POS_NAME+".txt -vec "+POS_NAME+".vec -bg "+NEG_NAME+".txt -num "+str(POS_NUM)
opencv_createsamples+=" -w "+str(POS_WIDTH)+" -h "+str(POS_HEIGHT)
os.system(opencv_createsamples)

print("===opencv_traincascade===")
opencv_traincascade="opencv_traincascade.exe"
opencv_traincascade+=" -data xml -vec "+POS_NAME+".vec -bg "+NEG_NAME+".txt -numPos "+str(POS_NUM)
opencv_traincascade+=" -numNeg "+str(NEG_NUM)+" -numStages "+str(NUMSTAGES)
opencv_traincascade+=" -featureType "+METHOD
opencv_traincascade+=" -w "+str(POS_WIDTH)+" -h "+str(POS_HEIGHT)
opencv_traincascade+=" -precalcValBufSize 4096 -precalcIdxBufSize 4096 -numThreads 12 -maxFalseAlarmRate 0.5 -minHitRate 0.995000 -maxFalseAlarmRate 0.500000 -weightTrimRate 0.950000 -maxDepth 1 -maxWeakCount 100 -haarFeatureMode BASIC9"
os.system(opencv_traincascade)

