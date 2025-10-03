import pandas as pd

data = [

    {"MusteriId": 101, "Ad": "Ali", "Soyad": "Yılmaz", "Sehir": "Ankara", "Gelir": 12000},
    {"MusteriId": 102, "Ad": "Ayşe", "Soyad": "Demir", "Sehir": "İstanbul", "Gelir": 8000},
    {"MusteriId": 103, "Ad": "Mehmet", "Soyad": "Kaya", "Sehir": "İzmir", "Gelir": 9500},
    {"MusteriId": 104, "Ad": "Zeynep", "Soyad": "Çelik", "Sehir": "Bursa", "Gelir": None},  # boş gelir örneği
    {"MusteriId": 105, "Ad": "Erdem", "Soyad": "Yılmaz", "Sehir": "Sivas", "Gelir": 7500}
]

df = pd.DataFrame(data)
df.to_excel("musteriler.xlsx", index=False, engine="openpyxl")
print("musteriler.xlsx oluşturuldu.")