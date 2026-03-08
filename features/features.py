from flask import Flask, request
from flask_login import login_required

app = Flask(__name__)

@app.route('/initial-feature', methods=['GET', 'POST'])
@login_required
def initial_feature():
    if request.method == 'POST':
        # Handle form data
        return 'Initial feature successfully submitted'
    else:
        # Render form
        return 'Please fill out the initial feature form'