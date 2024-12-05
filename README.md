# Email Breach Detection Tool

# Video Demo : https://youtu.be/EhNs6uAR7Eg

### Description:

This project touches on a real world problem, which has unfortunately been too common in this age of information; data breaches. This tool simply
takes input from user, their email and then outputs details breaches the email has been involved in, if any. And also gives advices to user if
their information has been compromised. Details of breaches includes the number of breaches the email has been involved in, name of the website
where it happened and also the date it happened.


This project was made to bring attention to the alarming rate at which data breaches have been taking place. In times like these online privacy
has become more critical than ever. With everyone's increasing reliance on internet and digital platforms it's important to be wary on where our
data ends up on the web. I made this project to help the people around me understand risks of data breaches, how they can be a prt of it without
knowing and what steps they can take to protect their online presence.

First up, I have a function for validating user's input. I decided to go the simple route and instead of using regex imported the validators
library and used validators.email() function to check if the user input was in the correct email format. If not my program starts a while loop
where my prompt puts emphasis on a 'valid' email and keeps taking input until a valid email is entered.

Next funciton is where I faced most of my challenges. The greatest one being trying to find a free API key. After much surfing I found one which
sufficed for this project, from a service named leakcheck. This function simply sends a GET request to leakcheck using leakcheck's url and it's
provided api key. (requests library was imported for this) Then, if the request was succesful (indicated by the status code) the function
response.json() is used to parse the response JSON and return the breach details. I alos made sure I catch any errors in this process by using
the try and except block.

The last and final function displays the information about breaches in a manner the user would easily understand. First off all, it checks if
there is any information in the info variable and if it has the success key. Then it retrieves the number of breaches. If breaches are found it
prints out the details. And in case some details are missing, like the date or name of the website where the breach happened it defaults to
unknown. After printing the breach information it calls another function which prints out some useful advice on how to keep data safe online next
time. If no breaches are found it prints out a message which says no breaches were found. In case the info variable doesn't contain enough valid
data, maybe due to an invalid response or an API error, the program prints a message which says no data was avalaible or an error has occurred.

Requirments.txt has all the libraries I imported for this project and the test file is a test for my project. In the test, though i imported the
patch library and made use of it's unittest.mock module. So that when I test my code, instead of sending an actual GET request, I can instead fake
some data. So that the focus remains only on the structure of my program, and not on any problems caused by using an external API.

TODO -I might want to add a simple user interface to make it more user friendly and easy to use.