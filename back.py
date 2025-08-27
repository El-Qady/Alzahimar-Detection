import os
from flask import Flask, render_template, request, redirect, url_for, flash
from AI_models import img_processing, img_prediction, classification_name

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.secret_key = '1234dddfffee---l'  # Replace '1234dddfffee---l' with a strong, unique key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file was uploaded. Please try again!', 'warning')  # Flash a warning message
        # return redirect(request.url)  # Redirect to the upload page
        return render_template("index.html")
    
    file = request.files['file']
    
    # If no file is selected
    if file.filename == '':
        flash('No selected file. Please choose a file to upload!', 'warning')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # create message depending on the classification result
        message = {
            0: """
                Stay mentally active with puzzles, reading, or learning new skills to help preserve cognitive function.
                    \nMaintain a structured daily routine to minimize confusion or frustration.
                    \nExercise regularly (e.g., walking, yoga) to support brain health and overall well-being.
                    \nFocus on a brain-healthy diet, such as the Mediterranean diet, which includes fruits, vegetables, whole grains, fish, and nuts.
                    \nSet reminders or use tools like calendars, alarms, or smartphone apps to stay organized.""",
            1: """
                \nPrioritize activities that bring joy and familiarity, such as listening to favorite music or reminiscing over photos.
                \nUse simplified tools for communication, such as picture boards, or practice verbal cues if memory fades.
                \nAttend regular medical checkups to monitor health changes and adapt care plans.
                \nStick to low-stress environments to reduce agitation.""",
            2: """
            \nContinue prioritizing brain health with a balanced diet, regular exercise, and quality sleep.
            \nStay socially active and maintain strong connections with family and friends.
            \nChallenge your brain by learning new skills or hobbies, like playing a musical instrument or solving puzzles.
            \nAvoid smoking and limit alcohol consumption to support cognitive health.
            \nGet regular health screenings, especially for cardiovascular risk factors like high blood pressure or diabetes, as these are linked to dementia risk.
            """,
            3:"""
                \nFocus on lifestyle changes that support cognitive health, such as regular physical activity and mental exercises.
                \nKeep stress levels low with relaxation techniques like meditation or deep breathing exercises.
                \nFoster strong social connections by joining community activities or spending time with loved ones.
                \nUse memory aids, like sticky notes or smartphone apps, for minor forgetfulness."""
        }
        
        processed_img = img_processing(filename)
        print(processed_img)
        classification_number = img_prediction(processed_img)
        classification_output_name = classification_name(classification_number)
        print(classification_output_name)
        print(classification_number)
        return render_template("index.html", fname=file.filename, res=classification_output_name, message = message[classification_number])
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)