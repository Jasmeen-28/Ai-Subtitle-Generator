
# 🎬 AI Subtitle Generator with Translation & Summarization

An intelligent web application that allows users to upload videos, automatically generate accurate subtitles using OpenAI’s Whisper model, translate them into multiple languages, and summarize the content using advanced NLP models.

---

## 🧰 Tech Stack

| Layer        | Technology                                      |
|--------------|-------------------------------------------------|
| Backend      | FastAPI, Python                                 |
| Frontend     | HTML, CSS, JavaScript, Jinja2 Templates         |
| AI/ML        | OpenAI Whisper, HuggingFace Transformers (BART) |
| Video        | MoviePy                                         |
| Translation  | Google Translate API                            |

---

## ✨ Features

- **Upload & Transcribe**  
  Upload `.mp4` videos and automatically extract audio for transcription.

- **Subtitles with Word Timestamps**  
  Uses Whisper’s `word_timestamps=True` to ensure precise subtitle timing.

- **Multi-language Support**  
  Subtitles are translated into 5+ languages including Hindi, French, and Spanish.

- **Smart Summarization**  
  Spoken content is summarized using the `bart-large-cnn-samsum` model for quick insights.

- **Downloadable VTT Files**  
  Subtitle files are saved in `.vtt` format and available for download.

- **Interactive Web UI**  
  User-friendly interface for video playback, language selection, and summary display.

---

## 🏗️ Architecture Overview

1. User uploads a video via web interface
2. Audio is extracted using **MoviePy**
3. Transcription is performed using **OpenAI Whisper**
4. Word-level timestamps are used to generate `.vtt` subtitle files
5. Subtitles are optionally translated using **Google Translate API**
6. Content is summarized using **HuggingFace Transformers**
7. Webpage displays video player, subtitles, and summary dynamically

---

## 📁 Project Structure

```
├── app.py 
├── venv/
├── templates/
│   └── index.html 
├── static/
├── requirements.txt
```

---

## ⚙️ Environment Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 🚀 Run the Application

```bash
uvicorn app:app --reload
```

### 🔗 Access in Browser

- Homepage: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Upload Endpoint: [http://127.0.0.1:8000/upload/](http://127.0.0.1:8000/upload/)

---

## 🌍 Supported Languages

| Code | Language |
|------|----------|
| en   | English  |
| es   | Spanish  |
| fr   | French   |
| de   | German   |
| hi   | Hindi    |

---

## 📤 Output Files

After a successful upload:

- Video File: `/static/{video_id}.mp4`
- Subtitles:
  - English: `/static/{video_id}_en.vtt`
  - Hindi: `/static/{video_id}_hi.vtt`
  - Others similarly structured
- Summary: Displayed beneath the video player

---

## 🤖 AI Models Used

1. **OpenAI Whisper (Base)**  
   - High-accuracy speech-to-text transcription  
   - Word-level timestamps enabled

2. **BART Large CNN**  
   - Used for generating concise summaries  
   - Implemented via HuggingFace Transformers

3. **Google Translate API**  
   - Converts subtitles to selected languages

---

## 🧠 Use Cases

- Auto-captioning for educational content  
- Language learning tools  
- Accessible media publishing  
- Summarizing long lectures, podcasts, or interviews

---

## 🔮 Future Enhancements

- Add subtitle preview overlays directly on the video
- Enable live language switching in the UI
- Cloud storage support (e.g., AWS S3)
- Upgrade to Whisper Large for enhanced accuracy
- Integrate a database to store videos, summaries, and analytics

---

## 📞 Contact

**Created by:** Jasmeen Kaur  
📧 [jasmeeenkaur463@gmail.com](mailto:jasmeeenkaur463@gmail.com)  
🔗 [LinkedIn: kaurjasmeen00](https://www.linkedin.com/in/kaurjasmeen00/)

---
