
# Github’s API To Populate DB with Github Users

This is the umba python software engineer task that returns data from a github API and populates the database.


## Screenshots

![alt text](https://github.com/Irotochukwusamuel/umba_python_software_task/blob/master/static/assets/img/sample.png?raw=true)


## Installation

```bash
  - Setup your virtual environment
  - Install required dependecies
  - You can run the project from app.py or run the file
    "flask_run.bash" from terminal
```
    
## Downloaded Dependencies

- Flask

## Implementation And Architecture Decision

This Project uses an MVC Architecture. Model, View, Controller. 
- Model: Handles data logic. 
  #### Model includes :
  - (table_model.py) : This contains a model class which oversees the (creation, reading and cleanup) of data in the database.
  - (validations.py) : This is a validation class which contains methods that accepts parameters, filters it from the database and return the result as a json. 
  - (database.py) : This is solely  creates a database
- View: It displays the information from the model to the user.(index.html)
  #### View includes :
  (index.html) : The index file runs on the client side. it includes a grid data and pagination. once a request is been made, the file api.py then oversees the request and sends back the
  result to the view (index.html) as a json file and in the index.html, it loops through the data received and displays them on a grid format. This index.html does not depend on any javascript file or plugin. 

- Controller: It controls the data flow into a model object and updates the view whenever data changes. 
    #### controller includes :

    (seed.py): This files sends a request to the github api and immediately passes it to the model for table and data creation.
    The methods model.create_table and model.insertData() are been called in this file to keep the project more simple.

 - Root.py :
    This is just a file that holds the name of the database and table respectifully.

```bash
├── app
│   ├── blueprints
│   │   ├── **/api.py
│   ├── modules
│   ├── ├──**/table_models.py
│   ├── ├──**/validations.py
│   ├── static
│   ├── ├──/assets
│   ├── ├──├──/css
│   ├── ├──├──├──**/style.css
│   ├── ├──├──/img
├── ├──├──├──**/*.jpg
│   ├── templates
│   ├── ├──/index.html
│   ├── unit_test
│   ├── ├──**/test_table_models.py
│   ├── ├──**/test_validations.py
│   ├── app.py
│   ├── database.py
│   ├── flask_run.bash
│   ├── root.py
│   ├── seed.py
```
## Running Tests

To run tests, run the following command

```bash
   python -m unittest test_table_models.py 
   python -m unittest test_validations.py 
```


## Features

- Simple interface via a concise set of functions
- Easy to run using app.py or flask_run.bash
- Few dependencies 
- Pure Python, runs on Python 3.6+
- Cross platform, runs on Windows, Linux, macOS
- Code quality is maintained via continuous integration and continous deployment

## Tech Stack

**Programming Languages:** HTML, Css, Python

**Frame Work:** Python FLASK



## Acceptable Users examples

```bash

localhost:5000/ 
localhost:5000/users?pagination=<limit>
localhost:5000/users/<int:page>
localhost:5000/users/<int:page>?pagination=<limit>

```
    
##  API Reference

```bash

localhost:5000/api/users/profiles # 25 pagination by default
localhost:5000/api/users/profiles?page=<page>
localhost:5000/api/users/profiles?pagination=<pagination>
localhost:5000/api/users/profiles?order_by=<id|type>
localhost:5000/api/users/profiles?username=<term>
localhost:5000/api/users/profiles?id=<id>

```
## Demo

www.ocowry.com 


## Support

For support, email irotochukwusamuel@gmail.com

