# AI Subtitle Generator with Translation & Summarization

An intelligent web application that allows users to upload videos, automatically generates subtitles using OpenAI’s Whisper model, translates them into multiple languages, and summarizes the content using state-of-the-art NLP models.



## Tech Stack

| Layer        | Technology                                      |
|--------------|-------------------------------------------------|
| Backend      | FastAPI, Python                                 |
| Frontend     | HTML, CSS, JavaScript, Jinja2 Templates         |
| AI/ML        | OpenAI Whisper, HuggingFace Transformers (BART) |
| Video        | MoviePy                                         |
| Translation  | Google Translate API                            |


##  Features

1. Upload & Transcribe :-  
    Upload `.mp4` videos and automatically extract audio for transcription.

2. Subtitles with Word Timestamps :-
    Uses Whisper’s `word_timestamps=True` to ensure precise subtitle timing.

3. Multi-language Support :-
    Translates subtitles into 5+ languages including Hindi, French, and Spanish.

4. Smart Summarization :-
    Summarizes the spoken content using `bart-large-cnn-samsum` to create concise summaries.

5. Downloadable VTT Files :-
    All subtitle files are saved in `.vtt` format and accessible for download.

6. Interactive Web UI :-
    User-friendly frontend with video playback and subtitle selection.


## Architecture Overview

1. User uploads video
2. Audio is extracted using MoviePy
3. Speech is transcribed using Whisper
4. Word-level timestamps are used to generate VTT subtitles
5. Subtitles are optionally translated using Google Translate
6. Text is summarized using HuggingFace Transformers
7. Webpage displays video, subtitle download links, and summary


##  Project Structure

├── app.py 
├── cp_env/
├── templates/
│ └── index.html 
├── static/ 
├── requirements.txt 


##  Environment Setup

bash
# Create and activate virtual environment
python3 -m venv cp_env
.\cp_env\Scripts\activate

# Install required dependencies
pip install -r requirements.txt

# Launch the Development Server

uvicorn app:app --reload
Access the app at:-  http://127.0.0.1:8000/

# Visit in browser:

http://127.0.0.1:8000/ (Homepage)

http://127.0.0.1:8000/upload/ (Upload Endpoint)


## Supported Languages

CODE 	LANGUAGES
en	    English
es	    Spanish
fr	    French
de	    German
hi	    Hindi


## Output Files

After uploading a video:

-> Video: /static/{video_id}.mp4

-> Subtitles (VTT):

    English: /static/{video_id}_en.vtt

    Hindi: /static/{video_id}_hi.vtt

etc.

Summary: Displayed on the webpage under the video

## AI Models Used

1. Whisper (base) :-
   * OpenAI’s model for high-accuracy speech-to-text transcription 
   * Word-level timestamps enabled

2. BART Large CNN  :-
   * Used for generating concise summaries of the transcribed speech
   * HuggingFace transformer pipeline

3. Google Translate API
   * Translates subtitles into the selected target languages


##  Use Cases

1. Auto-captioning for educational content
2. Language learning tools
3. Accessible media publishing
4. Summarizing long video lectures or podcasts


##  Future Enhancements

1. Add subtitle preview overlays on the video
2. Enable language selection from the UI
3. Store processed videos in cloud (e.g., AWS S3)
4. Upgrade to larger Whisper models for improved accuracy
5. Database integration for history & analytics


##  Contact 
 Created by : Jasmeen Kaur  
 [jasmeeenkaur463@gmail.com](mailto:jasmeeenkaur463@gmail.com)  
 [LinkedIn: kaurjasmeen00](https://www.linkedin.com/in/kaurjasmeen00/)
 








