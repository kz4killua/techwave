@echo off

@REM Install dependencies
echo [1/5] Installing dependencies...
pip install -r requirements.txt

@REM Set up the database
echo [2/5] Setting up the database...
python manage.py migrate

@REM Run tests
echo [3/5] Running tests...
python manage.py test

@REM Start the server
echo [4/5] Starting the server...
start cmd /k "python manage.py runserver"
timeout /t 3 >nul

@REM Open the browser to the server URL
echo [5/5] Opening the browser to the server URL...
start http://127.0.0.1:8000