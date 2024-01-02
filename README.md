//run these commands to start django project


pip install virtualenv
python -m venv venv

./venv/scripts/activate //activate virtual env to run
pip freeze > requirements.txt
pip install -r requirements.txt

//after this connect your database in settings.py folder
//then run this
python manage.py migrate 

//finally
python manage.py runserver //run website

