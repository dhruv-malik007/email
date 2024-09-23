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
logo1= "https://drive.google.com/uc?export=view&id=1Edu4KW3Zp1lrb5j4n_V2BEhxfcLgjEKV"
logo2= "https://drive.google.com/uc?export=view&id=1bwsXnUn7JpAkZ71dH5KlRk5IrP4YlYRC"
img1= "https://drive.google.com/uc?export=view&id=1wS3mc5R1-e0h8wZEF5LIzocGLhqSYXi2"
img2= "https://drive.google.com/uc?export=view&id=1t9IHDwlESONPjTWkE7C9cPI-mmunSjyX"
img3= "https://drive.google.com/uc?export=view&id=1uFr4mg-W7zrP_NE0mkfcG08DIIW9aIQ_"
@app.route('/signup', methods=['POST'])
def signup():
    user_email = request.form.get('email')
    user_name = request.form.get('name')
    user_mobile = request.form.get('mobile')
    password = request.form.get("password")

    try:
        msg = Message("Welcome to ACN", recipients=[user_email])
        msg.html = render_template("index.html", user_name=user_name,user_mobile=user_mobile,user_email=user_email,logo1=logo1,logo2=logo2,img1=img1,img2=img2,img3=img3)
        mail.send(msg)
        logging.info(f"Email sent successfully to {user_email}")
        return "Signup successful, email sent!"
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        return "Signup successful, but failed to send email."

if __name__ == '__main__':
    app.run(debug=True)
