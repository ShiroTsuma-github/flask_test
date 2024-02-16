pip install virtualenv
python -m venv venv
call venv/Scripts/activate.bat
set "filename=isvenv.py"
echo ^>^>^> Creating Python file: %filename%
echo import os >> %filename%
echo running_in_virtualenv = "VIRTUAL_ENV" in os.environ >> %filename%
echo print(f'venv working: {running_in_virtualenv}') >> %filename%

echo ^>^>^> Python file created: %filename%
python isvenv.py > temp.txt
set /p venv_working=<temp.txt
del temp.txt
del isvenv.py

echo %venv_working%

if "%venv_working%"=="venv working: True" (
    @REM NOTE: only uncomment the line below if you have a requirements.txt file
    echo venv is working properly. Installing requirements...
    pip install -r requirements.txt
) else (
    echo venv is not working properly. Not installing requirements.
)

pause
