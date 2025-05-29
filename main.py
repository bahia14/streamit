import streamlit as st

# Set page config for light theme and layout
st.set_page_config(page_title="US States App", layout="centered")

# Custom CSS for pale background and styling
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
            color: #333;
        }
        .stSelectbox label {
            font-weight: bold;
            color: #555;
        }
        h1 {
            color: #666;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("🇺🇸 US States")

# List of all 50 U.S. states
us_states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
    'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
    'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
    'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
    'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
    'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
    'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]

# Dropdown menu
selected_state = st.selectbox("Choose a U.S. state:", options=us_states)

# Show selected state
if selected_state:
    st.success(f"You selected: **{selected_state}**")