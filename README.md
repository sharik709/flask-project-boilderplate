# Flask Application with Blueprints

This repository contains a Flask application that is structured using Flask Blueprints and Flask-SQLAlchemy. The application is designed to handle a large Flask application with multiple components and database interactions.

## Introduction

Flask is a lightweight Python web framework that provides useful tools and features for developing web applications. SQLAlchemy is an SQL toolkit that offers efficient database access for relational databases, including an Object Relational Mapper (ORM) for querying and manipulating data using Python objects and methods. Flask-SQLAlchemy is a Flask extension that simplifies the integration of SQLAlchemy with Flask.

As an application grows larger and more complex, it becomes essential to organize the codebase to maintain readability and manageability. Flask provides a feature called blueprints, which allows you to structure your application into modular components. Each component can have its own set of routes, models, and templates, making it easier to manage and maintain the application.

## Repository Structure

The repository follows the recommended structure for a Flask application with blueprints:

```
.
└── flask_app
    ├── app
    │   ├── extensions.py
    │   ├── __init__.py
    │   ├── main
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── models
    │   │   ├── post.py
    │   │   └── question.py
    │   ├── posts
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── questions
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   └── templates
    │       ├── base.html
    │       ├── index.html
    │       ├── posts
    │       │   ├── categories.html
    │       │   └── index.html
    │       └── questions
    │           └── index.html
    ├── app.db
    └── config.py
```

The `flask_app` directory is the root directory of the Flask application. It contains the following files and directories:

- `app`: This directory contains the core code of the application.
  - `extensions.py`: This file is used for managing Flask extensions.
  - `__init__.py`: This file initializes the Flask application and sets up the application factory function.
  - `main`: This directory represents the main blueprint for the application's main routes.
    - `__init__.py`: This file initializes the main blueprint.
    - `routes.py`: This file defines the routes for the main blueprint.
  - `models`: This directory contains the Flask-SQLAlchemy models for the application.
    - `post.py`: This file defines the model for blog posts.
    - `question.py`: This file defines the model for questions and answers.
  - `posts`: This directory represents the blueprint for managing blog posts.
    - `__init__.py`: This file initializes the posts blueprint.
    - `routes.py`: This file defines the routes for the posts blueprint.
  - `questions`: This directory represents the blueprint for managing questions and answers.
    - `__init__.py`: This file initializes the questions blueprint.
    - `routes.py`: This file defines the routes for the questions blueprint.
  - `templates`: This directory contains the HTML templates for the application.
    - `base.html`: This file serves as the base template for other templates to extend.
    - `index.html`: This file is the template for the main index page.
    - `posts`: This directory contains templates related to the posts blueprint.
      - `categories.html`: This file is the template for the categories page of the posts blueprint.
      - `index.html`: This file is the template for the index page of the posts blueprint.
    - `questions`: This directory contains templates related to the questions blueprint.
      - `index.html`: This file is the template for the index page of the questions blueprint.
- `app.db`: This file is the SQLite database file used by the application.
- `config.py`: This file contains the configuration settings for the Flask application.

## Getting Started

To run the Flask application, follow these steps:

1. Set up a Python 3 programming environment.
2. Clone this repository: `git clone https://github.com/sharik709/flask-project-boilderplate.git`
3. Navigate to the `flask_app` directory: `cd flask_app`
4. Activate your virtual environment.
5. Install the required packages: `pip install -r requirements.txt`
6. Set the Flask application environment variable: `export FLASK_APP=app`
7. Set the Flask environment to development mode: `export FLASK_ENV=development`
8. Run the application: `flask run`
9. Access the application in your web browser at `http://127.0.0.1:5000/`

## Conclusion

This repository provides a structured Flask application using Flask Blueprints and Flask-SQLAlchemy. The modular organization allows for better code management and scalability. Feel free to explore the code and customize it for your own needs.

## MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
