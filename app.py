from flask import Flask, request, redirect, send_from_directory, render_template_string
import csv
import os

app = Flask(__name__)

# Serve index.html
@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    file_exists = os.path.isfile('contacts.csv')
    with open('contacts.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Message'])  # header
        writer.writerow([name, email, message])

    return redirect('/?success=true')
