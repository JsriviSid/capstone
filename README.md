# CAPSTONE

## Full Stack Nano - Capstone final project

Udacity has given final project of developing a flask app with RBAC and deploying that in a heroku/Render cloud platform. 

I have choosen Casting Agency Specifications as my project and deployed my flask app at Render. 

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer. It has two models Movies & Actors. 

## Application Render URL :
 https://jsricapstone.onrender.com



# **API end points:**

'/movies' - This end point will retrieve the details of movie available from the database and only the users with role casting assistant/casting director/Executive producer can access this end point. 

'/actors' - This end point will retrieve the details of actor available from the actors table and only the users with role casting assistant/casting director/Executive producer can access this end point. 

'/addactor' - This end point will be used to add new actors to the actor table. only the users with role casting director/Executive producer can access this end point. 

'/addmovie' - This end point will be used to add new movie details to the movie table. only the users with role Executive producer can access this end point. 

'/removemovie' - This end point will be used to remove  movie details to the movie table. only the users with role Executive producer can access this end point. 

'/removeactor' - This end point will be used to remove actor details to the actor table. only the users with role Executive producer/casting director can access this end point. 

'/updateactor' - This end point will be used to update actor details to the actor table. only the users with role Executive producer/casting director can access this end point. 

'/updatemovie' - This end point will be used to update movie details to the movie table. only the users with role Executive producer/casting director can access this end point. 
# 
# **Role models utilized**: 

There are three Roles available to utilize this API. 

Casting Assistant : Can view actors and movies
Casting Director :All permissions a Casting Assistant has and add or delete an actor from the database, Modify actors or movies
Executive Producer :All permissions a Casting Director has an add or delete a movie from the database

## About the Stack

app.py - The main flask app contains application endpoint logics stated above. 

auth.py - The code where the main authorization logic to retrieve JWT authorization bearer token from third party authentication system AUTH0 is written. This will retrieve the JWT, decode and check for required RBAC permissions to access the end points. 

models.py - This code contains the database connectivity details & table  structure as models/class. 

settings - This contains the mapping of local variables to environmental variables required to mainly connect to database

.env - Environment file which contains credentials to connect to database

test_app - Unit test python code to test all API end points for success and error behaviours. 

# API Authentication Setup

This API uses Bearer Token Authentication to ensure that only authorized users can access its endpoints configured via AUth0.

Steps to Authenticate:

1: Obtain a Bearer Token: From AUth0 user login. 
2: Making API Requests with Authentication : To access endpoints, bearer token should be given in header of curl/postman request. 
Note: Test_app python has valid bearer token to verify the application.
