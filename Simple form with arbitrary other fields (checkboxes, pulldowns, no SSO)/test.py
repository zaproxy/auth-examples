from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret'

users = {
    'test': generate_password_hash('test'),
    'zap': generate_password_hash('zap')
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        language = request.form.get('language')
        region = request.form.get('region')

        user = None
        for u in users:
            if u == username:
                user = u

        if user is not None and check_password_hash(users[user], password):
            session['user'] = user
            flash('You were successfully logged in')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            return render_template('login.html', languages=['English', 'Germany', 'Dutch'], regions=['North', 'South', 'East', 'West'], remember=remember, language=language, region=region)

    return render_template('login.html', languages=['English', 'Germany', 'Dutch'], regions=['North', 'South', 'East', 'West'])

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user = session['user']
        return render_template('dashboard.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
