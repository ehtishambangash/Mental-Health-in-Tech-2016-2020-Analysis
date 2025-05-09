import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(page_title="Mental Health Trends Dashboard", layout="wide")
st.title("🧠 Mental Health in Tech (2016–2020) Dashboard")

# Assuming CSV files still needed for viewing cleaned datasets
@st.cache_data
def load_data(year):
    return pd.read_csv(rf"cleaned_mental_health_{year}.csv")

years = list(range(2016, 2021))
data_by_year = {year: load_data(year) for year in years}

# Function to load image safely
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.warning(f"Image not found: {image_path}")
        return None

# Sidebar navigation
section = st.sidebar.radio("📁 Select Section", [
    "Trends by Demographics", 
    "Trends by Year", 
    "Comparison Across Years", 
    "View Cleaned Datasets"
])

# 1. Trends by Demographics using Images
if section == "Trends by Demographics":
    st.header("👥 Trends by Demographics (Sentiment Distribution)")

    st.header("📈 Cross-Year Comparison")

    comparison_path = rf"plots\image.png"
    comp_img = load_image(comparison_path)

    comparison_path3 = rf"plots\image3.png"
    comp_img3 = load_image(comparison_path3)


    comparison_path2 = rf"plots\image2.png"
    comp_img2 = load_image(comparison_path2)

    if comp_img:
        st.image(comp_img, use_container_width=True)

    if comp_img3:
        st.image(comp_img3, use_container_width=True)

    if comp_img2:
        st.image(comp_img2, use_container_width=True)

# 2. Trends by Year using Images
elif section == "Trends by Year":
    st.header("📅 Yearly Trends (Sentiment Line + Pie Charts)")

    for year in years:
        st.subheader(f"📌 Year: {year}")

        line_chart_path = rf"plots\{year}_sentiment_line.png"
        pie_chart_path = rf"plots\{year}_sentiment_pie.png"

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Line Chart:**")
            line_img = load_image(line_chart_path)
            if line_img:
                st.image(line_img, use_container_width=True)

        with col2:
            st.markdown("**Pie Chart:**")
            pie_img = load_image(pie_chart_path)
            if pie_img:
                st.image(pie_img, use_container_width=True)

# 3. Comparison Across Years
elif section == "Comparison Across Years":
    st.header("📈 Cross-Year Comparison")

    comparison_path = rf"plots\sentiment_relation_plot.png"
    comp_img = load_image(comparison_path)
    if comp_img:
        st.image(comp_img, use_container_width=True)

# 4. View Cleaned Datasets
elif section == "View Cleaned Datasets":
    st.header("📂 View Cleaned Datasets")

    selected_year = st.selectbox("Choose Year", years)
    df = data_by_year[selected_year]
    st.write(f"Showing cleaned data for {selected_year}:")
    st.dataframe(df)
