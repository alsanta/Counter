from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def main():
    if 'count' not in session:
        session['count'] = 0

    session['count'] += 1
    return render_template('index.html', session = session['count'])

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/plustwo')
def plusTwo():
    session['count'] +=1
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)