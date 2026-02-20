from faster_whisper import WhisperModel

# 1. Initialize the model
# Use 'cuda' if you have an NVIDIA GPU, or 'cpu' for standard processors.
model_size = "large-v3-turbo"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

# 2. Run transcription
# beam_size=5 provides high accuracy; vad_filter removes silence gaps.
segments, info = model.transcribe(
    "Capstone_Jail_Call.mp3", 
    beam_size=5, 
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=500)
)

print(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")

# 3. Process and print segments
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")