import os
import subprocess
import logging
from flask import Flask, redirect, url_for, request, render_template
from flask.logging import create_logger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


#Creating Flash Object
app = Flask(__name__, template_folder='template',static_folder='static')
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

#Creating DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Defining Database Entries
class TrackTestStatus(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    selected_option = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    def __repr__(self):
        return f'<Option {self.selected_option}>'
     
    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/dbase")
def dbase():
    test_data = TrackTestStatus.query.all()
    return render_template('db.html', test_data = test_data)
    
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      selection = request.form.get('test')
      r1_ip = request.form['r1_ip']
      r2_ip = request.form['r2_ip']
      device_type = request.form['device_type']
      
      #cmd = "robot --timestampoutputs --log '/app/static/mylog.html' --report '/app/static/report.html' "
      cmd = ['robot', '--log', 'static/mylog.html', '--report', 'static/report.html',\
            '--variable', f'ROUTER1:{r1_ip}', '--variable', f'ROUTER2:{r2_ip}',\
            '--variable', f'DEVICE_TYPE:{device_type}']
      
      file = f'tests/{selection}.robot'
      cmd.append(file)
      db.create_all()

     
      try:
         output = subprocess.check_output(cmd)
         LOG.info(f'Capturing robot testcase {cmd[0]} execution output : {output}')
         #Writing the contents to DB
         entry = TrackTestStatus(selected_option = selection, result = output)
         db.session.add(entry)
         db.session.commit()
         return redirect(url_for('static',filename='report.html'))
      except subprocess.CalledProcessError as e:
         LOG.info(f'Capturing exception seen while executing robot file {cmd} : {e.returncode}')
         #Writing the contents to DB during Exception
         entry = TrackTestStatus(selected_option = selection, result = e.returncode)
         db.session.add(entry)
         db.session.commit()
         return render_template('index.html',entered_values = f"Exception Occurred : {e}" )


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 8080))