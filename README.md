# WilCo Speech-to-Text Transcription
## ****Read Description***
This project provides a simple interface for transcribing audio files to text using the Whisper model via the `faster-whisper` library.

## Features
- High-accuracy speech-to-text transcription
- Language detection
- Silence gap removal (VAD filtering)

## Requirements
- Python 3.8+
- macOS, Linux, or Windows
- (Optional) NVIDIA GPU for faster inference

## Installation
1. Clone this repository:
   ```zsh
   git clone <repo-url>
   cd WilCo_Project
   ```
2. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   ```

## Usage
1. Place your audio file (e.g., `your_audio_file.wav`) in the project directory.
2. Run the transcription script:
   ```zsh
   python speech-to-text.py
   ```
3. The script will print the detected language and the transcribed segments with timestamps.

### Customization
- To use a different audio file, change the filename in `speech-to-text.py`:
  ```python
  segments, info = model.transcribe(
      "your_audio_file.wav",  # Change this to your file
      beam_size=5,
      vad_filter=True,
      vad_parameters=dict(min_silence_duration_ms=500)
  )
  ```
- To use GPU, change `device="cpu"` to `device="cuda"` in the script.

## Model Files
- The model will be automatically downloaded and cached by `faster-whisper`.
- You can store custom models in `models/whisper-turbo/` if needed.

## License
MIT

# WilCo_Project: Local Voice-to-Text Transcriber

## Project Overview
This project provides a fully local, secure, and multilingual voice-to-text transcription service. Designed for high-security environments, it processes audio data entirely on-device using the `faster-whisper` engine and the `large-v3-turbo` model.

**Key Features:**
* **Privacy First:** No data is sent to external APIs or cloud services.
* **Multilingual:** Supports over 99 languages with automatic detection.
* **High Performance:** Utilizes CTranslate2 for 4x faster inference than standard Whisper models.

---

## Directory Structure

```text
WilCo_Project/
├── .venv/                  # Virtual environment (ignored by Git)
├── models/
│   └── whisper-turbo/      # Local model weights (large-v3-turbo)
├── speech-to-text.py       # Main transcription script
└── README.md               # Documentation
```

## Setup & Installation

1. Environment Setup
It is recommended to use a Python virtual environment to manage dependencies.

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install required libraries
pip install faster-whisper huggingface_hub
```

2. Local Model Download
To ensure the transcriber runs fully local without requiring a Hugging Face token at runtime, download the model weights into the project directory:

```bash
# Create the local directory
mkdir -p models/whisper-turbo

# Run the download script (or CLI command)
python3 -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Systran/faster-whisper-large-v3-turbo', local_dir='models/whisper-turbo', local_dir_use_symlinks=False)"
```

## Usage
Run the main script to begin transcription. Ensure your .venv is active.

```bash
python3 speech-to-text.py
```

## Configuration
In `speech-to-text.py`, the model is initialized from the local path:

```python
model = WhisperModel("./models/whisper-turbo", device="cuda", compute_type="float16")
```

- Device: Change to "cpu" if an NVIDIA GPU is not available.
- Compute Type: Use "int8" to save memory on lower-end hardware.

## Security & Privacy
This application is designed to be air-gapped ready. Once the initial model download is complete, the application requires zero internet connectivity. No audio files, transcripts, or metadata are ever transmitted off the local machine.

---

### Tips for "Constant Updates"
* **Version Control:** Whenever you add a new feature (like real-time mic support or a GUI), immediately add a "New Feature" section or update the "Usage" section.
* **Requirements.txt:** As your project grows, run `pip freeze > requirements.txt`. This allows others to install all your dependencies with one command: `pip install -r requirements.txt`.

**Would you like me to help you add a "Troubleshooting" section to the README to cover# WilCo-AIDev-Capstone
