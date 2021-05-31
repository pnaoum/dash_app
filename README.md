#### Procedure for installation
1. Clone project
2. Go to directory `cd django_dash`
3. Create virtualenv `virtualenv venv`
4. Work on virtualenv `source venv/Scripts/activate` (if you are on Linux, replace `Scripts` by `bin`)
5. Install requirements `pip install -r requirements.txt`
6. Migrate `python manage.py migrate`
7. Run application `python manage.py runserver`
