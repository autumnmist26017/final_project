# 🎙️ Audio Transcription & Sentiment Analysis

A Streamlit web application that transcribes audio files and performs sentiment analysis on each speaker's dialogue using AI-powered speech recognition and natural language processing.

## ✨ Features

- **Multi-Speaker Transcription**: Supports 1-10 speakers with automatic speaker diarization
- **Multi-Language Support**: English, Spanish, French, German, and Italian
- **Real-time Sentiment Analysis**: Analyzes emotional tone for each speaker using VADER sentiment analyzer
- **Interactive Visualizations**: Bar charts showing sentiment scores by speaker
- **Export Functionality**: Download transcription results as CSV
- **User-Friendly Interface**: Clean, responsive Streamlit UI with custom styling

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **ScrAIbe**: AI transcription library with Whisper integration
- **VADER Sentiment**: Sentiment analysis tool
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **pydub**: Audio processing
- **imageio-ffmpeg**: Audio codec support

## 📋 Requirements

Create a `requirements.txt` file with:


## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/audio-transcription-sentiment
cd audio-transcription-sentiment
```
2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

🎯 Usage
Start the Streamlit application:
```bash
streamlit run audio2.py
```
Open your browser and navigate to http://localhost:8501

Configure settings in the sidebar:

Set the number of speakers (1-10)
Select the audio language
Upload a WAV audio file using the file uploader

Wait for processing (may take a few minutes depending on file size)

View results:

Transcription with timestamps and speaker labels
Sentiment analysis scores for each speaker
Visual sentiment comparison chart
Download CSV export option

📊 Output Format
The application generates a structured output with:

Speaker: Identified speaker labels (SPEAKER_01, SPEAKER_02, etc.)
Start Time: Beginning timestamp of speech segment
End Time: End timestamp of speech segment
Text: Transcribed speech content
Sentiment Score: Compound sentiment score (-1 to +1 scale)
🎨 Features Overview
Transcription Engine
Powered by OpenAI Whisper (tiny model for efficiency)
Automatic speaker diarization using ScrAIbe
Precise timestamp extraction
Multi-language detection and processing
Sentiment Analysis
VADER (Valence Aware Dictionary and sEntiment Reasoner)
Compound sentiment scoring (-1 to +1 scale)
Speaker-based sentiment aggregation
Real-time sentiment visualization
User Interface
Streamlit-powered web interface
Custom CSS styling for professional appearance
Real-time processing indicators with spinner
Interactive data tables
One-click CSV download functionality
Responsive sidebar configuration
🔧 Configuration Options
Audio Settings
File Format: WAV files only
Speaker Count: 1-10 speakers (configurable via sidebar)
Language Selection: 5 supported languages
Model Configuration
Whisper Model: "tiny" (optimized for speed)
Processing: Automatic transcription with speaker diarization
Caching: Model loading cached for performance
Supported Languages
English
Spanish
French
German
Italian
📁 Project Structure
🚀 Deployment
Local Development
Streamlit Cloud
Push code to GitHub repository
Connect repository to Streamlit Cloud
Deploy with automatic dependency installation
Docker (Optional)

⚡ Performance Notes
Processing Time: Varies based on audio length (typically 1-5 minutes for 10-minute audio)
Memory Usage: Moderate RAM requirements for Whisper model
File Size Limits: Recommended maximum 100MB for optimal performance
Concurrent Users: Single-user optimization (consider scaling for production)
🐛 Troubleshooting
Common Issues
FFmpeg not found: Ensure imageio-ffmpeg is installed
Model loading errors: Check internet connection for initial model download
Audio format issues: Convert audio to WAV format before upload
Memory errors: Use smaller audio files or increase system RAM
Error Handling
Automatic cleanup of temporary files
Graceful error messages for user guidance
Model loading validation with fallback options
🤝 Contributing
Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
OpenAI Whisper for state-of-the-art speech recognition
VADER Sentiment for sentiment analysis
Streamlit for the amazing web framework
ScrAIbe for audio transcription integration
📞 Support
For questions, issues, or contributions, please:

Open an issue on GitHub
Check existing documentation
Review troubleshooting section

Built with ❤️ using Python and Streamlit


