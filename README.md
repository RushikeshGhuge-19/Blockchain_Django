
# Blockchain-Based Voting System

## Overview
This project combines Blockchain technology and the Django framework to create a robust and secure voting system. It leverages blockchain's immutability and transparency to ensure the integrity of votes while providing a user-friendly web interface through Django. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is used here to handle backend logic, user authentication, and web application deployment. The system uses SQLite as the database for storing user and candidate information.

## Features
- **User Authentication:** Secure login and user management using Django's built-in authentication system.
- **Candidate Management:** Admins can add, view, and manage candidates.
- **Voting System:** Registered users can cast votes securely, with each vote recorded on the blockchain.
- **Blockchain Implementation:** Custom blockchain for recording votes, ensuring data integrity and transparency.
- **Vote Counter:** Real-time vote tallying and display of results.

## Requirements
- Python 3.12 or higher
- Django 5.1.4
- SQLite (or another database supported by Django)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RushikeshGhuge-19/Blockchain_Django.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Blockchain-Django/blockchain_django
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the superuser credentials.

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure
```
Blockchain-Django/
    blockchain_django/
        voting/        # Contains the Django app for the voting system
        blockchain/    # Blockchain implementation for secure vote storage
        templates/     # HTML templates for the frontend
        static/        # Static files (CSS, JS, images)
        settings.py    # Django project settings
        urls.py        # URL configuration
        views.py       # Application logic
    manage.py          # Django management script
    requirements.txt   # Python dependencies
```

## Usage

### Admin Features:
1. Log in to the admin panel: `http://127.0.0.1:8000/admin/`
2. Add candidates via the admin interface.
3. Monitor vote counts and system performance.

### User Features:
1. Register and log in to the system.
2. View available candidates.
3. Cast a vote securely.
4. View vote counts and results.

## Blockchain Details
- **Blocks:** Each block stores the following:
  - Voter ID (hashed for anonymity)
  - Candidate ID
  - Timestamp
  - Hash of the previous block
- **Hashing Algorithm:** SHA-256
- **Consensus:** Proof-of-Work (PoW) implemented for simplicity.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries, please contact:
- **Rushikesh Ghuge**
- GitHub: [RushikeshGhuge-19](https://github.com/RushikeshGhuge-19)
- Email: [rushighuge8099@gmail.com]

- **Vedant Joshi**
- GitHub: [2VedantJoshi](https://github.com/2VedantJoshi)
- Email: 
