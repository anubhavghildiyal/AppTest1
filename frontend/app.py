from flask import Flask, request, jsonify
import face_detection_module  # Import your face detection module here

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    
    image_file = request.files['image']
    # Call your face detection function with the image_file
    # detected_faces = face_detection_module.detect_faces(image_file)
    
    # Assuming detected_faces is a list of face coordinates (x, y, width, height)
    # You can process the detected faces here
    
    # Return the detected faces as JSON response
    return jsonify({'faces': detected_faces})

if __name__ == '__main__':
    app.run(debug=True)
 
