import streamlit as st
import pickle
from pathlib import Path
import streamlit.components.v1 as components

# Mapping of cities to their map and model files
city_files = {
    "Bangalore": {
        "map": "bangalore_map.html",
        "model": "bangaluru_model.pkl"
    },
    "Delhi": {
        "map": "delhi_map.html",
        "model": "delhi_model.pkl"
    },
    "Pune": {
        "map": "pune_map.html",
        "model": "pune_model.pkl"
    },
    "Kolkata": {
        "map": "kolkata_map.html",
        "model": "kolkata_model.pkl"
    }
}

# Streamlit App
st.title("EV Charging Station Suggestion System (Multi-City)")

# City Selection
city = st.selectbox("Select a city", list(city_files.keys()))

# Load map
map_file = city_files[city]["map"]
if Path(map_file).exists():
    with open(map_file, 'r', encoding='utf-8') as f:
        map_html = f.read()
    components.html(map_html, height=600, scrolling=True)
else:
    st.error(f"Map for {city} not found!")

# Load model
model_file = city_files[city]["model"]
if Path(model_file).exists():
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
    st.success(f"Model for {city} loaded successfully!")
else:
    st.error(f"Model for {city} not found!")

# Placeholder for model usage
# Example: st.write(model.predict(input_features))
st.write("**Model ready to give EV station suggestions!** (You can build input forms if needed.)")
