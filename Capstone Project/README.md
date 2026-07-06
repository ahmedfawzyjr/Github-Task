# Car Dealership Portal — Capstone Project

This repository contains the deliverables and screenshots for the **Car Dealership Portal** Capstone Project, completed as part of the IBM Full Stack Software Developer Professional Certificate. 

The project is a modern web application consisting of a Django-based backend, a React frontend, microservices (running on Node.js/Express and MongoDB for handling reviews), Watson NLP API integration for sentiment analysis of customer reviews, and containerized deployment.

---

## Project Structure & Architecture

```mermaid
graph TD
    Client[React Frontend] -->|HTTP Requests| Django[Django Web Server]
    Django -->|Database Queries| SQLite[(SQLite Database)]
    Django -->|Fetch Reviews| NodeService[Node.js Express / MongoDB Microservice]
    Django -->|Analyze Sentiment| WatsonNLP[Watson NLP Sentiment Analyzer]
```

- **Frontend**: React client with dynamic components, forms, and responsive navigation.
- **Backend**: Django server managing authentication, dealers list, and routing.
- **Microservices**: Node.js/Express service for managing customer reviews database (MongoDB).
- **Watson NLP**: Integration for real-time sentiment analysis (Positive, Negative, Neutral) on submitted reviews.

---

## Submission Checklist & Screenshots

Below are the screenshots documenting the successful completion of all project milestones, matching the grading rubric tasks:

### Phase 1: Django Admin Site & User Authentication

#### Task 1: Django Admin Login
The Django admin portal successfully configured with custom models and objects.
![Django Admin Login](screenshots/admin_login.png)

#### Task 2: Django Admin Logout
Successful logout screen showing Django session management is active.
![Django Admin Logout](screenshots/admin_logout.png)

---

### Phase 2: Dealership Directory & Filtering (Local Environment)

#### Task 3: Dealers Landing Page (Anonymous User)
The main landing page listing all car dealerships in the portal.
![Get Dealers - Anonymous](screenshots/get_dealers.png)

#### Task 4: Dealers Landing Page (Logged In)
Landing page showing user authentication state with the logged-in user's name in the navigation bar.
![Get Dealers - Logged In](screenshots/get_dealers_loggedin.png)

#### Task 5: Filter Dealers by State
Filtering functionality displaying dealerships matching the selected state from the dropdown filter.
![Dealers by State Filter](screenshots/dealersbystate.png)

---

### Phase 3: Reviews & Sentiment Analysis (Local Environment)

#### Task 6: Dealer Details & Reviews
Dealer detail view displaying the dealership information and reviews with their corresponding Watson NLP sentiments (Positive/Neutral/Negative).
![Dealer Details and Reviews](screenshots/dealer_id_reviews.png)

#### Task 7: Review Submission Form
The "Add Review" form interface where authenticated users can submit feedback.
![Add Review Form](screenshots/dealership_review_submission.png)

#### Task 8: Review Successfully Added
The updated review list or confirmation screen showing the newly added review in the dealership portal.
![Added Review Confirmation](screenshots/added_review.png)

---

### Phase 4: Cloud Deployment & Production Verification

#### Task 9: Deployed Landing Page
Verification of the live deployed landing page listing all dealers.
![Deployed Landing Page](screenshots/deployed_landingpage.png)

#### Task 10: Deployed Logged In State
Verification of the live deployed landing page showing a logged-in user session.
![Deployed Logged In User](screenshots/deployed_loggedin.png)

#### Task 11: Deployed Dealer Detail & Reviews
Verification of the live deployed dealer details page showing reviews and Watson NLP sentiments functioning in production.
![Deployed Dealer Detail](screenshots/deployed_dealer_detail.png)

#### Task 12: Deployed Review Submission
Verification of the live deployed review submission flow.
![Deployed Add Review](screenshots/deployed_add_review.png)

---

## How to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ahmedfawzyjr/Github-Task.git
   cd Github-Task/Django
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv env
   .\env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run Migrations & Server**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
