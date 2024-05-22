import os
from pydub import AudioSegment

def convert_sample_rate(input_path, output_path, desired_sample_rate):
    try:
        audio = AudioSegment.from_file(input_path)
        audio = audio.set_frame_rate(desired_sample_rate)
        audio.export(output_path, format="wav")
        print(f"Converted {input_path} to {output_path} with sample rate {desired_sample_rate} Hz")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def process_files_in_directory(input_directory, output_directory, desired_sample_rate):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file in os.listdir(input_directory):
        if file.endswith(".wav"):
            input_path = os.path.join(input_directory, file)
            output_path = os.path.join(output_directory, f"{os.path.splitext(file)[0]}.wav")
            convert_sample_rate(input_path, output_path, desired_sample_rate)

if __name__ == "__main__":
    input_directory = "/media/d4rk0n3/Project/AI/Voice-Cloning/training/Jarvis/wav"  # Change this to your input directory
    output_directory = "/opt/PiperTTS/Jarvis/wav"  # Change this to your output directory
    desired_sample_rate = 22050  # Change this to your desired sample rate
    process_files_in_directory(input_directory, output_directory, desired_sample_rate)
