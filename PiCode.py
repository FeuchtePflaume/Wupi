import os
import time
import requests

# Kamera-Settings
camera = "raspistill"
image_path = "/home/pi/image.jpg"

# Server-Settings
server_ip = "http://server-ip:8080"


# Funktion zum Bildaufnehmen und -senden
def send_image():
    # Bild aufnehmen
    os.system(f"{camera} -o {image_path}")

    # Bild an Server senden
    with open(image_path, "rb") as image_file:
        response = requests.post(f"{server_ip}/upload", files={"image": image_file})

    # Warten auf nächstes Bild
    time.sleep(60)


# Funktion zum Bildaufnehmen und -zurückliefern
@app.route("/image", methods=["GET"])
def get_image():
    # Bild aufnehmen
    os.system(f"{camera} -o {image_path}")

    # Bild zurückliefern
    with open(image_path, "rb") as image_file:
        return image_file.read()


# Hauptprogramm
if __name__ == "__main__":
    while True:
        send_image()