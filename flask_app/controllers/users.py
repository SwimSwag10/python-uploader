from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
  data = { 'id' : 1 }
  return render_template('index.html', patient=User.get_one_by_id(data), all_patients=User.get_all)