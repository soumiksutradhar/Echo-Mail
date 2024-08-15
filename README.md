# ECHO-MAIL

> ECHO-MAIL is a mass mailing solution that leverages AWS services to efficiently send emails at scale.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Test Event](#test-event)

## Overview

ECHO-MAIL is designed for sending bulk emails efficiently using AWS resources (`Lambda`, `S3`, `EC2`). The project is built to scale, ensuring that emails are delivered reliably.


## Architecture

1. **AWS Lambda**: Handles the business logic for sending emails. A request layer is included in the Lambda function to process API requests.
2. **AWS S3**: Stores email templates, configurations, or any other relevant assets.
3. **AWS EC2**: Runs the SMTP server, handling email transmission.
4. **SMTP Protocol**: Used for sending emails from the EC2 instance.
5. **API Gateway**: Provides a RESTful API interface for interacting with the Lambda function.

## Prerequisites

- AWS Account
- AWS CLI installed and configured
- Basic knowledge of AWS services (Lambda, S3, EC2, API Gateway)
- Docker (optional, if using Docker for local testing)

## Setup

- Clone the Repository
```bash
git clone https://github.com/Atul-Kumar-Rana/Echo-Mail.git
cd Echo-Mail
```

## AWS Configuration

### EC2 

1. **Launch an EC2 Instance**: Choose an appropriate instance type and configure security groups to allow `SMTP` (port 25), `HTTP` (port 80), and traffic on port 5000.

2. **Change Inbound Rules**:
   - Update the inbound rules of the security group associated with the EC2 instance to allow traffic on the ports mentioned.
   
     ![Screenshot 2024-08-05 231112](https://github.com/user-attachments/assets/29fe48af-0c68-40fd-ab5c-7b5773311f8e)


3. **Install Packages**:
   
   ```bash
   sudo apt-get update && upgrade
   sudo apt-get install python3.10-venv
   ```
   
4. **Setup Python venv and Script**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install boto3 flask
   touch EC2_code.py
   ```
   
   Copy the contents of `EC2_code.py` from the repository with any code editor (vim, nano etc.).
     
   ```bash
   python3 EC2_code.py
   ```

   Run the `EC2_code.py` to start the SMTP server and the associated Flask API to listen for incoming requests.

   ![Screenshot 2024-08-05 181502](https://github.com/user-attachments/assets/6b99fe9c-4a17-45c5-a340-0766bdfcb724)


#### Lambda Setup

1. **Configure IAM Roles**:
   - Create an IAM role for Lambda with the following permissions:
     - Access to S3 for retrieving email templates.
     - Permissions to send logs to CloudWatch.
     - Any other permissions required by your Lambda function.

2. **Attach IAM Role to Lambda**:
   - Attach the IAM role to your Lambda function to grant it the necessary permissions.

3. **Attach Request Layer**:
   - **Upload `requests_layer.zip`**:
     - Go to the AWS Lambda console.
     - Select your Lambda function.
     - Navigate to the "Layers" section and click "Add a layer."
     - Choose "Upload a .zip file" and upload the `requests_layer.zip` file from your repository.
     - Configure the layer and add it to your Lambda function.

4. **Set Up API Gateway**:
   - Create a new API in API Gateway.
   - Set up a resource and method (e.g., POST) to trigger the Lambda function.
   - Deploy the API and note the endpoint URL for testing.

5. **Configure Lambda Environment Variables**:
   - The necessary environment variables are already defined within the Lambda function code. These variables should be configured in the Lambda environment settings:
     - `SMTP_HOST`
     - `SMTP_USER`
     - `SMTP_PASS`
     - `Subject`
     - `body`
    
   To set these environment variables in AWS Lambda:
   1. Go to the AWS Lambda console.
   2. Select your Lambda function.
   3. Navigate to the "Configuration" tab and select "Environment variables."
   4. Add the key-value pairs for `SMTP_HOST`,`SMTP_USER`, `SMTP_PASS`, `Subject` , and `body`.

## Usage

1. **Upload Email Templates**: Place your email templates in the S3 bucket.
2. **Trigger Lambda Function**:
   - Use API Gateway to call the Lambda function with the appropriate HTTP request.
   - Alternatively, trigger Lambda via other events (e.g., scheduled CloudWatch event).
3. **Monitor Email Sending**: Logs and metrics can be monitored in CloudWatch to ensure successful email delivery.

## Test Event

To test the Lambda function, you can use the test event JSON file provided in the repository. Follow these steps:

1. **Attach the Test Event**:
   - Go to your Lambda function in the AWS Management Console.
   - Click on "Test" and then "Configure test event."
   - Upload the test event JSON file (`TestEvent.json`) from the repository.
  
2. **Run the Test**:
   - Click on the "Test" button to trigger the Lambda function with the provided test event.
   - Check the output and CloudWatch logs to ensure everything is working correctly.

As we send a PUT request through the API gateway, it will upload the file to S3 and trigger the Lambda function.

### File Uploading     

`CSV file Format`

![Screenshot 2024-08-15 153025](https://github.com/user-attachments/assets/db4ef39f-e383-4c59-81e9-5a1cad4222d2)

### Lambda Output

![Screenshot 2024-08-06 195725](https://github.com/user-attachments/assets/71fc8f45-ca41-405d-8d77-6c906b2d71f7)

### EC2 Console Output

![Screenshot 2024-08-07 164501](https://github.com/user-attachments/assets/347e4265-b6a4-45d3-b6ee-5d1739a1092d)


## Roadmap

- [x] Core Functionality
- [x] UI Design
- [ ] Application Dashboard
- [ ] Mailing Report Generation

