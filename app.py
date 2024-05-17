from flask import *
import cv2
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key="super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(filename,operation):
    image=cv2.imread(f"uploads/{filename}")
    file_front_name=filename.split('.')[0]
    match operation:
        case "jpg":
            img_processed_path=f"static/{file_front_name}.{operation}"
            print(img_processed_path)
            cv2.imwrite(img_processed_path,image)
        case "png":
            img_processed_path = f"static/{file_front_name}.{operation}"
            print(img_processed_path)
            cv2.imwrite(img_processed_path, image)
        case "webp":
            img_processed_path = f"static/{file_front_name}.{operation}"
            print(img_processed_path)
            cv2.imwrite(img_processed_path, image)
        case "tiff":
            img_processed_path = f"static/{file_front_name}.{operation}"
            print(img_processed_path)
            cv2.imwrite(img_processed_path, image)
        case "pbm":
            img_processed_path = f"static/{file_front_name}.{operation}"
            print(img_processed_path)
            cv2.imwrite(img_processed_path, image)
        case "bmp":
            img_processed_path = f"static/{file_front_name}.{operation}"
            
            cv2.imwrite(img_processed_path, image)
    return img_processed_path


@app.route("/")
def Frontpage():
    return render_template("index.html")
@app.route("/edit", methods=["GET","POST"])
def edit():
    if request.method == 'POST':
        operation=request.form.get("operation")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "Error wrong file type received"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "Error no file received"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filename1=process_image(filename,operation)
            flash(f"your image has been processed and is available in <a href='{filename1}'> HERE</a>")

    return render_template("index.html")
# if __name__ == '__main__':
#     app.run(debug=True)
