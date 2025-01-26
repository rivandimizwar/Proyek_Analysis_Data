import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Analisis Bike Sharing")

# Upload dan Baca Dataset
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset:")
    st.write(data.head())

    # Pilihan Analisis
    st.sidebar.header("Pilih Analisis")
    analysis_type = st.sidebar.radio(
        "Pilih tipe analisis:", ("Rata-rata Peminjaman Berdasarkan Hari", "Rata-rata Peminjaman Berdasarkan Jam")
    )

    # Rata-rata Peminjaman Berdasarkan Hari
    if analysis_type == "Rata-rata Peminjaman Berdasarkan Hari":
        daily_counts = data.groupby('dteday')['cnt'].mean()
        st.write("Rata-rata peminjaman per hari:")
        st.line_chart(daily_counts)

    # Rata-rata Peminjaman Berdasarkan Jam
    elif analysis_type == "Rata-rata Peminjaman Berdasarkan Jam":
        if 'hr' in data.columns:
            hourly_counts = data.groupby('hr')['cnt'].mean()
            st.write("Rata-rata peminjaman per jam:")
            st.bar_chart(hourly_counts)
        else:
            st.error("Kolom 'hr' tidak ditemukan dalam dataset.")

    # Visualisasi Seaborn
    st.sidebar.header("Pengaturan Visualisasi")
    hue_option = st.sidebar.selectbox("Pilih hue untuk visualisasi", options=data.columns, index=0)

    if st.sidebar.button("Buat Visualisasi"):
        plt.figure(figsize=(10, 6))
        sns.barplot(x=data['season'], y=data['cnt'], hue=data[hue_option])
        st.pyplot(plt)

else:
    st.write("Silakan upload file CSV untuk memulai analisis.")
