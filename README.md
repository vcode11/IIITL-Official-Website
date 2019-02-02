# IIIT Lucknow Official Website

![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg?style=for-the-badge)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)


This is the repository for official website of **Indian Institute of Information Technology Lucknow**.

## Setup

1. Clone this repo: `git clone https://github.com/dojutsu-user/IIITL-Official-Website.git`.
2. Navigate into the folder 'IIITL-Official-Website': `cd IIITL-Official-Website/`.
3. Install all the dependencies: `pipenv install`.
4. Open virtual environment: `pipenv shell`.
5. Navigate into the folder 'iiitl_website': `cd iiitl_website/`.
6. Run `python manage.py makemigrations`.
7. Run `python manage.py migrate`.
8. Create a superuser: `python manage.py createsuperuser`.
9. Collect static files: `python manage.py collectstatic`.
10. Run server: `python manage.py runserver`.
