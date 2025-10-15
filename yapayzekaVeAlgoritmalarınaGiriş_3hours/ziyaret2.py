# DFS (Depth-First Search) Algoritması Örneği
# Bu kod, bir graf üzerinde derinlik öncelikli arama algoritmasını uygular

# Graf yapısı - her düğümün komşularını liste halinde tutar
# 'A' düğümü 'B' ve 'C' düğümlerine bağlı
# 'B' düğümü 'D' ve 'E' düğümlerine bağlı
# 'C' düğümü 'F' düğümüne bağlı
# 'D', 'E', 'F' düğümleri terminal düğümler (komşu yok)
grafik={
    'A':["B","C"],
    'B':["D","E"],
    'C':["F"],
    'D':[],
    'E':[],
    'F':[],
}

# Ziyaret edilen düğümleri takip etmek için set kullanıyoruz
# Set kullanma sebebi: O(1) arama ve ekleme karmaşıklığı
ziyaret=set()

# DFS (Depth-First Search) fonksiyonu
# Parametreler:
# - ziyaret: ziyaret edilen düğümleri tutan set
# - grafik: graf yapısı (sözlük)
# - dügüm: şu anda işlenen düğüm
def dfs(ziyaret,grafik,dügüm):
    # Eğer düğüm daha önce ziyaret edilmemişse
    if dügüm not in ziyaret:
        # Düğümü yazdır (ziyaret et)
        print(dügüm)
        # Düğümü ziyaret edildi olarak işaretle
        ziyaret.add(dügüm)
        # Bu düğümün tüm komşuları için DFS'i tekrar çağır
        for komsu in grafik[dügüm]:
            dfs(ziyaret,grafik,komsu)

# DFS algoritmasını 'A' düğümünden başlatarak çalıştır
# Sonuç: A -> B -> D -> E -> C -> F (derinlik öncelikli sıralama)
dfs(ziyaret,grafik,'A')