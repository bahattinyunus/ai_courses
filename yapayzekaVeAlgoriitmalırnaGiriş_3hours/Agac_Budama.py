



agac=[[[5,1,2], [8,-8,-9]],[[9,4,5], [-3,4,3]]]
kok=0
budama=0

def cocuklar(dal,derinlik,alfa,beta):
    global agac
    global kok
    global budama
    i=0
    for cocuk in dal:
        if type(cocuk) is list:
            (nalfa,nbeta)=cocuklar(cocuk,derinlik+1,alfa,beta)
            if derinlik%2==1:
                beta=nalfa if nalfa<beta else beta
            else:
                alfa=nbeta if nbeta>alfa else alfa
                dal[i]=alfa if derinlik%2==0 else beta
                i += 1
        else:
            if derinlik%2==0 and alfa<cocuk:
                alfa=cocuk
            if derinlik%2==1 and beta>cocuk:
                beta=cocuk
            if alfa>=beta:
                budama+=1
                break
    if derinlik==kok:
        agac=alfa if kok==0 else beta
    return (alfa,beta)
def alfabeta(in_agac=agac,baslangıc=kok,alt=-15,ust=15):
    global agac
    global budama
    global kok
    (alfa,beta)=cocuklar(agac,baslangıc,alt,ust)
    if __name__ == "__main__":
        print ("(alfa, beta):",alfa,beta)
        print ("Sonuc: ",agac)
        print ("Budama Sayısı:",budama)
    return (alfa,beta,budama,agac)
if __name__ == "__main__":
    alfabeta(None)