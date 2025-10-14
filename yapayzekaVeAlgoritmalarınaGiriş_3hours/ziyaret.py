# Graf yapısı - her düğümün komşularını liste halinde tutar
# Bu örnekte A'dan başlayarak BFS algoritması uygulanacak
grafik={
    'A':['B','C'],  # A düğümünün komşuları B ve C
    'B':['D','E'],  # B düğümünün komşuları D ve E
    'C':['F'],      # C düğümünün komşusu F
    'D':[],         # D düğümünün komşusu yok (yaprak düğüm)
    'E':[],         # E düğümünün komşusu yok (yaprak düğüm)
    'F':[],         # F düğümünün komşusu yok (yaprak düğüm)
}

# BFS algoritması için gerekli listeler
ziyaret=[]  # Ziyaret edilen düğümleri tutar
yıgın=[]    # BFS için kuyruk (FIFO - First In First Out)

def bfs(ziyaret,grafik,düğüm):
    """
    Breadth-First Search (BFS) algoritması
    Graf üzerinde genişlik öncelikli arama yapar
    """
    # Başlangıç düğümünü ziyaret edildi olarak işaretle ve kuyruğa ekle
    ziyaret.append(düğüm)
    yıgın.append(düğüm)

    # Kuyruk boşalana kadar devam et
    while yıgın:
        # Kuyruğun başındaki düğümü al (FIFO prensibi)
        s=yıgın.pop(0)
        print(s,end=" ")  # Düğümü yazdır

        # Mevcut düğümün tüm komşularını kontrol et
        for komsu in grafik[s]:
            # Eğer komşu daha önce ziyaret edilmemişse
            if komsu not in ziyaret:
                # Komşuyu ziyaret edildi olarak işaretle
                ziyaret.append(komsu)
                # Komşuyu kuyruğa ekle (daha sonra işlenecek)
                yıgın.append(komsu)

# BFS algoritmasını A düğümünden başlayarak çalıştır
bfs(ziyaret,grafik,'A')                 