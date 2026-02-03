from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    file = request.files["image"]
    input_image = Image.open(file.stream)

    output = remove(input_image)

    img_io = io.BytesIO()
    output.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")

@app.route("/")
def home():
    return "rembg API is running"

if __name__ == "__main__":
    app.run()
