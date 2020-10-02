# BACK-END Installation



## Local:  
Requirements:
- Python >= 3.6
- pip lastest version  

<br>

Feel free to swap out virtualenv and Pip for Poetry or Pipenv.

<br>
clone this actual repo and follow these steps:
```shell
$ git clone https://github.com/jovicon/the_empire_strikes_back_challenge.git
$ cd backend
$ python -m venv env
$ source env\bin\active // env\Scripts\activate.bat  # mac or linux choice // windows choice
$ python -m pip install --upgrade pip
$ pip install -r dev-requirements.txt
$ pip install -r requirements.txt
$ uvicorn app.main:app --reload
```


