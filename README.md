<h1 align="center">Welcome to PropertEase 👋 - Mock Django Real Estate Platform with CRUD (MYSQL) </h1>
> Focused on Backend 🙂

> Leave a star 🌟 if you find it useful 🙂

## Technologies Used 💻

- Django 
- MySQL

## Usage 🚀

> Make sure you are using Dart < 3 (future upgrade to dart 3.0)

1. Clone the repository:

   ```bash
   git clone https://github.com/FarzamAliKhan/Hazri.git
   ```

2. Activate Python Virualenv:
   ```bash
    pip install virtualenv
   ```
   ```bash
    python -m venv venv
   ```
   ```bash
    ./venv/scripts/activate
   ```
   ```bash
    pip install virtualenv
   ```

2. Install dependencies:

   ```bash
   pip freeze > requirements.txt
   ```

    ```bash
   pip install -r requirements.txt
   ```
    
4. Connect your preferred database:

   > Kindly check online MySQL/PostGres Django connection (small configuration added in ```bash settings.py```)
   
   > After adding database connection string, migrate database
   ```bash
   python manage.py migrate 
   ```    

5. Run the Website:

   ```bash
   python manage.py runserver
   ```

   > Create Super user to get access to /admin django panel for database operations
   ```bash
   python manage.py createsuperuser 
   ```

###NOTE: 
 > ListingPage is incomplete will push changes later. I have it.
 > Adding properties doesnt work for some reason, to add listings do it from django-admin from /admin.


## Contributions 🤝

Suggestions & Contributions are always welcomed, raise an issue or contact me. @FarzamAliKhan

## License 📒

This project is licensed under the [MIT License](LICENSE).
