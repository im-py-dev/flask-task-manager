# Flask Task Manager
###### A simple Flask application showcasing my skills. This project includes user authentication, notes management, and follows high code structure practices.

### Technologies Used:
Python, Flask, Flask Blueprint, Flask Login, SQLAlchemy, Bcrypt, python-dotenv, email-validator

### .env template
```dotenv
FLASK_DEBUG=1
HOST="0.0.0.0"
PORT=9000

DB_TYPE="sqlite" # or postgresql or mysql
DB_USER="postgres"
DB_PASS=""
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME=""

CELERY_BROKER_URL='redis://localhost:6379/0'
CELERY_RESULT_BACKEND='redis://localhost:6379/0'

MAIL_SERVER='smtp.example.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME='your_email@example.com'
MAIL_PASSWORD='your_email_password'

```

### Future Enhancements (Coming Soon):
- #### Task Management: Plan and manage your tasks with an integrated task management feature.
- #### Admin Panel: An administrative interface for managing users, notes, and other resources.
- #### Celery Integration: Use Celery to schedule reminders and send notifications via email.

###### Feel free to explore the code and stay tuned for upcoming features!
