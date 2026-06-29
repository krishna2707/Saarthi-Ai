import sounddevice as sd
import io
import soundfile as sf
from sarvamai import SarvamAI
from config import SARVAM_API_KEY

client = SarvamAI(api_subscription_key=SARVAM_API_KEY)
def speak(input):
    chunks = []
    for chunk in client.text_to_speech.convert_stream(
        text=input,
        target_language_code="hi-IN",
        speaker="shubh",
        model="bulbul:v3",
        output_audio_codec="wav",
    ):
        chunks.append(chunk)

    audio_bytes = b"".join(chunks)


    audio, sample_rate = sf.read(io.BytesIO(audio_bytes), dtype="float32")

        # Play
    sd.play(audio, sample_rate)
    sd.wait()