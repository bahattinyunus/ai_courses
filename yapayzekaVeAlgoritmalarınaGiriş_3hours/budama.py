


# Alpha-Beta Budama (Pruning) Algoritması
# Bu kod, minimax algoritmasının optimizasyonu olan alpha-beta budama algoritmasını uygular
# Oyun ağaçlarında gereksiz dalları budayarak hesaplama maliyetini azaltır

# Oyun ağacı yapısı - iç içe listeler halinde
# Her seviye oyuncuların hamlelerini temsil eder
# İlk seviye: Maksimizasyon (oyuncu 1)
# İkinci seviye: Minimizasyon (oyuncu 2) 
# Üçüncü seviye: Maksimizasyon (oyuncu 1)
agac=[[[5,1,2], [8,-8,-9]],[[9,4,5], [-3,4,3]]]

# Kök düğümün derinliği (0'dan başlar)
kok=0

# Budama sayacı - kaç dalın budandığını takip eder
budama=0

# Çocuk düğümleri işleyen ana fonksiyon
# Parametreler:
# - dal: işlenecek düğüm listesi
# - derinlik: mevcut derinlik seviyesi
# - alfa: maksimizasyon oyuncusu için en iyi değer
# - beta: minimizasyon oyuncusu için en iyi değer
def cocuklar(dal,derinlik,alfa,beta):
    global agac
    global kok
    global budama
    i=0  # Liste indeksi için sayaç
    
    # Her çocuk düğümü için döngü
    for cocuk in dal:
        # Eğer çocuk bir liste ise (alt düğümler var)
        if type(cocuk) is list:
            # Alt düğümleri recursive olarak işle
            (nalfa,nbeta)=cocuklar(cocuk,derinlik+1,alfa,beta)
            
            # Minimizasyon seviyesi (tek derinlik)
            if derinlik%2==1:
                # Beta değerini güncelle (daha küçük değer seç)
                beta=nalfa if nalfa<beta else beta
            else:
                # Maksimizasyon seviyesi (çift derinlik)
                # Alfa değerini güncelle (daha büyük değer seç)
                alfa=nbeta if nbeta>alfa else alfa
                # Düğüm değerini güncelle
                dal[i]=alfa if derinlik%2==0 else beta
                i += 1
        else:
            # Yaprak düğüm (terminal durum)
            # Maksimizasyon seviyesinde alfa'yı güncelle
            if derinlik%2==0 and alfa<cocuk:
                alfa=cocuk
            # Minimizasyon seviyesinde beta'yı güncelle
            if derinlik%2==1 and beta>cocuk:
                beta=cocuk
            
            # Alpha-Beta budama koşulu
            # Eğer alfa >= beta ise, bu dal budanabilir
            if alfa>=beta:
                budama+=1  # Budama sayacını artır
                break      # Bu dalı işlemeyi bırak
    
    # Kök düğümdeyse, ağacın son değerini güncelle
    if derinlik==kok:
        agac=alfa if kok==0 else beta
    
    return (alfa,beta)

# Ana Alpha-Beta fonksiyonu
# Parametreler:
# - in_agac: giriş ağacı (varsayılan: global agac)
# - baslangıc: başlangıç derinliği
# - alt: alt sınır (varsayılan: -15)
# - ust: üst sınır (varsayılan: 15)
def alfabeta(in_agac=agac,baslangıc=kok,alt=-15,ust=15):
    global agac
    global budama
    global kok
    
    # Alpha-Beta algoritmasını çalıştır
    (alfa,beta)=cocuklar(agac,baslangıc,alt,ust)
    
    # Eğer dosya doğrudan çalıştırılıyorsa sonuçları yazdır
    if __name__ == "__main__":
        print ("(alfa, beta):",alfa,beta)
        print ("Sonuc: ",agac)
        print ("Budama Sayısı:",budama)
    
    # Sonuçları döndür
    return (alfa,beta,budama,agac)

# Eğer dosya doğrudan çalıştırılıyorsa algoritmayı başlat
if __name__ == "__main__":
    alfabeta(None)