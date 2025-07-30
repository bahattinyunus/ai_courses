



grafik={
        'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':[],
        'F':[],
        }

ziyaret=[]
yıgın=[]

def bfs(ziyaret,grafik,dügüm):
    ziyaret.append(dügüm)
    yıgın.append(dügüm)
    
    while yıgın:
        s=yıgın.pop(0)
        print(s,end=" ")
        
        for komsu in grafik[s]:
            if komsu not in ziyaret:
                yıgın.append(komsu)
                
            
            
bfs(ziyaret,grafik,'A')