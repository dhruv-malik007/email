from flask import Flask, request, render_template
from flask_mail import Mail, Message
import logging

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,  
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,  
    MAIL_USERNAME='dhruv3777@gmail.com', 
    MAIL_PASSWORD="qxfd qtqu mfkv ymzh", 
    MAIL_DEFAULT_SENDER='dhruv3777@gmail.com'
)


mail = Mail(app)

logging.basicConfig(level=logging.INFO)



@app.route('/signup', methods=['POST'])
def signup():
    user_email = request.form.get('email')
    user_name = request.form.get('name')
    user_mobile = request.form.get('mobile')
    password = request.form.get("password")

    try:
        msg = Message("Welcome to ACN", recipients=[user_email])
        msg.html = render_template("index.html", user_name=user_name,user_mobile=user_mobile,user_email=user_email)
        mail.send(msg)
        logging.info(f"Email sent successfully to {user_email}")
        return "Signup successful, email sent!"
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        return "Signup successful, but failed to send email."

if __name__ == '__main__':
    app.run(debug=True)
