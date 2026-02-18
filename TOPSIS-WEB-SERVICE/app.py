from flask import Flask, render_template, request
import os
import re
from topsis import calculate_topsis
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        # Validation
        weights_list = weights.split(',')
        impacts_list = impacts.split(',')

        if len(weights_list) != len(impacts_list):
            return "Number of weights must equal number of impacts"

        if not all(i in ['+', '-'] for i in impacts_list):
            return "Impacts must be + or - only"

        if not is_valid_email(email):
            return "Invalid email format"

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        output_file = "result.xlsx"
        calculate_topsis(filepath, weights, impacts, output_file)
        send_email(email, output_file)

        return "Result has been sent to your email successfully!"

    return render_template("index.html")

def send_email(receiver, attachment):
    sender = "your_real_mail.com"
    password = "16digitcode"

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Please find attached TOPSIS result.")

    with open(attachment, "rb") as f:
        msg.add_attachment(f.read(), maintype="application",
                           subtype="octet-stream", filename="result.xlsx")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)

