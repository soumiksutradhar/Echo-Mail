from flask import Flask, request, jsonify
import smtplib
import csv
import os
import boto3
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define the upload folder for the CSV file
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/send-emails', methods=['POST'])
def send_emails():
    data = request.get_json()
    
    # Extract data from the request
    bucket = data['bucket']
    key = data['key']
    filename = data['filename']
    sender_email = data['sender_email']
    sender_password = data['sender_password']
    subject = data['subject']
    body = data['body']
    
    # Download the file from S3
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    if allowed_file(filename):
        # Read the CSV file and send emails
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                recipient_email = row[1]
                if '@' in recipient_email:
                    try:
                        # Set up the SMTP server
                        if 'outlook.com' in sender_email:
                            host = 'smtp-mail.outlook.com
                            port = 587
                        elif 'gmail.com' in sender_email:
                            host = 'smtp.gmail.com'
                            port = 587

                        smtp = smtplib.SMTP(host, port)
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.login(sender_email, sender_password)

                        # Send the email
                        msg = f'Subject: {subject}\n\n{body}'
                        smtp.sendmail(sender_email, recipient_email, msg)
                        smtp.quit()
                        print(f'Email sent to {recipient_email}')
                    except Exception as e:
                        print(f'Error sending email to {recipient_email}: {str(e)}')

        return jsonify({'message': 'Emails sent successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
