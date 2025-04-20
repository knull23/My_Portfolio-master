from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                subject = f"Message from {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                email_message = f"Subject: {subject}\n\n{body}"
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=email_message
                )
            print(f"Email sent successfully from {name} ({email})!")
        except Exception as e:
            print(f"Error while sending email: {e}")

        # Redirect to home after submission
        return redirect(url_for('home'))

    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

if __name__ == '__main__':
    app.run(debug=True)


