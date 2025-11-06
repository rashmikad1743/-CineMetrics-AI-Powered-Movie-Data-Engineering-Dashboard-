import streamlit as st
import requests
import pandas as pd
import os

# -------------------- LOAD ENV VARIABLES --------------------
# Try to load .env if python-dotenv is available; keep going if it's not.
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # python-dotenv not installed or failed to load; continue and rely on env vars or input
    pass

API_KEY = os.getenv("OMDB_API_KEY")

# If API key not found in environment, allow the user to paste it into the Streamlit sidebar
if not API_KEY:
    try:
        st.sidebar.warning("OMDb API key not found in environment. You can set OMDB_API_KEY in a .env file or paste it below for this session.")
        _key_input = st.sidebar.text_input("OMDb API Key (session only)", value="", type="password")
        if _key_input:
            API_KEY = _key_input.strip()
    except Exception:
        # Not running inside Streamlit (e.g., `python movie_data_app.py`) — print guidance
        print("OMDb API key not found. Create a .env file with the line `OMDB_API_KEY=your_key` or set the OMDB_API_KEY environment variable.")

if not API_KEY:
    # Final guard: surface a clear message in Streamlit or exit when not available
    try:
        st.error("⚠️ OMDb API key not found! Please set OMDB_API_KEY in a .env file or paste it in the sidebar.")
        st.stop()
    except Exception:
        raise RuntimeError("OMDb API key not found. Set OMDB_API_KEY in environment or .env file.")

DATA_LAKE_DIR = "data_lake"
os.makedirs(DATA_LAKE_DIR, exist_ok=True)

# -------------------- FUNCTIONS --------------------
def fetch_movie_data(movie_name):
    """Fetch movie data from OMDb API"""
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
    return None


def clean_movie_data(raw_data):
    """Convert list of movie JSONs into DataFrame"""
    df = pd.DataFrame(raw_data)
    selected_columns = ['Title', 'Year', 'Genre', 'Director', 'imdbRating', 'imdbVotes', 'Runtime', 'BoxOffice']
    df = df[selected_columns]

    # Data cleaning
    df['imdbRating'] = pd.to_numeric(df['imdbRating'], errors='coerce')
    df['imdbVotes'] = df['imdbVotes'].replace(',', '', regex=True).astype(float)
    df['Runtime'] = df['Runtime'].str.replace(' min', '', regex=False).astype(float)
    df['BoxOffice'] = df['BoxOffice'].replace(r'[\$,]', '', regex=True).astype(float)

    df = df.dropna(subset=['imdbRating', 'BoxOffice', 'Runtime'])
    return df


def save_to_datalake(df):
    """Save cleaned data to simulated data lake"""
    file_path = os.path.join(DATA_LAKE_DIR, "cleaned_movie_data.csv")
    df.to_csv(file_path, index=False)
    return file_path


# -------------------- STREAMLIT FRONTEND --------------------
st.set_page_config(page_title="🎬 CineMetrics Dashboard", layout="wide", page_icon="🎥")

st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .stDownloadButton>button {
        background-color: #09ab3b;
        color: white;
        font-weight: 600;
        border-radius: 8px;
    }
    h1, h2, h3, h4 {
        color: #FFD700;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.title("🎬 CineMetrics – AI-Powered Movie Data Analytics Platform")
st.caption("Developed by Rashmika Rohit | Data Engineering & AI Project")

st.markdown("""
Welcome to **CineMetrics**, an interactive movie analytics dashboard that:
- Fetches real-time data from **OMDb API**
- Cleans and processes it through a mini **ETL pipeline**
- Stores data in a local **Data Lake**
- Visualizes IMDb Ratings and Box Office Collections
""")

# -------------------- SIDEBAR --------------------
st.sidebar.header("🎞️ Search Settings")
st.sidebar.markdown("Enter one or more movie names to analyze:")

movie_input = st.sidebar.text_input("🎬 Enter a movie name:", "Inception")
multi_mode = st.sidebar.checkbox("Enable multiple movie comparison", value=True)

if multi_mode:
    movie_list_text = st.sidebar.text_area("🎥 Movie List (comma-separated):", "Inception, Interstellar, Avatar, Oppenheimer, Joker")
else:
    movie_list_text = movie_input

st.sidebar.markdown("---")
st.sidebar.info("Tip: You can compare multiple movies for IMDb and Box Office analysis.")

# -------------------- RUN PIPELINE --------------------
if st.sidebar.button("🚀 Run CineMetrics Pipeline"):
    movie_list = [m.strip() for m in movie_list_text.split(",") if m.strip()]
    raw_data = []

    with st.spinner("⏳ Fetching movie data..."):
        for movie in movie_list:
            data = fetch_movie_data(movie)
            if data:
                raw_data.append(data)

    if not raw_data:
        st.error("❌ No valid movie data found. Please check the names or API key.")
    else:
        st.success("✅ Data Extraction Successful!")

        df = clean_movie_data(raw_data)
        save_to_datalake(df)

        # -------------------- DISPLAY RESULTS --------------------
        st.markdown("## 📽️ Movie Details")
        for movie in raw_data:
            st.markdown("---")
            st.subheader(f"🎞️ {movie['Title']} ({movie['Year']})")

            col1, col2 = st.columns([1, 3])

            with col1:
                poster_url = movie.get("Poster")
                if poster_url and poster_url != "N/A":
                    st.image(poster_url, width=200)
                else:
                    st.image("https://via.placeholder.com/200x300?text=No+Poster", width=200)

            with col2:
                st.markdown(f"**🎭 Genre:** {movie.get('Genre', 'N/A')}")
                st.markdown(f"**🎬 Director:** {movie.get('Director', 'N/A')}")
                st.markdown(f"**⭐ IMDb Rating:** {movie.get('imdbRating', 'N/A')}")
                st.markdown(f"**💰 Box Office:** {movie.get('BoxOffice', 'N/A')}")
                st.markdown(f"**⏱️ Runtime:** {movie.get('Runtime', 'N/A')}")

        # -------------------- ANALYTICS SECTION --------------------
        st.markdown("## 📊 Movie Analytics Summary")
        st.dataframe(df.style.highlight_max(color='lightgreen', subset=['imdbRating', 'BoxOffice']))

        colA, colB = st.columns(2)
        with colA:
            st.subheader("⭐ IMDb Ratings Comparison")
            st.bar_chart(df.set_index('Title')['imdbRating'])

        with colB:
            st.subheader("💰 Box Office Comparison")
            st.bar_chart(df.set_index('Title')['BoxOffice'])

        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Cleaned Movie Data", csv_data, "cleaned_movie_data.csv", "text/csv")

else:
    st.info("👈 Enter movie names in the sidebar and click **Run CineMetrics Pipeline** to start analysis.")

