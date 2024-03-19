START http://localhost:5000

python src/main.py
if errorlevel 9009 goto TRY1

TRY1:
py src/main.py
if errorlevel 9009 goto TRY2

TRY2:
python3 src/main.py
if errorlevel 9009 goto TRY3

TRY3:
py3 src/main.py
goto SUCCESS

cmd /k

SUCCESS:


endlocal