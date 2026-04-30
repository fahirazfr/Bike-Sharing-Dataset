# Bike Sharing Dashboard

Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda dari dataset Bike Sharing selama periode 2011–2012 menggunakan Streamlit.

## Tujuan Analisis

Dashboard ini bertujuan untuk:
- Mengetahui pengaruh musim terhadap jumlah penyewaan sepeda
- Menganalisis tren penyewaan sepeda dari waktu ke waktu
- Mengidentifikasi pola penyewaan berdasarkan kategori waktu (Morning, Afternoon, Evening, Night)

## Fitur Dashboard

- Visualisasi penyewaan sepeda berdasarkan musim
- Tren penyewaan sepeda per bulan
- Clustering sederhana berdasarkan waktu
- Analisis tren interaktif berdasarkan rentang tanggal
- Filter interaktif (tahun, musim, kategori waktu)

## Cara Menjalankan

1. Masuk ke folder project:
   ```
   cd dashboard
   ```

2. (Opsional) Buat virtual environment:
   ```
   python -m venv venv
   ```

3. Aktifkan virtual environment:

   **Windows:**
   ```
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```
   source venv/bin/activate
   ```

4. Install dependencies:
   ```
   python -m pip install -r requirements.txt
   ```

5. Jalankan dashboard:
   ```
   python -m streamlit run dashboard.py
   ```

6. Buka di browser:
   ```
   http://localhost:8501
   ```

## Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset (2011–2012)** yang berisi informasi penyewaan sepeda berdasarkan waktu, musim, cuaca, dan faktor lainnya.

##  Insight Utama

- Rata-rata penyewaan sepeda tertinggi terjadi pada kategori waktu **Evening**
- Musim **Fall** memiliki rata-rata penyewaan tertinggi
- Tahun **2012 menunjukkan peningkatan** dibandingkan tahun 2011
- Pola penyewaan dipengaruhi oleh waktu dan musim

## Catatan

Project ini disarankan dijalankan menggunakan:
- Python versi 3.10 atau 3.11

## Author

Nama: Fahira
