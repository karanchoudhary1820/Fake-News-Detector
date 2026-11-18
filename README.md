
# 📰 Fake News Detector

<p align="center">
  <b>A Machine Learning Based Fake News Detection System</b>
  <br>
  Detecting Fake and Real News Using Python, Flask, NLP & Machine Learning
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange" />
  <img src="https://img.shields.io/badge/Database-MySQL-blue?logo=mysql" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 📌 Overview

Fake News Detector is a web-based application developed using Python, Flask, and Machine Learning to identify whether a given news article is **Fake News or Real News**.

The application uses Natural Language Processing (NLP) techniques and a trained Machine Learning model to analyze news content and generate predictions.

Users can create an account, log in, submit news articles for verification, view prediction results, and access their previous detection history.

The project aims to demonstrate how Machine Learning can be applied to text classification and help users identify potentially misleading information.

---

## ✨ Features

- **User Registration:** Create a new account.
- **User Login:** Securely access the application through login.
- **Fake News Detection:** Classify news content as Fake or Real.
- **Machine Learning Prediction:** Uses a trained Passive Aggressive Classifier.
- **Text Vectorization:** Converts news text into numerical features using TF-IDF.
- **Prediction History:** Stores previously checked news articles.
- **User-Specific History:** View individual news detection records.
- **Logout:** End the current user session.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Flask | Web Framework |
| Scikit-learn | Machine Learning |
| TF-IDF Vectorizer | Text Feature Extraction |
| Passive Aggressive Classifier | News Classification |
| MySQL | Database Management |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Pickle | Model Serialization |

---

## 🧠 Machine Learning Workflow

The project uses a supervised Machine Learning approach for news classification.

**1. Dataset Collection**

The model is trained using two datasets:

- `Fake.csv` – Fake news articles.
- `True.csv` – Real news articles.

**2. Data Preprocessing**

- Combine news titles and article content.
- Remove missing records.
- Assign labels to fake and real news.

**3. Feature Extraction**

TF-IDF (Term Frequency–Inverse Document Frequency) converts textual data into numerical features.

**4. Model Training**

A Passive Aggressive Classifier is trained using the extracted features.

**5. Prediction**

The trained model classifies submitted news content.

| Label | Prediction |
|---|---|
| 1 | Fake News |
| 0 | Real News |

The trained model and vectorizer are saved using Pickle:

- `fake_news_model.pkl`
- `vectorizer.pkl`

---

## 📂 Project Structure

```text
Fake_News_Detector/
│
├── App.py
├── train_model.py
├── fake_news_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── .gitignore
│
└── templates/
    ├── login.html
    ├── register.html
    ├── index.html
    └── history.html
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/karanchoudhary1820/Fake-News-Detector.git
```

### 2. Navigate to the Project Directory

```bash
cd Fake-News-Detector
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL Database

Make sure MySQL Server is installed and running.

Log in to MySQL:

```bash
mysql -u root -p
```

Create the database:

```sql
CREATE DATABASE fake_news_app;

USE fake_news_app;
```

Create the Users Table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

Create the News History Table:

```sql
CREATE TABLE checks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    news TEXT,
    result VARCHAR(100),
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 7. Configure Database Credentials

Configure your MySQL connection details in `App.py`.

Set your database password through an environment variable rather than hardcoding credentials.

### 8. Run the Application

```bash
python App.py
```

### 9. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 📸 Application Screenshots

Add screenshots of your application here.

| Login Page | Registration Page |
|---|---|
| Add Login Screenshot | Add Registration Screenshot |

| News Detection | Prediction History |
|---|---|
| Add Detection Screenshot | Add History Screenshot |

---

## 🗄️ Database Structure

The application uses MySQL with two tables.

**Users Table**

Stores registered user account details.

**Checks Table**

Stores news detection history, including:

- Username
- News Content
- Prediction Result
- Date and Time

---

## 🚀 Future Enhancements

- Improve prediction accuracy using larger datasets.
- Add additional Machine Learning algorithms.
- Implement secure password hashing.
- Add news source credibility verification.
- Improve text preprocessing.
- Deploy the application to a cloud platform.

---

## ⚠️ Disclaimer

The predictions generated by this application are based on a trained Machine Learning model and its training dataset. Results should not be considered definitive proof of whether a news article is authentic or misleading.

---

## 👩‍💻 Author

**Karan Choudhary**

GitHub: [@karanchoudhary1820](https://github.com/karanchoudhary1820)

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>
