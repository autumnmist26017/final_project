import streamlit as st
import pandas as pd
import re
import os
import base64
from io import StringIO
from scraibe import Scraibe
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Set page config
st.set_page_config(
    page_title="Audio Transcription & Sentiment Analysis",
    page_icon="🎙️",
    layout="wide"
)

# Title and description
st.title("🎙️ Audio Transcription & Sentiment Analysis")
st.markdown("Upload an audio file to transcribe and analyze the sentiment of each speaker.")

# File upload
uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    num_speakers = st.number_input(
        "Number of Speakers", 
        min_value=1, 
        max_value=10, 
        value=2,
        help="Set the number of speakers in the audio"
    )
    language = st.selectbox(
        "Language",
        ["english", "spanish", "french", "german", "italian"],
        index=0,
        help="Select the language of the audio"
    )

@st.cache_resource
def load_model():
    """Load the ScrAIbe model."""
    try:
        # Use a smaller Whisper model for efficiency
        model = Scraibe(whisper_model="tiny", whisper_type="whisper")
        return model
    except Exception as e:
        st.error(f"Error loading ScrAIbe model: {e}")
        return None

def parse_transcription_to_df(transcription_string):
    """Parse transcription string into a DataFrame."""
    pattern = re.compile(r"^(SPEAKER_\d+)\s+\((\d{2}:\d{2}:\d{2})\s+;\s+(\d{2}:\d{2}:\d{2})\):\s*(.*)$")
    lines = transcription_string.strip().split('\n')
    data_rows = []
    
    for line in lines:
        match = pattern.match(line)
        if match:
            speaker, start_time, end_time, text = match.groups()
            data_rows.append({
                'speaker': speaker,
                'start_time': start_time,
                'end_time': end_time,
                'text': text.strip()
            })
    
    return pd.DataFrame(data_rows)

def analyze_sentiment(df):
    """Analyze sentiment of the transcribed text."""
    analyzer = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df['text'].apply(
        lambda text: analyzer.polarity_scores(text)['compound']
    )
    return df

def get_table_download_link(df):
    """Generate a download link for the DataFrame as CSV."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="transcription_results.csv">Download CSV</a>'
    return href

# Main app logic
if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    try:
        # Show a loading spinner while processing
        with st.spinner('Transcribing audio... This may take a few minutes...'):
            # Load the model
            model = load_model()
            if model is None:
                st.error("Failed to load the ScrAIbe model. Please try again.")
                st.stop()
            
            # Transcribe the audio
            transcription = model.autotranscribe(
                "temp_audio.wav", 
                language=language, 
                num_speakers=num_speakers
            )
            
            # Parse the transcription
            df = parse_transcription_to_df(str(transcription))
            
            # Analyze sentiment
            df = analyze_sentiment(df)
            
            # Display results
            st.subheader("Transcription Results")
            st.dataframe(df, use_container_width=True)
            
            # Calculate average sentiment
            speaker_sentiment = df.groupby('speaker')['sentiment_score'].mean().sort_values()
            
            # Display sentiment analysis
            st.subheader("Sentiment Analysis by Speaker")
            st.write("(Score > 0 is positive, < 0 is negative)")
            
            # Plot sentiment
            fig, ax = plt.subplots(figsize=(10, 6))
            colors = ['g' if x > 0 else 'r' for x in speaker_sentiment.values]
            speaker_sentiment.plot(kind='barh', color=colors, ax=ax)
            plt.title('Overall Sentiment by Speaker')
            plt.xlabel('Average Sentiment Score')
            plt.axvline(x=0, color='k', linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            
            # Download button
            st.markdown(get_table_download_link(df), unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    finally:
        # Clean up temporary file
        if os.path.exists("temp_audio.wav"):
            os.remove("temp_audio.wav")
else:
    st.info("Please upload a WAV file to get started.")
