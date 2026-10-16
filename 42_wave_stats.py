"""Report duration and amplitude statistics for 16-bit PCM WAV files."""
import sys
import wave
from array import array

def analyze(path: str):
    with wave.open(path, "rb") as audio:
        channels = audio.getnchannels()
        sample_rate = audio.getframerate()
        width = audio.getsampwidth()
        frames = audio.readframes(audio.getnframes())
    if width != 2:
        raise ValueError("This example supports 16-bit PCM WAV files")
    samples = array("h")
    samples.frombytes(frames)
    peak = max((abs(sample) for sample in samples), default=0)
    rms = (sum(sample * sample for sample in samples) / len(samples)) ** 0.5 if samples else 0.0
    return {
        "channels": channels,
        "sample_rate": sample_rate,
        "frames": len(samples) // channels if channels else 0,
        "duration_seconds": len(samples) / (sample_rate * channels) if sample_rate and channels else 0,
        "peak": peak,
        "rms": round(rms, 2),
    }

if __name__ == "__main__":
    print(analyze(sys.argv[1]))
