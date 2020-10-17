# This is the website front-end for Azure my chatbot
# Import libraries and dependencies
from flask import Flask

# Create the new app for the running process and various tasks required for the website
app = Flask(__name__)

# Add the decorator
@app.route('/')

# Define a function with no parameters that returns the text in parenthesis
def home():
    return "Chatbot Website"

# This statement runs the file only if the whole code is executed
if __name__ =='_main_':
    app.run(host='0.0.0.0', debug=True)
