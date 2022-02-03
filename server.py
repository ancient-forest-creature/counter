from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Thems that dies the lucky ones!"

# our index route will handle rendering our form
@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    if 'count' in session:
        session['count'] = session.get('count')  # reading and updating session data
    else:
        session['count'] = 0 # setting session data
    return render_template('index.html')#"Total visits: {}".format(session.get('visits'))

@app.route('/extra')
def add2():
    if 'count' in session:
        session['count'] = session.get('count') + 2  # reading and updating session data
    else:
        session['count'] = 2 # setting session data
    return redirect('/')

@app.route('/any', methods=['POST'])
def addall():
    print(request.form)
    try:
        session['count'] += int(request.form['req']) - 1
        return redirect('/')
    except:
        return redirect('/')


@app.route('/reset')
def show_user():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
