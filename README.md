# big-peach
Big Peach is the PyATL meetup management system

# Setup for local development

- Fork this repo.
- Create a branch based of the `develop` branch. Do not branch off `master`.
- Clone your fork repository locally.

OSX / Linux:
- Create a new virtual environment by running `python3 -m venv .venv`
Then run: `source .venv/bin/activate`

Windows:
- Run: `c:\>python -m venv c:\path\to\myenv`
Documentation: https://docs.python.org/3/library/venv.html#creating-virtual-environments

- Install the requirements by running: `pip install -r requirements.txt`
- On your terminal go to the directory where you find the file `manage.py`.
- There is a file named `.env.example`. Rename it to `.env` (remove the `.example` part).
- Run: `python3 manage.py migrate`. This will create your local SQlite database.
- Run: `python3 manage.py runserver` to run the app.
- The app should be live at http://127.0.0.1:8000/


# Before you add a new feature

Please open an issue or explain the issue in our discord server (https://discord.gg/5UBnR3P)
The last thing we want is to waste your time :)

Happy coding!