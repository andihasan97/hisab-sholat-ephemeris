print("       PROGRAM WAKTU SHOLAT ACCURATE HASANI 1.0.2       ")
print("             SISTEM EPHEMERIS HISAB RUKYAH")
print(" ")
print("           diprogram oleh: Andi Hasan Ashari   ")
print(" ")
print("              PYTHON PROGRAMMING LANGUAGE")
print(" ")
print("Masukkan Data dibawah ini ")
print(" ")
HR=input('Hari= ')
TGL=input('Tanggal= ')
BLN=input('Bulan= ')
TH=input('Tahun= ')
import math
from datetime import datetime
now=datetime.now()
#Lintang Tempat dr,mnt,dtk
J=-7
M=-26
D=-0
#Bujur Tempat dr,mnt,dtk
B1=111
B2=26
B3=0
print(" ")
print("Deklinasi")
DK1=float(input('derajat= '))
DK2=float(input('menit= '))
DK3=float(input('detik= '))
print(" ")
#Equation of time
print("Equation of Time")
EQ1=float(input('derajat= '))
EQ2=float(input('menit= '))
EQ3=float(input('detik= '))
print(" ")
TT=float(input('Tinggi Tempat= '))
TZ=float(input('Time Zone= '))
print(" ")
#WIB=105,WITA=120,WIT=135
TZ1=[105,120,135]
TZ2=["WIB","WITA","WIT"]
#LINTANG X
if J<0 :
    X=-1*(abs((J)+M/60+D/3600))
else : 
    X=J+M/60+D/3600
#BUJUR Y
if B1<0 :
    Y=-1*(abs((B1)+B2/60+B3/3600))
else :
    Y=B1+B2/60+B3/3600
#DEKLINASI DKL
if DK1<0 :
    DKL=-1*(abs((DK1)+DK2/60+DK3/3600))
else :
    DKL=DK1+DK2/60+DK3/3600
#EQUATION OF TIME E
if EQ1<0 :
    E=-1*(abs((EQ1)+EQ2/60+EQ3/3600))
else :
    E=EQ1+EQ2/60+EQ3/3600
#Kerendahan Ufuk KU
KU = (1.76/60)*math.sqrt(TT)
#REFRAKSI REF
REF=0.575
#Semi Diameter SD
SD=0.2666666666667
#Meridian Pass MP
MP=12-(E)
#tz 105 120 135
if TZ==7 :
    tz=TZ1[0]
elif TZ==8 :
    tz=TZ1[1]
elif TZ==9 :
    tz=TZ1[2]
else :
    print("Ada yang Salah!")
#t wib wita wit
if TZ==7 :
    t=TZ2[0]
elif TZ==8 :
    t=TZ2[1]
elif TZ==9 :
    t=TZ2[2]
else :
    print("Ada yang Salah!")
