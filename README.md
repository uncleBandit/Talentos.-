Talentos – Next-Gen Job Platform

Talentos is a full-stack Django-based job platform designed to connect talent with opportunities and employers with skilled candidates. The platform features a modern, responsive landing page, secure authentication, custom user models, and role-based organization management.

Table of Contents

Features

Technologies

Installation

Usage

Project Structure

Contributing

License

Features

✅ Responsive landing page with TailwindCSS

✅ Custom user model using email as username

✅ User registration, login, and logout

✅ Role-based organization management (Admin, Employer)

✅ Job posting and application workflow

✅ Membership connections between users and organizations

✅ Clean and maintainable Django project structure

✅ Designed with privacy and security in mind

Technologies

Backend: Python 3.14, Django 6.0

Frontend: TailwindCSS, HTML5, CSS3

Database: SQLite (development)

Version Control: Git & GitHub

Authentication: Django’s built-in auth, custom user model

Installation

Clone the repository

git clone https://github.com/uncleBandit/Talentos.-.git
cd Talentos.-.


Create a virtual environment

python -m venv myworld


Activate the environment

Windows:

myworld\Scripts\activate


Linux/macOS:

source myworld/bin/activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the development server

python manage.py runserver


Open your browser at http://127.0.0.1:8000

Usage

Landing Page: Accessible at /

User Authentication: Login, logout, and signup

Dashboard: /members/dashboard – shows user-specific jobs and memberships

Jobs: /jobs/ – view job listings and details

Admin: /admin/ – manage users, organizations, memberships, and jobs

Project Structure
job_site/
│
├── members/          # Custom user model, forms, views, URLs
├── jobs/             # Job models, views, URLs
├── job_site/         # Project settings, templates, and main configuration
├── db.sqlite3        # Database
└── manage.py


Templates: Located in job_site/templates and app-specific templates folders

Static files: Managed via TailwindCSS for responsive design

Contributing

Contributions are welcome!

Fork the repository

Create a feature branch: git checkout -b feature/my-feature

Commit your changes: git commit -m "Add feature"

Push to the branch: git push origin feature/my-feature

Open a Pull Request

License

This project is MIT Licensed – see the LICENSE file for details.
