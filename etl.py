# etl.py
"""
Basit ETL pipeline:
1) Excel'den veri oku (Extract)
2) Temizle/Dönüştür (Transform)
3) CSV kaydet ve SQLite DB'ye yükle (Load)
"""

import pandas as pd
import sqlite3
from pathlib import Path

EXCEL_FILE = "musteriler.xlsx"
CSV_FILE = "musteriler.csv"
SQLITE_DB = "dwh_demo.db"
TABLE_NAME = "Musteriler"

def extract(excel_path):
    # Excel dosyasını oku (pandas otomatik sütunları algılar)
    print("1) Extract: Excel okunuyor:", excel_path)
    df = pd.read_excel(excel_path, engine="openpyxl")
    print("   Satır sayısı:", len(df))
    return df

def transform(df):
    # Temel temizleme & dönüşümler
    print("2) Transform: Temizleme başlıyor")
    # 2.1 Sütun isimlerini standartlaştır (boşluk varsa temizle)
    df.columns = [c.strip() for c in df.columns]

    # 2.2 Küçük yazım farklarını düzelt (örnek olmadıysa atla)
    # (bizim örnekte 'Gelir' varsa None dolduracağız)
    # 2.3 Eksik gelirleri ortalama ile doldur
    if "Gelir" in df.columns:
        df["Gelir"] = pd.to_numeric(df["Gelir"], errors="coerce")  # sayıya çevir
        mean_gelir = df["Gelir"].mean()
        df["Gelir"] = df["Gelir"].fillna(mean_gelir)

    # 2.4 Sehir isimlerini düzgün formata getir
    if "Sehir" in df.columns:
        df["Sehir"] = df["Sehir"].astype(str).str.title()

    # 2.5 Ek özellik: Gelir kategorisi
    df["GelirKategori"] = pd.cut(df["Gelir"], bins=[-1, 9000, 11000, 9999999], labels=["Dusuk","Orta","Yuksek"])

    print("   Transform tamam. Örnek:")
    print(df.head(3))
    return df

def load_csv(df, csv_path):
    print("3) Load: CSV kaydediliyor:", csv_path)
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

def load_sqlite(df, sqlite_db, table_name):
    print("3) Load: SQLite veritabanına yazılıyor:", sqlite_db)
    conn = sqlite3.connect(sqlite_db)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def validate(sqlite_db, table_name):
    print("4) Validate: Veritabanında doğrulama")
    conn = sqlite3.connect(sqlite_db)
    df = pd.read_sql(f"SELECT Sehir, COUNT(*) as Adet, ROUND(AVG(Gelir),2) as OrtGelir FROM {table_name} GROUP BY Sehir", conn)
    print(df)
    conn.close()

def main():
    p = Path(EXCEL_FILE)
    if not p.exists():
        print(f"Hata: {EXCEL_FILE} bulunamadı. Lütfen create_sample_excel.py çalıştırın veya dosyayı koyun.")
        return
    df = extract(EXCEL_FILE)
    df = transform(df)
    load_csv(df, CSV_FILE)
    load_sqlite(df, SQLITE_DB, TABLE_NAME)
    validate(SQLITE_DB, TABLE_NAME)
    print("ETL pipeline tamamlandı.")

if __name__ == "__main__":
    main()
