# TTBOT_NLP_FLU
## Objective

Development of a Twitter bot for sentiment analysis of the Fluminense Football Club (the biggest and most important football club on Earth).

## Functionalities
>The first version of the bot tweets a wordcloud made with the most used words related to the club every 3 hours.

## Files

The files in this repository are:

>lambda_function.py : the main script of the bot with the function that creates the wordcloud and posts it on Twitter;

>entrypoint.py : a script to test the bot;

>requirements.txt : a .txt file with a list of the libraries used;

>createlambdalayer.sh : a bash script to build a layer with docker with the libraries used;

>buildpackage.sh : a bash script to create a .zip file with the function.

The .sh files are ideas from Dylan Castillo (published on his personal blog https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/ thanks for your job!).

## Using AWS

The function is running on AWS following the scheme:
![image](https://user-images.githubusercontent.com/106821774/177230769-f7d62ec7-4d7f-48bf-904b-3fd1852e7a43.png)

A time-trigger was added to run the function every 3 hours everyday.

## Future objectives

Add sentiment analysis of what is said about the club and post it automatically.


