import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# LOAD DATA

hour_df = pd.read_csv("hour_clean.csv")
day_df = pd.read_csv("day_clean.csv")

# SIDEBAR FILTER

st.sidebar.header("Filter")

selected_year = st.sidebar.selectbox(
    "Pilih Tahun",
    options=sorted(day_df['year'].unique())
)

selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=day_df['season'].unique(),
    default=day_df['season'].unique()
)
selected_time_group = st.sidebar.multiselect(
    "Pilih Kategori Waktu",
    options=['Morning', 'Afternoon', 'Evening', 'Night'],
    default=['Morning', 'Afternoon', 'Evening', 'Night']
)

# TITLE

st.title("Bike Sharing Dashboard")
st.markdown("Analisis penyewaan sepeda berdasarkan musim dan tren tahunan (2011–2012)")



# PERTANYAAN 1

st.header(" Pengaruh Musim terhadap Penyewaan Sepeda")

filtered_day = day_df[
    (day_df['year'] == selected_year) &
    (day_df['season'].isin(selected_season))
]

season_usage = filtered_day.groupby('season')['count_cr'].mean().sort_values(ascending=False)

st.write(f"Menampilkan data tahun: {selected_year}")

# FIX DI SINI
fig2, ax2 = plt.subplots()

colors = ['#4C72B0'] + ['#BDBDBD']*(len(season_usage)-1)

sns.barplot(x=season_usage.index, y=season_usage.values, palette=colors, ax=ax2)

ax2.set_title("Pengaruh Musim terhadap Penyewaan Sepeda")
ax2.set_xlabel("Musim")
ax2.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig2)

# PERTANYAAN 2

st.header("📈 Tren Penyewaan Sepeda")

filtered_trend = day_df[day_df['year'] == selected_year]

time_series = filtered_trend.groupby(['year','month'])['count_cr'].mean().reset_index()

month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
time_series['month'] = pd.Categorical(time_series['month'], categories=month_order, ordered=True)

time_series = time_series.sort_values(['year','month'])

fig3, ax3 = plt.subplots()

sns.lineplot(data=time_series, x='month', y='count_cr', marker='o', ax=ax3)

ax3.set_title(f"Tren Penyewaan Sepeda Tahun {selected_year}")
ax3.set_xlabel("Bulan")
ax3.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig3)



# ANALISIS Lanjutan 
# =========================
## clustering 
st.header("Clustering Penyewaan Sepeda Berdasarkan Waktu")

# buat kolom time_group
hour_df['time_group'] = hour_df['hours'].apply(lambda x:
    'Morning' if 6 <= x < 12 else
    'Afternoon' if 12 <= x < 17 else
    'Evening' if 17 <= x < 21 else
    'Night'
)

# filter berdasarkan pilihan user
filtered_cluster = hour_df[
    hour_df['time_group'].isin(selected_time_group)
]

# hitung rata-rata
time_cluster = filtered_cluster.groupby('time_group')['count_cr'].mean().sort_values(ascending=False)

# plot
fig4, ax4 = plt.subplots()

colors = ['#2E8B57'] + ['#BDBDBD']*(len(time_cluster)-1)

sns.barplot(x=time_cluster.index, y=time_cluster.values, palette=colors, ax=ax4)

ax4.set_title("Clustering Penyewaan Sepeda Berdasarkan Waktu")
ax4.set_xlabel("Kategori Waktu")
ax4.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig4)



st.header("Analisis Tren Penyewaan Sepeda Berdasarkan Waktu")

# pastikan format datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# ambil min & max tanggal
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

# date range picker
date_range = st.date_input(
    "Pilih Rentang Tanggal",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# pastikan user pilih 2 tanggal
if len(date_range) == 2:
    start_date, end_date = date_range

    # filter data
    filtered_time = day_df[
        (day_df['dteday'] >= pd.to_datetime(start_date)) &
        (day_df['dteday'] <= pd.to_datetime(end_date))
    ]

    # agregasi (rata-rata harian)
    time_usage = filtered_time.groupby('dteday')['count_cr'].mean()

    # plot
    fig4, ax4 = plt.subplots(figsize=(12,4))

    ax4.plot(time_usage.index, time_usage.values, marker='o', linewidth=1)
    ax4.set_title("Tren Penyewaan Sepeda Berdasarkan Rentang Waktu")
    ax4.set_xlabel("Tanggal")
    ax4.set_ylabel("Rata-rata Penyewaan")

    plt.xticks(rotation=45)

    st.pyplot(fig4)

else:
    st.warning("Silakan pilih rentang tanggal lengkap")

# =========================
# INSIGHT
# =========================
st.markdown("---")
st.subheader("Insight")

st.write("""
- Rata-rata penyewaan sepeda tertinggi terjadi pada kelompok waktu evening
- Musim Fall memiliki rata-rata penyewaan sepeda tertinggi
- Tahun 2012 menunjukkan peningkatan dibandingkan 2011
""")