#Koreksi Waktu Daerah KWD
KWD=abs((tz-Y)/15)
#Mencari Tinggi Matahari
#Ashar
ZM=abs(X-DKL)
#HOA Ketinggian Matahari Ashar
HOA=math.degrees(math.atan(1/(math.tan(math.radians(ZM))+1)))
#HOM Ketinggian Matahari Maghrib
HOM=-(REF+SD+KU)
#HOI Ketinggian Matahari Isya'
HOI=-17+HOM
#HOS Ketinggian Matahari Shubuh
HOS=-19+HOM
#HOT Ketinggian Matahari Thulu'
#HOT=TOM
#HOD Ketinggian Matahari Dluha
HOD=4.5
#MENCARI AWAL WAKTU SHOLAT
#Dhuhur
DHWIB=MP-KWD+(2/60)
DH1=int(DHWIB)
DH2=(DHWIB-DH1)*60
DH3=int(DH2)
DH4=(DH2-DH3)*60
#round(x,2) untuk mengambil 2 angka dibelakang koma
DH5=round(DH4,2)
#WIS
DHWIS=DHWIB+E+KWD
DH6=int(DHWIS)
DH7=(DHWIS-DH6)*60
DH8=int(DH7)
DH9=(DH7-DH8)*60
DH10=int(DH9)
#Ashar
#TOA Rumus Sudut Waktu Ashar
TOA=math.degrees(math.acos(((math.sin(math.radians(HOA))/math.cos(math.radians(X)))/math.cos(math.radians(DKL)))-math.tan(math.radians(X))*math.tan(math.radians(DKL))))/15
ASWIB=TOA+MP-KWD+(2/60)
AS1=int(ASWIB)
AS2=(ASWIB-AS1)*60
AS3=int(AS2)
AS4=(AS2-AS3)*60
AS5=round(AS4,2)
#Ashar WIS
ASWIS=ASWIB+E+KWD
AS6=int(ASWIS)
AS7=(ASWIS-AS6)*60
AS8=int(AS7)
AS9=(AS7-AS8)*60
AS10=round(AS9,2)
#TOM Sudut Waktu Maghrib
TOM=math.degrees(math.acos(((math.sin(math.radians(HOM))/math.cos(math.radians(X)))/math.cos(math.radians(DKL)))-math.tan(math.radians(X))*math.tan(math.radians(DKL))))/15
MWIB=TOM+MP-KWD+(2/60)
M1=int(MWIB)
M2=(MWIB-M1)*60
M3=int(M2)
M4=(M2-M3)*60
M5=round(M4,2)
#Maghrib WIS
MWIS=MWIB+E+KWD
M6=int(MWIS)
M7=(MWIS-M6)*60
M8=int(M7)
M9=(M7-M8)*60
M10=round(M9,2)
#TOI Sudut Waktu Isya'
TOI=math.degrees(math.acos(((math.sin(math.radians(HOI))/math.cos(math.radians(X)))/math.cos(math.radians(DKL)))-math.tan(math.radians(X))*math.tan(math.radians(DKL))))/15
IWIB=TOI+MP-KWD+(2/60)
I1=int(IWIB)
I2=(IWIB-I1)*60
I3=int(I2)
I4=(I2-I3)*60
I5=round(I4,2)
#Isya' WIS
IWIS=IWIB+E+KWD
I6=int(IWIS)
I7=(IWIS-I6)*60
I8=int(I7)
I9=(I7-I8)*60
I10=round(I9,2)
#TOS Sudut Waktu Shubuh
TOS=math.degrees(math.acos(((math.sin(math.radians(HOS))/math.cos(math.radians(X)))/math.cos(math.radians(DKL)))-math.tan(math.radians(X))*math.tan(math.radians(DKL))))/15
SWIB=MP-TOS-KWD+(2/60)
S1=int(SWIB)
S2=(SWIB-S1)*60
S3=int(S2)
S4=(S2-S3)*60
S5=round(S4,2)
#Shubuh WIS
SWIS=SWIB+E+KWD
S6=int(SWIS)
S7=(SWIS-S6)*60
S8=int(S7)
S9=(S7-S8)*60
S10=round(S9,2)
#TU Sudut Waktu Thulu'/Terbit
TUWIB=MP-TOM-KWD-(2/60)
TU1=int(TUWIB)
TU2=(TUWIB-TU1)*60
TU3=int(TU2)
TU4=(TU2-TU3)*60
TU5=round(TU4,2)
#Terbit WIS
TUWIS=TUWIB+E+KWD
TU6=int(TUWIS)
TU7=(TUWIS-TU6)*60
TU8=int(TU7)
TU9=(TU7-TU8)*60
TU10=round(TU9,2)
#TODL Sudut Waktu Dluha
TODL=math.degrees(math.acos(((math.sin(math.radians(HOD))/math.cos(math.radians(X)))/math.cos(math.radians(DKL)))-math.tan(math.radians(X))*math.tan(math.radians(DKL))))/15
DLWIB=MP-TODL-KWD+(2/60)
DL1=int(DLWIB)
DL2=(DLWIB-DL1)*60
DL3=int(DL2)
DL4=(DL2-DL3)*60
DL5=round(DL4,2)
#Dluha WIS
DLWIS=DLWIB+E+KWD
DL6=int(DLWIS)
DL7=(DLWIS-DL6)*60
DL8=int(DL7)
DL9=(DL7-DL8)*60
DL10=round(DL9,2)
#Tengah Malam
TM=((SWIB+24)-MWIB)/2+MWIB-(2/60)
TM1=int(TM)
TM2=(TM-TM1)*60
TM3=int(TM2)
TM4=(TM2-TM3)*60
TM5=round(TM4,2)
#Tengah Malam WIS
TMWIS=TM+E+KWD
TM6=int(TMWIS)
TM7=(TMWIS-TM6)*60
TM8=int(TM7)
TM9=(TM7-TM8)*60
TM10=round(TM9,2)
#1/3 Malam terakhir
SP=((24+SWIB-MWIB)/3)*2+MWIB-(4/60)-24
SP1=int(SP)
SP2=(SP-SP1)*60
SP3=int(SP2)
SP4=(SP2-SP3)*60
SP5=round(SP4,2)
#1/3 Malam terakhir WIS
SPWIS=SP+E+KWD
SP6=int(SPWIS)
SP7=(SPWIS-SP6)*60
SP8=int(SP7)
SP9=(SP7-SP8)*60
SP10=round(SP9,2)

print("_______________________________________________________")
print(" ")
print("         HASIL HISAB pada ",HR,",",TGL,BLN,TH)
print(" ")
print("               untuk Wilayah Kota Ngawi")
print("  LT",J,"°",M,"'",D,'"',"~","BT",B1,"°",B2,"'",B3,'"',"TT",TT,"mdpl")
print(" ")
print(" ")
print("Dhuhur = ",DH1,":",DH3,":",DH5,t,"   ",DH6,":",DH8,":",DH10,"WIS")
print(" ")
print("Ashar  = ",AS1,":",AS3,":",AS5,t,"  ",AS6,":",AS8,":",AS10,"WIS")
print(" ")
print("Maghrib= ",M1,":",M3,":",M5,t,"  ",M6,":",M8,":",M10,"WIS")
print(" ")
print("Isya'  = ",I1,":",I3,":",I5,t,"  ",I6,":",I8,":",I10,"WIS")
print(" ")
print("Shubuh = ",S1,":",S3,":",S5,t,"   ",S6,":",S8,":",S10,"WIS")
print(" ")
print("Terbit = ",TU1,":",TU3,":",TU5,t,"   ",TU6,":",TU8,":",TU10,"WIS")
print(" ")
print("Dluha  = ",DL1,":",DL3,":",DL5,t,"   ",DL6,":",DL8,":",DL10,"WIS")
print(" ")
print("T.Malam= ",TM1,":",TM3,":",TM5,t,"   ",TM6,":",TM8,":",TM10,"WIS")
print(" ")
print("1/3 Mlm.T=",SP1,":",SP3,":",SP5,t,"   ",SP6,":",SP8,":",SP10,"WIS")
print(" ")
print("  dihisab & diprogram oleh:")
print("      Andi Hasan Ashari")
print("      LF PCNU Kab. Ngawi")
print(" ")
print("dihisab pada",now)