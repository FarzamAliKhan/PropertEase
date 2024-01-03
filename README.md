//run these commands to start django project


pip install virtualenv
==
python -m venv venv
==
./venv/scripts/activate 
==
//activate virtual env to run

pip freeze > requirements.txt
==
pip install -r requirements.txt
==
//after this connect your database in settings.py folder
//then run this

python manage.py migrate 
==
//finally

python manage.py runserver
==
//run website

python manage.py createsuperuser 
==
//create ur own admin account to manage functionalites and listings additions etc 


//NOTE: 
ListingPage is incomplete will push changes later. I have it.
Adding properties doesnt work for some reason, to add listings do it from django-admin.
