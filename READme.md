I make both API(Retrieve Sales by Drug Classification) and (Retrieve Drug Reviews for a given Drug) you can call my api in postman as
method:- GET
First_api-end-point:- http://127.0.0.1:8000/calculation/Year/Drugtype

               example:- http://127.0.0.1:8000/calculation/2014/R

Second_api_end_point:- http://127.0.0.1:8000/drugCalculation/year/Drug

               example:- http://127.0.0.1:8000/drugCalculation/2016/Melatonin

Note: In Second_api sorting functionality does not apply.


### To Run this Project you have make a directory at any name than

Run the following commands:

pip insatll virtualenv

virtualenv virtual_env_name

source virtual_env_name/bin/activate

pip install requirements.txt

python manage.py runserver

Open Postman and hit the API above

