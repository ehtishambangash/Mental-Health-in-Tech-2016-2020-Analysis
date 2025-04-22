# 🧠 Mental Health in Tech (2016–2020) Dashboard

This project features a **Streamlit-powered interactive dashboard** that visualizes trends in mental health within the tech industry from 2016 to 2020. Using **NLP-driven sentiment analysis** of survey data, the dashboard allows users to explore sentiment changes over time, compare across demographics, and directly interact with cleaned datasets.

---

## 📊 Features

- **Trends by Demographics:** 
  Visualizes sentiment distribution across gender, age groups, and other demographic factors.

- **Trends by Year:** 
  Year-wise sentiment trends using line and pie charts for each year from 2016 to 2020.

- **Comparison Across Years:** 
  A consolidated view showing how sentiments evolved over time.

- **Cleaned Dataset Viewer:** 
  Interactive table view of cleaned data for each year.

---

## 🛠 Technology Stack

- **Python 3**
- **Streamlit** – for the web-based dashboard
- **Pandas** – for data processing
- **Pillow (PIL)** – for displaying images
- **Jupyter Notebook** – for initial data cleaning and EDA
- **Matplotlib/Seaborn** – for creating sentiment plots
- **Natural Language Processing (NLP)** – for sentiment analysis

---

## 🚀 How to Run the Dashboard

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mental-health-dashboard.git
cd mental-health-dashboard

### 2. Install Dependencies
```bash
pip install streamlit pandas pillow

### 3. Run the Dashboard
```bash
streamlit run dashboard.py

### 4. Navigate the App
Use the sidebar to explore:

- Trends by Demographics
- Trends by Year
- Cross-Year Comparison
- View Cleaned Datasets

## 🔍 How It Works

The dashboard is divided into four main sections:

- **Trends by Demographics**: Displays images from the /plots folder that compare sentiment across different population groups.
- **Trends by Year**: For each year, a line chart and pie chart summarize the sentiment analysis, also stored in the /plots folder.
- **Comparison Across Years**: Shows combined trends using pre-generated visuals to highlight evolving sentiment patterns.
- **Cleaned Dataset Viewer**: Loads pre-cleaned CSVs from 2016 to 2020 and displays them using `st.dataframe()`.

Each visual and dataset is preprocessed to reduce app load time and ensure smooth performance.

## 📌 Notes

- Ensure the CSV and image files are present and named exactly as expected in the `dashboard.py`.
- If you add new data or visuals, update paths and logic in the code accordingly.
- This dashboard is a great fit for internships, data science projects, social tech research, and mental health awareness presentations.


## 📬 Authors

- Ehtisham Hussain  
  📧 ehishambangash111@gmail.com

- Hasnain Bakhat  
  📧 hasnainbakht47@gmail.com

---

## 📃 License

This project is intended for educational and non-commercial use. Please credit the authors when sharing.

