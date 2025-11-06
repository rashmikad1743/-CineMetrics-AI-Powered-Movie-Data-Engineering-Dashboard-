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

**CineMetrics** is a production-ready data engineering project that demonstrates the complete ETL (Extract, Transform, Load) workflow using real-world movie data. Built with **Python** and **Streamlit**, it fetches live data from the OMDb API, processes it through a robust data pipeline, stores it in a simulated data lake, and presents interactive visualizations for analytics.

### 🎯 Key Highlights

- 🔄 **Real-time ETL Pipeline** - Automated data extraction and transformation
- 📊 **Interactive Dashboards** - Beautiful visualizations with Streamlit
- 🗄️ **Data Lake Architecture** - Simulated local storage with CSV format
- 🤖 **AI Integration** - Optional Gemini AI for intelligent insights
- 📈 **Analytics Ready** - IMDb ratings, box office comparisons, and more

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎞️ **Real-Time Data Extraction** | Fetches movie data from OMDb API with error handling |
| 🔧 **ETL Pipeline** | Complete Extract → Transform → Load workflow |
| 🗃️ **Data Lake Storage** | Saves cleaned data to local CSV files |
| 🎨 **Interactive UI** | Beautiful Streamlit interface with movie posters |
| 📊 **Visual Analytics** | IMDb ratings and box office comparison charts |
| 💾 **Downloadable Reports** | Export cleaned data as CSV |
| 🤖 **AI Summaries** | Optional Gemini AI integration for movie insights |
| 🔍 **Batch Processing** | Analyze multiple movies simultaneously |

---

## 🚀 Demo

### Dashboard Preview

```
📽️ CineMetrics Dashboard
├── Sidebar Input: Enter movie names
├── Pipeline Execution: Click to run ETL
├── Results Display:
│   ├── Movie Posters Grid
│   ├── IMDb Ratings Chart
│   ├── Box Office Comparison
│   └── Data Download Button
└── Data Lake: cleaned_movie_data.csv
```

### Sample Output

- **Visual Analytics**: Bar charts comparing IMDb ratings and box office collections
- **Movie Cards**: Display posters, titles, years, and ratings
- **Downloadable Data**: Clean, structured CSV exports

---

## 🧠 Tech Stack

<div align="center">

| Category | Technologies |
|:--------:|:-------------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Framework** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |
| **Data Processing** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) |
| **API** | OMDb API |
| **Storage** | CSV (Data Lake Simulation) |
| **AI** | ![Google](https://img.shields.io/badge/Gemini_AI-4285F4?style=flat&logo=google&logoColor=white) (Optional) |
| **Environment** | python-dotenv |

</div>

---

## ⚙️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│                      (Streamlit Dashboard)                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ETL Pipeline Layer                         │
├─────────────────────────────────────────────────────────────────┤
│  EXTRACT              TRANSFORM              LOAD               │
│  ├─ API Request       ├─ Data Cleaning      ├─ CSV Storage     │
│  ├─ JSON Parse        ├─ Type Conversion    ├─ Data Lake       │
│  └─ Error Handling    └─ Pandas DataFrame   └─ Validation      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       Data Sources                              │
├─────────────────────────────────────────────────────────────────┤
│  • OMDb API (External)                                          │
│  • Gemini AI (Optional)                                         │
└─────────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Data Lake (Local Storage)                     │
│              data_lake/cleaned_movie_data.csv                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
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
```

---

## 🗝️ Environment Variables

Create a `.env` file in the root directory:

```env
# OMDb API Configuration
OMDB_API_KEY=your_omdb_api_key_here

# Optional: Gemini AI Configuration
GEMINI_API_KEY=your_gemini_api_key_here
```

### 🔑 Getting API Keys

1. **OMDb API Key** (Required)
   - Visit: [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx)
   - Sign up for a free API key
   - Paste it in your `.env` file

2. **Gemini API Key** (Optional)
   - Visit: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
   - Create an API key
   - Add it to `.env` for AI features

---

## ⚡ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/CineMetrics.git
cd CineMetrics
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file and add your API keys (see [Environment Variables](#️-environment-variables))

### Step 5: Run the Application

```bash
streamlit run movie_dashboard_app.py
```

The app will open automatically at: **http://localhost:8501** 🎉

---

## 🎥 Usage

### Basic Workflow

1. **Launch the App**
   ```bash
   streamlit run movie_dashboard_app.py
   ```

2. **Enter Movie Names**
   - Open the sidebar
   - Input movie titles separated by commas
   - Example: `Inception, Interstellar, Avatar, The Dark Knight, Oppenheimer`

3. **Run the Pipeline**
   - Click **"🚀 Run CineMetrics Pipeline"**
   - Wait for data extraction and processing

4. **Explore Results**
   - View movie posters and details
   - Analyze IMDb ratings chart
   - Compare box office collections
   - Download cleaned data as CSV

5. **Access Data Lake**
   - Processed data saved in: `data_lake/cleaned_movie_data.csv`
   - Use for further analysis or reporting

### Example Input

```
Inception, The Matrix, Avatar, Titanic
```

### Example Output

- **Total Movies Processed**: 4
- **Data Fields**: Title, Year, IMDb Rating, Box Office, Genre, Director, Actors
- **Visualizations**: Bar charts for ratings and revenue
- **Download**: Clean CSV file ready for analytics

---

## 📊 Data Pipeline Details

### Extract Phase
- Fetches data from OMDb API using HTTP requests
- Handles API errors and missing data gracefully
- Supports batch processing of multiple movies

### Transform Phase
- Cleans and validates movie data
- Converts data types (ratings to float, box office to numeric)
- Removes duplicates and handles null values
- Structures data in Pandas DataFrame

### Load Phase
- Saves processed data to local data lake
- Creates timestamped backups
- Ensures data persistence across sessions

---

## 🚀 Future Enhancements

- [ ] **Cloud Integration**: Migrate to Azure Data Lake or AWS S3
- [ ] **Workflow Orchestration**: Add Apache Airflow scheduling
- [ ] **Advanced Analytics**: Power BI or Plotly dashboards
- [ ] **ML Models**: Movie recommendation engine
- [ ] **Database Support**: PostgreSQL or MongoDB integration
- [ ] **Real-time Streaming**: Kafka for live data ingestion
- [ ] **API Endpoint**: RESTful API for data access
- [ ] **Docker Support**: Containerization for easy deployment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👩‍💻 Author

**Rashmika**  
🎓 *Artificial Intelligence & Machine Learning Engineer*  
🏛️ *L.D. College of Engineering*

[![Email](https://img.shields.io/badge/Email-rashmikad1743%40gmail.com-red?style=flat&logo=gmail)](mailto:rashmikad1743@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/yourusername)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
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
```

---

## 🙏 Acknowledgements

- [OMDb API](http://www.omdbapi.com/) - Movie database API
- [Streamlit](https://streamlit.io/) - Web app framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation library
- [Google Gemini](https://deepmind.google/technologies/gemini/) - AI integration
- [Shields.io](https://shields.io/) - README badges

---

## 📞 Support

If you encounter any issues or have questions:

- 📧 Email: rashmikad1743@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/CineMetrics/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/CineMetrics/discussions)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Rashmika | Data & AI Enthusiast

</div>#   - C i n e M e t r i c s - A I - P o w e r e d - M o v i e - D a t a - E n g i n e e r i n g - D a s h b o a r d -  
 