# Flask-Json-RestAPI-CV

This is a sample Python Flask application that presents your CV data as a JSON REST API and as a Flask CLI command that prints the data to the console.

Requirements
------------

-   Python 3.x
-   Flask

Installation
------------

Clone the repository to your local machine:

`git clone https://github.com/teodorstelian/Flask-Json-RestAPI-CV`

Install the required packages using pip

Usage
-----

To run the Flask application, use the following command:

`$env:FLASK_APP = "app.py"`

`flask run`

This will start the Flask development server on `http://localhost:5000`.

To run the Flask CLI command, use the following command:

`flask show-cv`

This will print your CV data to the console.

REST API Endpoints
------------------

The REST API has the following endpoints:

-   `GET /personal`: Retrieve your personal data
-   `GET /experience`: Retrieve your experience data
-   `GET /education`: Retrieve your education data

You can access each one of them by going to 
- `http://localhost:5000/personal`, 
- `http://localhost:5000/experience`, 
- `http://localhost:5000/education`
