import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Analisis Bike Sharing")

# Load Dataset (tidak perlu upload)
day_data = pd.read_csv("day.csv")
hour_data = pd.read_csv("hour.csv")

# Informasi Dataset
st.subheader("Informasi Dataset")
st.write("Dataset 'day.csv':")
st.write(day_data.head())
st.write("Dataset 'hour.csv':")
st.write(hour_data.head())

# Visualisasi 1: Pola Peminjaman Berdasarkan Waktu (Jam)
st.subheader("Visualisasi 1: Pola Peminjaman Berdasarkan Waktu (Jam)")
hourly_counts = hour_data.groupby('hr')['cnt'].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o', color='blue')
plt.title('Rata-rata Peminjaman Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Rata-rata Jumlah Peminjaman')
plt.grid(True)
st.pyplot(plt)

# Visualisasi 2: Pengaruh Cuaca dan Suhu terhadap Jumlah Peminjaman
st.subheader("Visualisasi 2: Pengaruh Cuaca dan Suhu terhadap Jumlah Peminjaman")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=hour_data, x='temp', y='cnt', hue='weathersit', palette='coolwarm')
plt.title('Pengaruh Suhu dan Cuaca terhadap Jumlah Peminjaman')
plt.xlabel('Suhu (Normalized)')
plt.ylabel('Jumlah Peminjaman')
st.pyplot(plt)

# Informasi Tambahan
st.markdown("""
**Analisis**:
1. Dari visualisasi pertama, terlihat bahwa peminjaman sepeda memiliki pola tertentu berdasarkan waktu. Peminjaman cenderung lebih tinggi pada jam tertentu.
2. Dari visualisasi kedua, terlihat bahwa kondisi cuaca dan suhu memengaruhi jumlah peminjaman sepeda. Suhu yang lebih tinggi dan cuaca cerah cenderung meningkatkan jumlah peminjaman.
""")