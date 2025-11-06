# 🎬 CineMetrics: AI-Powered Movie Data Engineering Dashboard

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-success.svg)  

**An interactive Data Engineering + Analytics dashboard for real-time movie insights**

[Features](#-features) • [Demo](#demo) • [Installation](#installation--setup) • [Usage](#usage) • [Architecture](#architecture)  

</div>

---

## 📖 Overview  
**CineMetrics** demonstrates a production-style data engineering project: a full ETL (Extract → Transform → Load) workflow built in Python + Streamlit. It sources live movie data via the OMDb API, cleans and transforms it, stores cleaned data into a simulated data lake (CSV), and visualizes metrics such as IMDb ratings and box-office revenue. Optional AI integration with Gemini API adds intelligent movie summaries.

### 🎯 Key Highlights  
- 🔄 Real-time ETL pipeline – automated extraction & transformation  
- 📊 Interactive analytics dashboard built with Streamlit  
- 🗄️ Local “data lake” storage simulation using CSV  
- 🤖 Optional AI-powered insights (Gemini)  
- 🎥 Movie-focused metrics: ratings, genre, box office, etc.  

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎞️ Real-Time Data Extraction | Fetches live movie info from OMDb API, with error handling |
| 🔧 Full ETL Pipeline | Extract → Transform → Load implemented in Python & Pandas |
| 🗃️ Data Lake Storage | Saves processed data locally in `/data_lake/cleaned_movie_data.csv` |
| 🎨 Interactive UI | Streamlit frontend with movie posters, details and charts |
| 📊 Visual Analytics | Bar charts comparing IMDb ratings & box-office collections |
| 💾 Downloadable Data | Export cleaned movie dataset as CSV |
| 🤖 AI Summaries | (Optional) Use Gemini API to generate intelligent movie summaries |
| 🔍 Multi-movie Analysis | Compare multiple movies in one run |

---

## 🚀 Demo

### Dashboard Workflow  

### Sample Output  
- Movie cards: posters, title, year, genre, director, rating  
- Bar charts: IMDb ratings vs box-office  
- CSV download: cleaned movie dataset  

---

## 🧠 Tech Stack

<div align="center">
  
| Category        | Technologies                              |
|-----------------|-------------------------------------------|
| Language        | Python                                    |
| Framework       | Streamlit                                 |
| Data Processing | Pandas                                    |
| API Source      | OMDb API                                  |
| Storage         | CSV (Simulated Data Lake)                 |
| AI Integration  | Gemini API (Optional)                     |
| Env Management  | python-dotenv                             |

</div>

---



## 📁 Project Structure

<img width="259" height="331" alt="image" src="https://github.com/user-attachments/assets/92c34326-e18a-4d22-a6e7-aea4274aba4c" />




### 🗝️ Environment Variables

Before running the application, create a `.env` file in your project’s root directory and add the following:

env
# OMDb API Configuration (Required)
OMDB_API_KEY=your_omdb_api_key_here

# Gemini AI Configuration (Optional)
GEMINI_API_KEY=your_gemini_api_key_here
🔑 Getting API Keys
🎬 OMDb API Key (Required)
Visit http://www.omdbapi.com/apikey.aspx

Sign up for a free API key

Paste your key in the .env file:

env
Copy code
OMDB_API_KEY=your_omdb_api_key_here
🤖 Gemini API Key (Optional)
Visit https://makersuite.google.com/app/apikey

Create your Gemini API key

Add it in .env file:

env
Copy code
GEMINI_API_KEY=your_gemini_api_key_here
⚡ Installation & Setup
🧩 Prerequisites
Make sure you have the following installed:

🐍 Python 3.8+

📦 pip (Python package manager)

🌐 Git (optional, for cloning the repo)

🪜 Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/CineMetrics.git
cd CineMetrics
🪜 Step 2: Create a Virtual Environment
For Windows:

bash
Copy code
python -m venv env
env\Scripts\activate
For macOS/Linux:

bash
Copy code
python3 -m venv env
source env/bin/activate
🪜 Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
🪜 Step 4: Configure Environment Variables
Create a .env file and add your API keys (see Environment Variables).

🪜 Step 5: Run the Application
bash
Copy code
streamlit run movie_dashboard_app.py
The app will automatically open in your default browser at:
👉 http://localhost:8501 🎉

🎥 Usage
🔹 Basic Workflow
Launch the App

bash
Copy code
streamlit run movie_dashboard_app.py
Enter Movie Names

Open the sidebar

Input multiple titles separated by commas

Example:

Copy code
Inception, Interstellar, Avatar, The Dark Knight, Oppenheimer
Run the Pipeline

Click “🚀 Run CineMetrics Pipeline”

Wait for extraction and transformation

Explore Results

🎞️ View movie posters & details

⭐ Compare IMDb ratings

💰 Analyze Box Office trends

💾 Download cleaned CSV data

Access the Data Lake

Processed data is saved automatically in:

bash
Copy code
data_lake/cleaned_movie_data.csv
📘 Example Input
Copy code
Inception, The Matrix, Avatar, Titanic
📊 Example Output
Movies Processed: 4

Data Fields: Title, Year, IMDb Rating, Box Office, Genre, Director

Visualizations: IMDb Ratings vs Box Office Charts

Download: Clean CSV file for analytics

📊 Data Pipeline Details
🟢 Extract Phase
Fetches data from the OMDb API using HTTP requests

Handles missing values and errors gracefully

Supports batch requests for multiple movies

🟡 Transform Phase
Cleans & validates movie data

Converts IMDb rating & Box Office into numeric values

Removes duplicates and handles null fields

Structures data into a Pandas DataFrame

🔵 Load Phase
Stores processed data in the local Data Lake (/data_lake/)

Creates backup CSV files

Ensures data persistence across sessions

🚀 Future Enhancements
☁️ Cloud Integration – Use Azure Data Lake or AWS S3

⏱️ Workflow Scheduling – Integrate Apache Airflow

📈 Advanced Visuals – Plotly or Power BI dashboards

🤖 ML Models – Add movie recommendation engine

🗃️ Database Support – PostgreSQL / MongoDB integration

⚡ Streaming Support – Kafka for live data ingestion

🐳 Docker Deployment – Containerize for production

🤝 Contributing
We welcome all contributions! 🧠

Follow these steps:

bash
Copy code
# 1️⃣ Fork the repository
# 2️⃣ Create a new branch
git checkout -b feature/AmazingFeature

# 3️⃣ Commit your changes
git commit -m "Add some AmazingFeature"

# 4️⃣ Push your branch
git push origin feature/AmazingFeature

# 5️⃣ Open a Pull Request
👩‍💻 Author
Rashmika Rohit
🎓 Artificial Intelligence & Machine Learning Engineer
🏛️ L.D. College of Engineering

📧 rashmikad1743@gmail.com
🔗 LinkedIn
💻 GitHub

📜 License
This project is licensed under the MIT License.

text
Copy code
MIT License

Copyright (c) 2025 Rashmika

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
🙏 Acknowledgements
🎞️ OMDb API — Movie data source

💻 Streamlit — Frontend dashboard framework

🧠 Pandas — Data transformation library

🤖 Google Gemini — Optional AI insights

🛡️ Shields.io — README badges

📞 Support
If you have questions, feedback, or ideas — reach out anytime:

📧 Email: rashmikad1743@gmail.com

🐛 GitHub Issues

💬 GitHub Discussions

⭐ If you find this project helpful, please give it a Star!
Made with ❤️ by Rashmika Makwana | Data & AI Enthusiast



