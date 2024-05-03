# Import necessary libraries and modules
from flask import Flask, render_template, request, Response
import cv2
import requests
import numpy as np
import time
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from refresh import Refresh  # Assuming this is a custom module for refreshing Spotify token
import mecre
import random

# Define the list of emotion labels
emotion_labels = ['Angry', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Initialize Flask app
app = Flask(__name__)

# Initialize Opepython nCV camera
camera = cv2.VideoCapture(0)

# Load Haar cascade for face detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load emotion detection model
classifier = load_model('fer.h5')

# Function to obtain Spotify token
def get_spotify_token():
    print("Refreshing token...")
    refreshCaller = Refresh()
    return refreshCaller.refresh()

# Global variable to store the Spotify token
spotify_token = get_spotify_token()

# Function to generate video frames
def generate_frames():
    global label  # Use the global variable to store emotion label
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            capture_duration = 5
            start_time = time.time()
            while int(time.time() - start_time) < capture_duration:
                _, frame = camera.read()
                frame = cv2.flip(frame, 1)
                labels = []
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

                    if np.sum([roi_gray]) != 0:
                        roi = roi_gray.astype('float') / 255.0
                        roi = img_to_array(roi)
                        roi = np.expand_dims(roi, axis=0)
                        prediction = classifier.predict(roi)[0]
                        label = emotion_labels[prediction.argmax()]  # Set the global variable
                        label_position = (x, y)
                        cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        print(label)
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                cv2.waitKey(0)
                yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n\r\n')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for streaming video frames
@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for managing playlists and rendering results
# Route for managing playlists and rendering results
@app.route('/result', methods=["POST", "GET"])
# Route for managing playlists and rendering results
@app.route('/result', methods=["POST", "GET"])
def playlistmanager():
    option = request.form['btnradio']
    print("Option is " + option)
    try:
        input_emotion = label  # Use the global variable for detected emotion
    except NameError:
        return Response("Emotion was not detected properly")
    else:
        print("Emotion detected:", input_emotion)

        # Determine playlist_id based on input_emotion and option
        if input_emotion == 'Happy':
            playlist_id = secret.happy if option == "video" else secret.mhappy
        elif input_emotion == 'Sad':
            playlist_id = secret.sad if option == "video" else secret.msad
        elif input_emotion == 'Neutral':
            playlist_id = secret.neutral if option == "video" else secret.mneutral
        elif input_emotion == 'Angry':
            playlist_id = secret.angry if option == "video" else secret.mangry
        elif input_emotion == 'Surprise':
            playlist_id = secret.surprise if option == "video" else secret.msurprise
        elif input_emotion == 'Fear':
            playlist_id = secret.fear if option == "video" else secret.mfear
        else:
            return Response("Enter valid keyword")

        if option == "video":
            search_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
            search_params = {
                'key': secret.youtube_key,
                'playlistId': playlist_id,
                'part': 'contentDetails',
                'maxResults': 10,
            }
                                        
            r = requests.get(search_url, params=search_params)
            response_json = r.json()
            print(response_json)  # Print the response JSON for review

            results = response_json.get('items', [])
            video_ids = [result['contentDetails']['videoId'] for result in results]
            
            return render_template('results.html', input=input_emotion, video_ids=video_ids, quote=random.choice(secret.emotion_quotes[input_emotion]), constant_message=secret.constant_messages[input_emotion])

            #return render_template('results.html', input=input_emotion, video_ids=video_ids, quote=random.choice(emotion_quotes[input_emotion]))
        else:
            print("Refreshing Spotify token...")
            global spotify_token  # Use the global variable for Spotify token
            spotify_token = get_spotify_token()  # Refresh Spotify token
            print("New Spotify token:", spotify_token)

            query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
            headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(spotify_token)}
            response = requests.get(query, headers=headers)
            response_json = response.json()
            print(response_json)  # Print the response JSON for review

            response_items = response_json.get('items', [])
            music_ids = [music['track']['id'] for music in response_items]
            

            return render_template('music.html', input=input_emotion, music_ids=music_ids, quote=random.choice(secret.emotion_quotes[input_emotion]), constant_message=secret.constant_messages[input_emotion])


if __name__ == '__main__':
    app.run(debug=True)
