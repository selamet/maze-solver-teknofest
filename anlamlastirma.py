import sys
sys.setrecursionlimit(1500)
liste=[]
f=open("cozum.txt", "r")
satirlar=f.readlines()
for satir in satirlar:
    liste.append(satir)
f.close()
ttc=()
hepsi=[]
satir=[]
sutun=[]
sayac=0
ilk_elm=liste[0][0]
for x in liste:
    satir=x.partition(" ")
    if satir[0] != ilk_elm:
        ttc=tuple(sutun)
        hepsi.append(ttc)
        sutun.clear()
        ilk_elm=satir[0]
        sayac+=1
    if satir[0]==ilk_elm:
        satir=satir[2].partition("\n")
        sutun.append(satir[0])
print("Veriler Listelendi")
ilk=hepsi[0][0]
son=hepsi[0][len(hepsi[0])-1]
sinir=int(son)-int(ilk)+1
print("Yol genişliği: ", sinir)
ileri=0
yol=[]
ddog='g'
ydog='l'
don=""
def anlam(x,k):
    global ileri
    global ddog
    global ydog
    global yol
    global don
    global donus
    global basl
    global ilk
    global son
    global yatay_ust
    global yatay_alt
    global xg
    if hepsi[x].count(ilk)>0 and hepsi[x].count(son)>0:
        ileri+=1
        if x>=len(hepsi)-1:
            yol.append(ileri)
            return 1
        if hepsi[x].count(str(int(ilk)-1))>0 and hepsi[x].count(str(int(son)+1))<1:
            donus=-1
            ydog='b'
            if ddog=='g':
                don="sağ"
            elif ddog=='k':
                don="sol"
            basl=int(son)
        elif hepsi[x].count(str(int(ilk)-1))<1 and hepsi[x].count(str(int(son)+1))>0:
            donus=+1
            ydog='d'
            if ddog=='g':
                don="sol"
            elif ddog=='k':
                don="sağ"
            basl=int(ilk)
        if k==1:
            x+=1
            yatay_ust=x-1
            yatay_alt=yatay_ust-9
        elif k==0:
            x-=1
            yatay_alt=x+1
            yatay_ust=yatay_alt+9
        return anlam(x,k)
    else:
        yol.append(ileri)
        if don=="sol":
            yol.append("Sol")
        elif don=="sağ":
            yol.append("Sağ")
        ileri=0
        while hepsi[yatay_alt].count(str(basl)) and hepsi[yatay_ust].count(str(basl)):
            if ydog=='b':
                basl-=1
            elif ydog=='d':
                basl+=1
            ileri+=1
        else:
            if ydog=='b':
                basl+=1
                ilk=str(basl)
                son=str(int(ilk)+9)
            elif ydog=='d':
                basl-=1
                son=str(basl)
                ilk=str(int(son)-9)
            yol.append(ileri)
            if hepsi[yatay_alt-1].count(str(basl)):
                donus=-1
                ddog='k'
                k=0
                xg=yatay_ust
                if ydog=='b':
                    don="sağ"
                elif ydog=='d':
                    don="sol"
            elif hepsi[yatay_ust+1].count(str(basl)):
                donus=+1
                ddog='g'
                k=1
                xg=yatay_alt
                if ydog=='b':
                    don="sol"
                elif ydog=='d':
                    don="sağ"
            if don=="sol":
                yol.append("Sol")
            elif don=="sağ":
                yol.append("Sağ")
            ileri=0
            if x>=len(hepsi):
                return 1
            return anlam(xg,k)
anlam(0,1)
print(yol)
print("Son")
