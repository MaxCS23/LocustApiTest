# 🦗 LocustApiTest

## 📖 Overview
LocustApiTest is a performance testing project for a sample Flask API. It demonstrates **load testing** and **CRUD operations** using Locust. 

Showcasing skills in **API automation and Performance Testing**. 

A sample Flask API is used to ensure no public APIs or websites are affected.

The project simulates multiple user types:

- **BasicUser:** Visits basic pages of the API.
- **HeavyUser:** Performs high-frequency requests to simulate heavy traffic.
- **DataUser:** Performs CRUD operations (Create, Read, Update, Delete) on API items.

---

## 🛠️ Technologies

* Python
* Locust
* Flask
* JSON

---

## 📂 Project Structure
```
LocustApiTest/
├── config/
│   └── settings.py         # Project settings
├── api/
│   ├── app.py              # Main Flask application
│   ├── routes/             # API endpoints
│   └── data/sample_data.json # Example CRUD data
├── locust/
│   ├── tasks/              # Task definitions for each scenario
│   └── users/              # User classes
├── run_api.py              # Script to start the Flask API
├── locustfile.py           # Entry point for Locust
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the API
```bash
python run_api.py
```

### 3. Run Locust
```bash
locust -f locustfile.py
```
Open your browser at http://localhost:8089 to start the test.
Configure the number of users and spawn rate (e.g., 20 users, run for 2 minutes).

---

## ⭐ Features

* Performance testing of multiple endpoints.
* CRUD operations simulation.
* Configurable user types and wait times.
* Easy-to-maintain code using a settings.py file for URLs and endpoints.

---

## 🔧 Next Steps / Improvements

* Add interactive dashboard visualizations using Dash or Streamlit.

---

## 👤 Author
Max Cortes Serrano
QA Engineer
[LinkedIn Profile](https://www.linkedin.com/in/max-cortés-6a132b21b)
Email: maxcortes23@gmail.com
