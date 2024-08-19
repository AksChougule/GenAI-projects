import assemblyai as aai
import threading

# Set your API key
aai.settings.api_key = "my-api-key"

# Define callback functions
def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session ID:", session_opened.session_id)

def on_data(transcript: aai.RealtimeTranscript):
    if transcript.text:
        if isinstance(transcript, aai.RealtimeFinalTranscript):
            print(transcript.text, end="\r\n")

def on_error(error: aai.RealtimeError):
    print("An error occurred:", error)

def on_close():
    print("Closing Session")

# Initialize the transcriber
transcriber = aai.RealtimeTranscriber(
    on_data=on_data,
    on_error=on_error,
    sample_rate=16_600,
    on_open=on_open, 
    on_close=on_close, 
)

# Function to stop the stream after a certain duration
def stop_recording():
    print("Timer expired, stopping recording")
    transcriber.close()

# Set the duration for recording (in seconds)
duration = 10  # For example, record for 10 seconds

# Create a timer that will call `stop_recording` after the specified duration
timer = threading.Timer(duration, stop_recording)

# Start the connection
transcriber.connect()

# Open the microphone stream
microphone_stream = aai.extras.MicrophoneStream(sample_rate=16_600)

# Start the timer
timer.start()

# Start streaming from the microphone
try:
    transcriber.stream(microphone_stream)
except KeyboardInterrupt:
    print("Recording aborted by user")

# Ensure the transcriber is closed
transcriber.close()
