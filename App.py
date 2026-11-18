from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load model
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='elvish',
        database='fake_news_app',
        port=3306
    )

# ---------- Default route ----------
@app.route('/')
def index():
    return redirect(url_for('login'))

# ---------- Register ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
        except mysql.connector.IntegrityError:
            return render_template('register.html', error="Username already exists.")
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

# ---------- Login ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

# ---------- Logout ----------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# ---------- Home + Prediction ----------
@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    prediction = None
    user_input = ""

    if request.method == 'POST':
        news = request.form['news']
        user_input = news
        news_vector = vectorizer.transform([news])
        pred_label = model.predict(news_vector)[0]
        prediction = "❌ Fake News" if pred_label == 1 else "✅ Real News"

        # Save check to DB
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO checks (username, news, result) VALUES (%s, %s, %s)", 
                       (session['user'], news, prediction))
        conn.commit()
        cursor.close()
        conn.close()

    return render_template('index.html', prediction=prediction, user_input=user_input)

# ---------- User History ----------
@app.route('/history')
def history():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM checks WHERE username = %s ORDER BY checked_at DESC", (session['user'],))
    checks = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('history.html', checks=checks)

# ---------- Run ----------
if __name__ == '__main__':
    app.run(debug=True)

