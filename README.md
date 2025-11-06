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




##🗝️ Environment Variables
Create a .env file in the root directory:
env# OMDb API Configuration
OMDB_API_KEY=your_omdb_api_key_here

# Optional: Gemini AI Configuration
GEMINI_API_KEY=your_gemini_api_key_here
🔑 Getting API Keys

OMDb API Key (Required)

Visit: http://www.omdbapi.com/apikey.aspx
Sign up for a free API key
Paste it in your .env file


##Gemini API Key (Optional)

Visit: https://makersuite.google.com/app/apikey
Create an API key
Add it to .env for AI features




##⚡ Installation & Setup
Prerequisites

Python 3.8 or higher
pip package manager
Git (for cloning)

Step 1: Clone the Repository
bashgit clone https://github.com/yourusername/CineMetrics.git
cd CineMetrics
Step 2: Create Virtual Environment
Windows:
bashpython -m venv env
env\Scripts\activate
Mac/Linux:
bashpython3 -m venv env
source env/bin/activate
Step 3: Install Dependencies
bashpip install -r requirements.txt
Step 4: Configure Environment Variables
Create a .env file and add your API keys (see Environment Variables)
Step 5: Run the Application
bashstreamlit run movie_dashboard_app.py
The app will open automatically at: http://localhost:8501 🎉

##🎥 Usage
Basic Workflow

Launch the App

bash   streamlit run movie_dashboard_app.py

## Enter Movie Names

Open the sidebar
Input movie titles separated by commas
Example: Inception, Interstellar, Avatar, The Dark Knight, Oppenheimer


## Run the Pipeline

Click "🚀 Run CineMetrics Pipeline"
Wait for data extraction and processing


## Explore Results

View movie posters and details
Analyze IMDb ratings chart
Compare box office collections
Download cleaned data as CSV


Access Data Lake

Processed data saved in: data_lake/cleaned_movie_data.csv
Use for further analysis or reporting



Example Input
Inception, The Matrix, Avatar, Titanic
Example Output

Total Movies Processed: 4
Data Fields: Title, Year, IMDb Rating, Box Office, Genre, Director, Actors
Visualizations: Bar charts for ratings and revenue
Download: Clean CSV file ready for analytics


📊 Data Pipeline Details
Extract Phase

Fetches data from OMDb API using HTTP requests
Handles API errors and missing data gracefully
Supports batch processing of multiple movies

Transform Phase

Cleans and validates movie data
Converts data types (ratings to float, box office to numeric)
Removes duplicates and handles null values
Structures data in Pandas DataFrame

Load Phase

Saves processed data to local data lake
Creates timestamped backups
Ensures data persistence across sessions


🚀 Future Enhancements

 Cloud Integration: Migrate to Azure Data Lake or AWS S3
 Workflow Orchestration: Add Apache Airflow scheduling
 Advanced Analytics: Power BI or Plotly dashboards
 ML Models: Movie recommendation engine
 Database Support: PostgreSQL or MongoDB integration
 Real-time Streaming: Kafka for live data ingestion
 API Endpoint: RESTful API for data access
 Docker Support: Containerization for easy deployment


🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request


👩‍💻 Author
Rashmika
🎓 Artificial Intelligence & Machine Learning Engineer
🏛️ L.D. College of Engineering


📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
MIT License

Copyright (c) 2025 Rashmika

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

🙏 Acknowledgements

OMDb API - Movie database API
Streamlit - Web app framework
Pandas - Data manipulation library
Google Gemini - AI integration
Shields.io - README badges


📞 Support
If you encounter any issues or have questions:

📧 Email: rashmikad1743@gmail.com
🐛 Issues: GitHub Issues
💬 Discussions: GitHub Discussions


<div align="center">
⭐ Star this repository if you find it helpful!
Made with ❤️ by Rashmika | Data & AI Enthusiast
</div>



