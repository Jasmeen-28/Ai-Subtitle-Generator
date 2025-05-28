from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from moviepy.editor import VideoFileClip
import os, uuid, shutil, tempfile, datetime
import whisper
from googletrans import Translator
from transformers import pipeline

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "static"
os.makedirs(UPLOAD_DIR, exist_ok=True)

LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'hi': 'Hindi',
}

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "video_url": None})

@app.post("/upload/", response_class=HTMLResponse)
async def upload_video(request: Request, file: UploadFile = File(...)):
    video_id = str(uuid.uuid4())
    temp_video_path = os.path.join(tempfile.gettempdir(), f"{video_id}.mp4")

    with open(temp_video_path, "wb") as temp_file:
        shutil.copyfileobj(file.file, temp_file)

    audio_path = os.path.join(tempfile.gettempdir(), f"{video_id}.wav")
    with VideoFileClip(temp_video_path) as video:
        video.audio.write_audiofile(audio_path, logger=None)

    model = whisper.load_model("base")
    result = model.transcribe(audio_path, word_timestamps=True)
    segments = result.get("segments", [])

    def format_timestamp(seconds):
        td = datetime.timedelta(seconds=seconds)
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        secs = total_seconds % 60
        milliseconds = int((td.total_seconds() - total_seconds) * 1000)
        return f"{hours:02}:{minutes:02}:{secs:02}.{milliseconds:03}"

    def generate_vtt(segments, lang_code='en', translate=False, window_size=4):
        translator = Translator()
        vtt_lines = ["WEBVTT\n"]
        cue_index = 1
        words = []
        for segment in segments:
            words.extend(segment.get("words", []))

        for i in range(len(words)):
            start = words[i]["start"]
            end = words[min(i + window_size - 1, len(words) - 1)]["end"]
            window_words = words[i:i + window_size]
            if i > 0:
                text = " ".join(
                    f"<b>{w['word'].strip()}</b>" if j == len(window_words) - 1 else w['word'].strip()
                    for j, w in enumerate(window_words)
                )
                if translate:
                    try:
                        text = translator.translate(text, dest=lang_code).text
                    except:
                        pass
                start_str = format_timestamp(start)
                end_str = format_timestamp(end)
                vtt_lines.append(str(cue_index))
                vtt_lines.append(f"{start_str} --> {end_str}")
                vtt_lines.append(text + "\n")
                cue_index += 1

        return "\n".join(vtt_lines)

    # Save VTT subtitle files
    vtt_filenames = {}
    for lang_code in LANGUAGES:
        translated = lang_code != 'en'
        vtt_content = generate_vtt(segments, lang_code, translate=translated)
        filename = f"{video_id}_{lang_code}.vtt"
        with open(os.path.join(UPLOAD_DIR, filename), "w", encoding="utf-8") as f:
            f.write(vtt_content)
        vtt_filenames[lang_code] = filename

    # Save video file to static
    static_video_path = os.path.join(UPLOAD_DIR, f"{video_id}.mp4")
    shutil.copy(temp_video_path, static_video_path)

    # Cleanup
    os.remove(audio_path)
    os.remove(temp_video_path)

    # Generate summary
    full_text = " ".join(segment["text"] for segment in segments)

    def split_text(text, max_tokens=500):
        words = text.split()
        return [" ".join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]

    summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
    chunks = split_text(full_text)
    summaries = []
    for chunk in chunks:
        try:
            summary = summarizer(chunk, max_length=80, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        except:
            summaries.append("[Summary failed]")

    summary_text = " ".join(summaries)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "video_url": f"/static/{video_id}.mp4",
        "video_id": video_id,
        "languages": LANGUAGES,
        "summary_text": summary_text
    })
