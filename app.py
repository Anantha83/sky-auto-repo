import os
import subprocess
import shlex
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, template_folder='template',static_folder='template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/success/<setup>')
def success(setup):
   return 'You have Entered %s' % setup

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      setup = request.form.get('setup', False)
      cleanup = request.form.get('cleanup', False)
      test = request.form.get('test', False)
      ip = request.form['ip']
      port = request.form['port']
      
      if setup:
          cmd = ['robot', 'test.robot']
      if test:
          cmd = ['robot', 'bgp_md5.robot']
      
      
      try:
         subprocess.check_output(cmd)
         #return redirect(url_for(filename='report.html'))
         return render_template('index.html',entered_values = "Please look inro C:\\Users\\91994\\sky-auto-repo\\report.html for more details" )
      except Exception as e:
         return render_template('index.html',entered_values = f"Exception Occurred : {e}" )

   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 8080))