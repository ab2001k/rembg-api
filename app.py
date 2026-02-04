# Change this line
from rembg import remove, new_session

# Use the 'u2netp' (lightweight) model session
model_name = "u2netp" 
session = new_session(model_name)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    # ... inputs ...
    # Pass the session to the remove function
    output = remove(input_image, session=session)
    # ... return ...
