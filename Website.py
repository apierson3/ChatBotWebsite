# This is the website front-end for Azure my chatbot
# Import libraries and dependencies
from flask import Flask

# Create the new app for the running process and various tasks required for the website
app = Flask(__name__)

# Add the decorator for the webpage hierarchy
@app.route('/')

# Define a function with no parameters that returns the text in parenthesis
def home():
    return "Chatbot Website - Andrew Pierson"

# This statement runs the file only if the whole code is executed
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)
