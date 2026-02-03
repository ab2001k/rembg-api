import os
from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
CORS(app) # Allows GitHub Pages to talk to this server

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if 'image' not in request.files:
        return "No image provided", 400

    file = request.files["image"]
    input_image = Image.open(file.stream)
    output = remove(input_image)

    img_io = io.BytesIO()
    output.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    # Render provides the PORT env variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
