@echo off

@REM Install dependencies
echo [1/4] Installing dependencies...
pip install -r requirements.txt

@REM Set up the database
echo [2/4] Setting up the database...
python manage.py migrate

@REM Run tests
echo [3/4] Running tests...
python manage.py test

@REM Start the server
echo [4/4] Starting the server...
python manage.py runserver