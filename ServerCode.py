import os
import cv2
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify
from tesseract import Tesseract

app = Flask(__name__)

# Tesseract-OCR-Settings
tesseract = Tesseract()

# OpenCV-Settings
cv2.namedWindow("Wasseruhr", cv2.WINDOW_NORMAL)

# Datenbank-Settings
db_path = "/home/server/data.db"


# Funktion zum Bildverarbeiten
def process_image(image_path):
    # Bild lesen
    image = cv2.imread(image_path)

    # Texterkennung
    text = tesseract.image_to_text(Image.open(image_path))

    # Zeigererkennung
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200, minLineLength=100, maxLineGap=10)

    # Daten speichern
    with open(db_path, "a") as db_file:
        db_file.write(f"{text}\n")

    return text


# Funktion zum Bildupload
@app.route("/upload", methods=["POST"])
def upload_image():
    image_file = request.files["image"]
    image_path = "/home/server/image.jpg"
    image_file.save(image_path)

    # Bild verarbeiten
    text = process_image(image_path)

    return jsonify({"success": True, "text": text})


# Funktion zum Bildmachen
@app.route("/make_image", methods=["POST"])
def make_image():
    # Bild vom Raspberry Pi anfordern
    response = requests.get("http://raspberry-pi-ip:8080/image")
    image_data = response.content

    # Bild speichern
    with open("/home/server/image.jpg", "wb") as image_file:
        image_file.write(image_data)

    return jsonify({"success": True})


# Funktion zum Cron-Job
def cron_job():
    # Bild vom Raspberry Pi anfordern
    response = requests.get("http://raspberry-pi-ip:8080/image")
    image_data = response.content

    # Bild speichern
    with open("/home/server/image.jpg", "wb") as image_file:
        image_file.write(image_data)

    # Bild verarbeiten
    text = process_image("/home/server/image.jpg")

    return text


# Hauptprogramm
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)