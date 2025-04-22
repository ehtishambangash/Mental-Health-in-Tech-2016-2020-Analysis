import streamlit as st
import pandas as pd
from PIL import Image
import os

# Set up the page configuration for Streamlit
st.set_page_config(page_title="Mental Health Trends Dashboard", layout="wide")
st.title("🧠 Mental Health in Tech (2016–2020) Dashboard")

# Function to load CSV data for a given year
@st.cache_data
def load_data(year):
    file_path = os.path.join(f"cleaned_mental_health_{year}.csv")
    
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return None  # Return None or empty dataframe if file is missing
    
    return pd.read_csv(file_path)

# Define the years for the dataset (2016 to 2020)
years = list(range(2016, 2021))

# Load the data for all years
data_by_year = {year: load_data(year) for year in years}

# Function to load images safely
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.warning(f"Image not found: {image_path}")
        return None

# Sidebar navigation for selecting sections
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

    comparison_path = os.path.join("plots", "image.png")
    comp_img = load_image(comparison_path)

    comparison_path2 = os.path.join("plots", "image2.png")
    comp_img2 = load_image(comparison_path2)

    comparison_path3 = os.path.join("plots", "image3.png")
    comp_img3 = load_image(comparison_path3)

    if comp_img:
        st.image(comp_img, use_container_width=True)

    if comp_img2:
        st.image(comp_img2, use_container_width=True)

    if comp_img3:
        st.image(comp_img3, use_container_width=True)

# 2. Trends by Year using Images
elif section == "Trends by Year":
    st.header("📅 Yearly Trends (Sentiment Line + Pie Charts)")

    for year in years:
        st.subheader(f"📌 Year: {year}")

        line_chart_path = os.path.join("plots", f"{year}_sentiment_line.png")
        pie_chart_path = os.path.join("plots", f"{year}_sentiment_pie.png")

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

    comparison_path = os.path.join("plots", "sentiment_relation_plot.png")
    comp_img = load_image(comparison_path)
    
    if comp_img:
        st.image(comp_img, use_container_width=True)

# 4. View Cleaned Datasets
elif section == "View Cleaned Datasets":
    st.header("📂 View Cleaned Datasets")

    selected_year = st.selectbox("Choose Year", years)
    
    # Check if the data exists before showing
    df = data_by_year[selected_year]
    
    if df is not None:
        st.write(f"Showing cleaned data for {selected_year}:")
        st.dataframe(df)
    else:
        st.error(f"Data for {selected_year} is not available.")
