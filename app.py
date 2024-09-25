import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
@st.cache_data
def load_data():
    day_df = pd.read_csv('day_cleaned.csv')
    hour_df = pd.read_csv('hour_cleaned.csv')
    
    # Pastikan kolom 'date' dalam format datetime
    day_df['date'] = pd.to_datetime(day_df['date'])
    hour_df['date'] = pd.to_datetime(hour_df['date'])
    
    return day_df, hour_df

day_df, hour_df = load_data()

# Header dan Pengantar
st.title("Bike Sharing Analysis Dashboard")
st.markdown("""
Ini adalah dashboard untuk menganalisis penggunaan sepeda bersama di Washington D.C. berdasarkan **Bike Sharing Dataset**. Dashboard ini mencakup:
- Perbandingan antara pengguna terdaftar dan pengguna biasa di tahun 2011 dan 2012
- Analisis penggunaan sepeda berdasarkan musim
- Dominasi penggunaan sepeda di hari kerja dan libur
- Puncak penggunaan sepeda pada jam tertentu
""")

# Filter Interaktif
st.sidebar.header("Filter by Date Range")
min_date = day_df['date'].min().date()
max_date = day_df['date'].max().date()

# Buat filter rentang tanggal menggunakan st.date_input
date_range = st.sidebar.date_input(
    "Select date range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Pastikan ada dua nilai dalam rentang tanggal
if len(date_range) == 2:
    start_date, end_date = date_range
    st.write(f"Data shown for date range: {start_date} to {end_date}")
else:
    st.error("Please select a valid date range.")
    st.stop()

# Filter berdasarkan tahun
years = sorted(day_df['year'].unique())
selected_years = st.sidebar.multiselect("Select Year", options=years, default=years)

# Terapkan filter berdasarkan tanggal dan tahun yang dipilih
filtered_day_df = day_df[
    (day_df['date'].dt.date >= start_date) & 
    (day_df['date'].dt.date <= end_date) &
    (day_df['year'].isin(selected_years))
]
filtered_hour_df = hour_df[
    (hour_df['date'].dt.date >= start_date) & 
    (hour_df['date'].dt.date <= end_date) &
    (hour_df['year'].isin(selected_years))
]

if filtered_day_df.empty or filtered_hour_df.empty:
    st.warning("No data available for the selected date range and filters.")
    st.stop()

# Total Penggunaan setelah filter diterapkan
total_registered = filtered_day_df['registered'].sum()
total_casual = filtered_day_df['casual'].sum()

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Registered Users", f"{total_registered:,}")
with col2:
    st.metric("Total Casual Users", f"{total_casual:,}")

# Visualisasi Tren Penggunaan Sepeda Berdasarkan Tahun dan Tipe User
st.header("Tren Penggunaan Sepeda Berdasarkan Tahun")
yearly_user_counts = filtered_day_df.groupby('year')[['registered', 'casual']].sum()
st.bar_chart(yearly_user_counts)

# Pola Penggunaan Sepeda Berdasarkan Musim
season_counts = filtered_day_df.groupby('season')['cnt'].sum()
st.bar_chart(season_counts)

# Perbedaan Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan
st.header("Perbedaan Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan")
workingday_mapping = {0: 'Weekend/Holiday', 1: 'Working Day'}
filtered_day_df['workingday_name'] = filtered_day_df['workingday'].map(workingday_mapping)
workingday_counts = filtered_day_df.groupby('workingday_name')['cnt'].sum().sort_values(ascending=False)
st.bar_chart(workingday_counts)

# Distribusi Penggunaan Sepeda Selama Jam-Jam Tertentu
st.header("Distribusi Penggunaan Sepeda Selama Jam-Jam Tertentu")
hourly_counts = filtered_hour_df.groupby('hour')['cnt'].mean().sort_index()
st.line_chart(hourly_counts)

# Tambahkan informasi tambahan
st.info("Data source: Capital Bikeshare system, Washington D.C., USA")
st.write("Dashboard created by Rafly Rangghani Putra")