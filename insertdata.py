from flask import Flask, redirect, render_template, request
app = Flask(__name__)
 
@app.route('/')
def home():
        return render_template('reg.html')
@app.route('/insert',methods=['POST'])
def insert():
        name=request.form['n']
        email=request.form['e']
        password=request.form['p']
        
        return name
@app.route("/players/")
def players():
        users = ["virat(c)","rohit(vc)","dhawan","raina","manish","dhoni(wk)","hardik","bhuvaneswar","kuldeep","chahal","bumrah"]
        return render_template('user.html', **locals())
        #**locals() would make the names value and name available in the template being rendered.
if __name__ == "__main__":
        app.run(debug=True)
