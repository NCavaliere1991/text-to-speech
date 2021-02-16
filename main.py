import PyPDF2
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/path/to/file.json')

with open("pdf file", 'rb') as pdf_file:
    file_reader = PyPDF2.PdfFileReader(pdf_file)
    count = file_reader.numPages
    for i in range(count):
        text = ""
        page = file_reader.getPage(i)
        text += page.extractText()

def synthesize_text(text):
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient(credentials=credentials)

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

synthesize_text(text)
