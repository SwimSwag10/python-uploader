from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
  return render_template('index.html', patient=User.get_one_by_id(), all_patients=User.get_all)

@app.route('/patient/id', methods=['POST'])
def get_patient_id():
  data = {
    "pat_id" : request.form["pat_id"],
  }
  return redirect('/')