# FASTAPI_ML
SERVING MACHINE LEARNING MODELS USING FAST  API

FastAPI is a modern, fast (high performance), web framework for building API’s with python 
3.6+ based on Standard python type hints.

Before Going into the Steps in the document Refer how Fast api Works and try out a Simple 
Example. So this Document will Help you out to make it Functional.

Installation:
	Create a virtual environment using : python -m venv env_name
	Activate the Virtual environment : 

	In Virtual Environment Install fastapi using :
		pip install fastapi
		pip install uvicorn (uvicorn is a asynchronous gateway interface - asgi Layer)

Creating Api:

	Create a python file (check with the git Uploads)
	Refer the Fast api Document for the Functionality Coding


Run the api:
    Two Ways : 
    
    1.Running the Python file : python main.py(filename is main here)
    2.Running Using uvicorn : uvicorn main:app --reload (
     filename is main.py and app name instantiated in the file is ‘app’ )
     
Fast api Provides Two Interfaces to check the functionalities which  can be accessible at the  Urls :

       1.localhost/docs 
       2.localhost/redoc

To serve Files Install the Library mentioned as :

	pip install python-multipart 

Install all the necessary pip libraries for the machine model in the environment

Write down logic to communicate the Function Written in Api to The machine Model Python File.
Using Function Calls , Parameterizing. 

Check the libraries installed with the ‘requirements.txt file’ 

Note:

   The Mention Git Upload Is to Serve the data Uploaded as CSV to process in the Machine Learning MOdel and return MOdel output as CSV Downloadable To the User Uploaded.  


HOPING THIS WILL HELP YOU OUT

THANK YOU.!!

--VARMA



