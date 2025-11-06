# 🎬 CineMetrics: AI-Powered Movie Data Engineering Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**An interactive Data Engineering + Analytics Dashboard for real-time movie insights**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation--setup) • [Usage](#-usage) • [Architecture](#️-architecture)

</div>

---

## 📖 Overview

**CineMetrics** is a production-ready **Data Engineering Project** demonstrating a complete **ETL (Extract, Transform, Load)** workflow using real-world movie data.  

Built with **Python** and **Streamlit**, it fetches live data from the **OMDb API**, processes it through a robust data pipeline, stores it in a simulated **Data Lake**, and presents interactive **visual analytics** for insights.  

---

### 🎯 Key Highlights

- 🔄 **Real-time ETL Pipeline** – Automated data extraction and transformation  
- 📊 **Interactive Dashboards** – Stunning analytics powered by Streamlit  
- 🗄️ **Data Lake Architecture** – Local CSV storage simulation  
- 🤖 **AI Integration (Optional)** – Gemini AI for intelligent movie summaries  
- 📈 **Analytics Ready** – IMDb ratings, genre trends, and box office insights  

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| 🎞️ **Real-Time Data Extraction** | Fetches movie data from OMDb API with validation and error handling |
| 🔧 **ETL Pipeline** | Complete Extract → Transform → Load workflow |
| 🗃️ **Data Lake Storage** | Saves cleaned data locally as CSV files |
| 🎨 **Interactive UI** | Sleek Streamlit interface with movie posters and cards |
| 📊 **Visual Analytics** | IMDb ratings and box office comparison charts |
| 💾 **Downloadable Reports** | Export processed movie data as CSV |
| 🤖 **AI Summaries** | (Optional) Gemini AI integration for dynamic insights |
| 🔍 **Batch Processing** | Analyze multiple movies in a single run |

---

## 🚀 Demo

### 🖥️ Dashboard Overview



📽️ CineMetrics Dashboard
├── Sidebar Input: Enter movie names
├── Pipeline Execution: Click to run ETL
├── Results Display:
│ ├── Movie Posters Grid
│ ├── IMDb Ratings Chart
│ ├── Box Office Comparison
│ └── Data Download Button
└── Data Lake: cleaned_movie_data.csv


### 🎬 Sample Output

- **Visual Analytics:** Bar charts comparing IMDb ratings & box office collections  
- **Movie Cards:** Posters, titles, year, rating, and director  
- **Downloadable Data:** Clean CSV export ready for analysis  

---

## 🧠 Tech Stack

<div align="center">

| Category | Technologies |
|:----------:|:-------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |
| **Data Processing** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) |
| **API Source** | OMDb API |
| **Storage** | CSV (Local Data Lake Simulation) |
| **AI (Optional)** | ![Google](https://img.shields.io/badge/Gemini_AI-4285F4?style=flat&logo=google&logoColor=white) |
| **Environment** | python-dotenv |

</div>

---


---

## 📁 Project Structure

CineMetrics/
│
├── 📄 movie_dashboard_app.py      # Main Streamlit application
├── 📄 .env                        # API keys (not in repo)
├── 📄 requirements.txt            # Python dependencies
├── 📄 .gitignore                  # Git ignore rules
├── 📄 README.md                   # Project documentation
│
├── 📁 data_lake/                  # Data storage directory
│   └── cleaned_movie_data.csv     # Processed movie data
│
└── 📁 assets/                     # Optional screenshots
    └── dashboard_preview.png






---

## 🗝️ Environment Variables

Create a file named `.env` in your project root and add:

```env
# OMDb API Key (Required)
OMDB_API_KEY=your_omdb_api_key_here

# Gemini API Key (Optional)
GEMINI_API_KEY=your_gemini_api_key_here

🔑 Getting API Keys

OMDb API Key → https://www.omdbapi.com/apikey.aspx

Gemini API Key (Optional) → https://makersuite.google.com/app/apikey

⚡ Installation & Setup
🧩 Prerequisites

Python 3.8 or higher

pip (Python package manager)

Git (for cloning the repo)

Step 1️⃣: Clone the Repository
git clone https://github.com/yourusername/CineMetrics.git
cd CineMetrics

Step 2️⃣: Create a Virtual Environment

Windows:

python -m venv env
env\Scripts\activate


Mac/Linux:

python3 -m venv env
source env/bin/activate

Step 3️⃣: Install Dependencies
pip install -r requirements.txt

Step 4️⃣: Configure API Keys

Add your API keys in the .env file as shown in Environment Variables
.

Step 5️⃣: Run the App
streamlit run movie_dashboard_app.py


Then open: 👉 http://localhost:8501

🎥 Usage

Launch the app

Enter movie names in the sidebar (comma-separated):

Inception, Interstellar, Avatar, Joker, Oppenheimer


Click 🚀 Run CineMetrics Pipeline

View posters, ratings, and analytics

Download the cleaned movie dataset (CSV)

Access saved data in data_lake/cleaned_movie_data.csv

📊 Data Pipeline Stages
🟢 Extract

Fetches data from OMDb API

Handles invalid inputs & network issues

🟡 Transform

Cleans and standardizes fields (rating, box office, runtime)

Converts numeric types

Removes duplicates & missing entries

🔵 Load

Stores processed dataset as a CSV in /data_lake/

Enables analytics and download options

🚀 Future Enhancements

 Integrate Gemini AI for movie summaries

 Add genre filters & search by year

 Deploy on Streamlit Cloud or Render

 Build Power BI / Plotly Dashboards

 Automate ETL using Apache Airflow

 Store data on Azure Data Lake / AWS S3

👩‍💻 Author

Rashmika Rohit
🎓 Artificial Intelligence & Machine Learning Engineer — L.D. College of Engineering
💼 SSIP-Funded Innovator | Data & AI Enthusiast






📜 License

This project is licensed under the MIT License:

MIT License

Copyright (c) 2025 Rashmika

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

🙏 Acknowledgements

OMDb API
 — for movie data

Streamlit
 — for dashboard UI

Pandas
 — for data manipulation

Google Gemini
 — for AI integration (optional)

Shields.io
 — for badges

<div align="center">

⭐ Star this repo if you like it!
Built with ❤️ by Rashmika Rohit | Data & AI Engineer

</div> ```

✅ Pro Tip for GitHub Upload:
When you upload this README.md:

GitHub will render all badges, tables, and emoji perfectly.

Keep .env and /data_lake/ in .gitignore.

Add a screenshot under /assets/ (e.g., dashboard_preview.png) for visual impact.

