from flask import Flask, request, jsonify
import whisper
import os
import subprocess

app = Flask(__name__)

@app.route('/process-video', methods=['POST'])
def process_video():
    # Placeholder: Receive video file, transcribe, and edit
    return jsonify({"message": "Video received and will be processed"}), 200

if __name__ == '__main__':
    app.run(debug=True)
