import os
import subprocess
import logging
from flask import Flask, redirect, url_for, request, render_template
from flask.logging import create_logger


#Creating Flash Object
app = Flask(__name__, template_folder='template',static_folder='static')
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      selection = request.form.get('test')
      
      
      #cmd = "robot --timestampoutputs --log '/app/static/mylog.html' --report '/app/static/report.html' "
      cmd = ['robot', '--log', 'static/mylog.html', '--report', 'static/report.html']
      
      file = f'tests/{selection}.robot'
      cmd.append(file)
      LOG.info(f'cmd to execute : {cmd}')
      LOG.info(f'cmd to execute : {os.getcwd()}')

      
      try:
         output = subprocess.check_output(cmd)
         LOG.info(f'Capturing robot testcase {cmd[0]} execution output : {output}')
         return redirect(url_for('static',filename='report.html'))
         #return render_template('index.html',entered_values = "Please look inro C:\\Users\\91994\\sky-auto-repo\\report.html for more details" )
      except Exception as e:
         LOG.info(f'Capturing exception seen while executing robot file {cmd[0]} : {e}')
         return render_template('index.html',entered_values = f"Exception Occurred : {e}" )

   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 8080))