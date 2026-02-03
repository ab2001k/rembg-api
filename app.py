from flask import Flask, request, send_file
from flask_cors import CORS  # Import CORS
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if 'image' not in request.files:
        return "No image provided", 400
        
    file = request.files["image"]
    
    # Convert file to Image
    input_image = Image.open(file.stream)

    # Remove background
    output = remove(input_image)

    # Save to buffer
    img_io = io.BytesIO()
    output.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")

@app.route("/")
def home():
    return "Local Rembg API is running!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
