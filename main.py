from flask import Flask, render_template
app = Flask(__name__) 

  
@app.route('/status') 
def hello(): 
    return "up"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/cover')
def cover():
    return render_template('cover.html')



if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 8080, debug = True)