pyinstaller -i icon.ico --onefile --clean --noconsole --distpath dev/ -n kde main.py
del kde.spec
rd /s /q "build"