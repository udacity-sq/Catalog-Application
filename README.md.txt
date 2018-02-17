# Build an Item Catalog Application:
Using the Flash python framework this project implements a Catalog Application. The Catalog
contains a list of items within a variety of categories. The Application also implements a user
registration and authentication system using Google OAuth2. Registered users have the ability to create, edit 
and delete their own items.

# Installation and Setup:

A linux based virtual machine is required. See instructions on install [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)   

Next clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm/tree/master/vagrant)

To Launch the virtual machine use commands ```vagrant up```. It may take a few minutes for the configuration to
finish. Then use command ```vagrant ssh```. 

locate the catalog folder and ```cd``` in to it.

The folder should be empty. Next, donwload the project files from GitHub for this project and
unzip the contents in the catalog folder. 

In your Git terminal type ```ls``` and you should not see the project files listed.

## Creating & Populating the Database:

Run the pyhton file called ```database_setup``` within the virtual machine. This will create the database.

Next, run the python file called ```createDbCatalog```.You should see the success message indicating that
the Catalog and items have been created.

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.cd 
* The log table includes one entry for each time a user has accessed the site.

## Launching the Application:

Run the pyhton file called ```Applcation``` within the virtual machine. 

Open a webbrowser and go to the following [link](http://localhost:8000/)

# Application User Authentication:

If the user hasn't logged in using a google account then he/she is limited to simply browsing the catalog.
In order to login, use the login button located on every page of the application. Once logged in the user 
should be able to create new records. The application only allows the user to edit or delete entries created
by themselves. In case the user tries to edit another users entry a pop-up will notify them that the action is
not possible since they aren't the owner of the entry.

Once, a user is logged in the login button changes to "Logoff". The user can logout using this button.

## JSON Endpoints:

There are two JSON endpoints located at:
* ```/catalog/json``` - [link](http://localhost:8000/catalog/json)
* ```/catalog/items/json``` - [link](http://localhost:8000/catalog/items/json)

If the user visits these links they will be shown the catalog categories and a list of the items.

# Resources:
* SQL Alchemy -[Documentation](https://www.sqlalchemy.org/)
* Full Stack Foundations Course - [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/348776022975462/lessons/3487760229239847/concepts/36310386700923)
* Udacity - Authentication and Authorization Course [here](https://classroom.udacity.com/courses/ud330)
* Udacity Full Stack Developer Forum - [here](https://discussions.udacity.com/c/nd004-full-stack-broadcast)
