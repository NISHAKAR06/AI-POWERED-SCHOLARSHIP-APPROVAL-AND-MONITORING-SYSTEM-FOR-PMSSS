# AI-Powered Scholarship Approval and Monitoring System for PMSSS

This project is a web-based platform designed to streamline the Prime Minister's Special Scholarship Scheme (PMSSS) application, approval, and monitoring process. It leverages an AI-powered chatbot for user assistance, automates the verification process, and provides a centralized system for students and administrators to manage scholarship applications efficiently.

## Key Features

* **User Authentication:** Secure registration and login system for students, ensuring that only authorized users can access and submit applications.
* **Scholarship Application Portal:** An intuitive, multi-step form for students to submit their personal, academic, and financial details for the PMSSS scholarship.
* **Document Upload System:** A dedicated interface for applicants to upload necessary documents such as Aadhaar card, bonafide certificates, mark sheets, and bank details.
* **Real-Time Status Tracking:** Applicants can track the status of their application through various stages, from submission to final approval and payment disbursement.
* **AI-Powered Chatbot:** An integrated chatbot, powered by the Gemini API, to assist users with their queries, provide information about the scholarship, and guide them through the application process.
* **Admin and User Dashboards:** Separate interfaces for administrators to review applications and for students to monitor their application status and details.

## Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** MongoDB
* **AI/ML:** Google Gemini API for the chatbot functionality

## Getting Started

### Prerequisites

* Python 3.x
* MongoDB
* pip (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nishakar06/ai-powered-scholarship-approval-and-monitoring-system-for-pmsss.git
    cd ai-powered-scholarship-approval-and-monitoring-system-for-pmsss
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file should be created containing Flask, PyMongo, Flask-WTF, etc.)*

3.  **Configure the database:**
    * Make sure your MongoDB server is running.
    * Update the MongoDB connection string in `routes.py` with your database credentials:
        ```python
        client = MongoClient("mongodb+srv://<YOUR_USERNAME>:<YOUR_PASSWORD>@<YOUR_CLUSTER>.mongodb.net/")
        ```

4.  **Set up the Gemini API Key:**
    * Obtain an API key from [Google AI Studio](https://aistudio.google.com/).
    * Add the key to `chat.js`:
        ```javascript
        const Api_Url = "[https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY](https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY)";
        ```

5.  **Run the application:**
    ```bash
    flask run
    ```
    The application will be accessible at `http://127.0.0.1:5000`.

