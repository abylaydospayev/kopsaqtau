from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__,static_folder="assets")

# Secret key for flash messages
app.secret_key = os.environ.get('SECRET_KEY')

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')



mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject=f"New Contact Form Submission: {subject}",
                      recipients=['kopsaqtau@gmail.com'],
                       sender= email)
        msg.body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        Message: {message}
        """

        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred while sending your message. Please try again later.', 'error')

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
