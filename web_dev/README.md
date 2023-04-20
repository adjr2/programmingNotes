# web_dev

### Virtual Environment

[Follow this](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html#install-virtualenv-win)

### Find the location of python

[Follow this](https://datatofish.com/locate-python-windows/)
Manually Locate Where Python is Installed

1. Type 'Python' in the Windows Search Bar.
2. Right-click on the Python App, and then select “Open file location“
3. Right-click on the Python shortcut, and then select Properties.
4. Click on “Open File Location“.
5. It should look like: C:\path\to\Python\Python39\python.exe

### How to change the virtual environment

1. In VSCode open your command palette — `Ctrl+Shift+P` by default.

2. Look for `Python: Select Interpreter`.

3. In `Select Interpreter` choose `Enter interpreter path...` and then `Find...`.

4. Navigate to your `venv` folder — eg, `~/pyenvs/myenv/` or `\Users\Foo\Bar\PyEnvs\MyEnv\`.

5. In the virtual environment folder choose `<your-venv-name>/Script/python` or `<your-venv-name>/Script/python3`.

### How to remove/rename a virtual environment

1. Activate your virtualenv: `source vnev/bin/activate`.
2. Create a requirements.txt of currently installed packages: `pip freeze > requirements.txt`.
3. Delete the misspelled virtualenv: `rm -r vnev/`.
4. Create a new virtualenv with correct name: `virtualenv venv`.
5. Activate new virtualenv: `source venv/Script/activate`.
6. Install packages from requirements.txt: `pip install -r requirements.txt`.
