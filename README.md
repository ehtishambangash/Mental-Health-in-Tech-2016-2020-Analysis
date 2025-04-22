# Mental Health in Tech Dashboard

A comprehensive Streamlit-based dashboard visualizing sentiment analysis of mental health in the technology industry from 2016 to 2020.

## 📋 Project Overview

This dashboard visualizes sentiment analysis results from the OSMI Mental Health in Tech Survey conducted from 2016 to 2020. The application processes qualitative responses from survey participants, performs sentiment analysis using NLTK's VADER sentiment analyzer, and presents the results through an interactive dashboard.

## 👨‍💻 Contributors

- **Ehtisham Hussain** (ehishambangash111@gmail.com)
- **Hasnain Bakhat** (hasnainbakht47@gmail.com)

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Streamlit
- Pandas
- NLTK
- Matplotlib
- Seaborn
- PIL (Python Imaging Library)

### Installation

1. Clone the repository
2. Install the required dependencies:
```
pip install streamlit pandas nltk matplotlib seaborn pillow
```
3. Download NLTK resources:
```python
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
```

## 🧠 Dashboard Features

The dashboard consists of four main sections:

1. **Trends by Demographics**: Visualizes sentiment distribution across different geographic regions using boxplots, barplots, and lineplots.

2. **Trends by Year**: Displays yearly sentiment trends through line charts and pie charts for each year from 2016 to 2020.

3. **Comparison Across Years**: Provides comparative analysis of sentiment scores across all years through boxplots.

4. **View Cleaned Datasets**: Allows exploration of the processed datasets for each year.

## 💻 How to Use the Dashboard

1. Start the Streamlit application:
```
streamlit run app.py
```

2. Use the sidebar navigation to select between different visualization sections:
   - **Trends by Demographics**: Explores sentiment patterns across different countries
   - **Trends by Year**: Views year-specific sentiment distributions
   - **Comparison Across Years**: Compares sentiment trends across all years
   - **View Cleaned Datasets**: Examines the processed data directly

## 🔍 Technical Details

### Data Processing

The application processes five years of survey data (2016-2020) using the following steps:

1. Text cleaning and preprocessing:
   - Converting text to lowercase
   - Removing punctuation, numbers, and stopwords
   - Lemmatizing words to their base form
  
2. Sentiment analysis using VADER:
   - Computing compound sentiment scores
   - Categorizing responses as positive, negative, or neutral
   - Generating aggregated views by demographics and year

### Dashboard Implementation

The Streamlit dashboard includes:
- Navigation sidebar for intuitive section switching
- Interactive data tables for exploring processed data
- Data visualizations including:
  - Boxplots for sentiment distribution comparisons
  - Pie charts showing sentiment category proportions
  - Line charts tracking sentiment trends over time
  - Bar plots comparing regional sentiment patterns

## 📊 Code Structure

- `app.py`: Main Streamlit application file
- `/plots`: Directory containing generated visualization images
- `cleaned_mental_health_XXXX.csv`: Processed datasets for each year

## 🔄 Data Flow

1. Raw survey data is loaded from CSV files
2. Text responses are cleaned and preprocessed
3. NLTK's VADER analyzer computes sentiment scores
4. Sentiment labels are assigned based on compound scores
5. Processed data is saved to CSV files
6. Visualizations are generated and displayed in the dashboard

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
