# 🚗 Car Price Prediction System (Dockerized)

An end-to-end Machine Learning web application that predicts the resale price of a car based on its historical specifications and features. This iteration of the project encapsulates the entire system architecture—including data transformations, the trained Random Forest Regressor model, and the Flask backend environment—inside a highly secure, isolated Docker container for seamless cloud deployment.

---

## 👤 Developer Profile
* **Name:** Akshat Garg
* **Registration Number:** 23BCE10641
* **Course:** B.Tech Computer Science and Engineering

---

## 🔗 Project Links
* **Live Dockerized Web Application:** [Insert Your New Render Live URL Here]
* **GitHub Repository:** [Insert Your New GitHub Repository URL Here]

---

## 🛠️ Tech Stack & Container Ecosystem
* **Core Language:** Python 3.10
* **Containerization Engine:** Docker
* **Machine Learning & Data Processing:** Scikit-learn, Pandas, NumPy
* **Backend Web Framework:** Flask
* **Production Web Server:** Gunicorn (WSGI)
* **Model Serialization:** Pickle
* **Cloud Infrastructure Gateway:** Render (Docker Runtime Container Service)

---

## 📂 Production Directory Architecture
This project strictly follows containerization production guidelines, eliminating the need for environment-specific cloud management artifacts like `Procfile` or `runtime.txt` by managing environment specifications natively inside a single container blueprint:

```text
📁 Car-Price-Docker/
│
├── 📁 static/
│   └── 📄 style.css            # Custom forest green user interface theme
│
├── 📁 templates/
│   └── 📄 index.html           # Core frontend interactive web form
│
├── 📄 app.py                   # Production Flask application backend logic
├── 📄 train.py                 # Automated pipeline dataset download & ML trainer
├── 📄 car_price_model.pkl      # Serialized Random Forest Regressor binary
├── 📄 requirements.txt         # Plaintext manifest mapping third-party libraries
├── 📄 Dockerfile               # Core Docker container environment configuration
└── 📄 .gitignore               # Excludes runtime caches and raw dataset packages

```

---

## 📊 Dataset & Feature Alignment

The machine learning pipeline utilizes the **Vehicle Dataset from CarDekho** (sourced dynamically from Kaggle). Predictions are queried directly from the trained Machine Learning binary array with **zero fallback or placeholder values**. The model evaluates the following target metrics:

| Feature Name | Type | Description / Mapped Space |
| --- | --- | --- |
| **Present Price** | Continuous | Current showroom valuation of the vehicle (in Lakhs) |
| **Kilometers Driven** | Discrete | Total numeric mileage history of the car |
| **Fuel Type** | Categorical | Mapped Target Vectors: `Petrol: 0`, `Diesel: 1`, `CNG: 2` |
| **Seller Type** | Categorical | Mapped Target Vectors: `Dealer: 0`, `Individual: 1` |
| **Transmission** | Categorical | Mapped Target Vectors: `Manual: 0`, `Automatic: 1` |
| **Owners History** | Discrete | Integer count of previous registered owners |
| **Car Age** | Continuous | Transformed temporal matrix calculated from the build year |

---

## ⚙️ How to Setup and Run Locally

### Option A: Standard Local Execution

1. **Initialize Your Environment:**
```bash
conda activate carprice
pip install -r requirements.txt

```


2. **Train the Model Matrix:**
```bash
python train.py

```


3. **Launch the Local Development Server:**
```bash
python app.py

```


Navigate to `http://127.0.0.1:5000` inside your web browser.

### Option B: Local Container Testing (Requires Docker Desktop)

To test the identical configuration used by the cloud environment locally on your machine, compile and run the sandbox container:

```bash
# 1. Build the Docker image from your local blueprint configuration
docker build -t car-price-docker-app .

# 2. Spin up the container sandbox and map your public port
docker run -p 10000:10000 car-price-docker-app

```

Navigate to `http://localhost:10000` inside your web browser.

---

## 🚀 Live Cloud Deployment via Docker

The architecture is containerized and deployed automatically using continuous integration connected directly to **Render**:

* Render parses the root `Dockerfile` to build an isolated, lightweight `python:3.10-slim` Linux sandbox environment.
* Dependencies are safely installed inside the container sandbox according to layer caching rules.
* The production server opens public communication ports inside the sandbox layer via Gunicorn web workers bound directly to Render's gateway environment, bypassing local system dependencies completely.
