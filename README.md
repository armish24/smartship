# smartship

## Description
The android app is made for the a shipping hackathon purpose. It consists of a android app to measure weight and size of object using camera of phone. App is made with the help of Apache Cordova. Backend is on Flask.
Also there are features to get your shipping charges calculated and get suggestive packing. Shipping charges are calculated with the help of API provided by Pitney Bowes

## Features

+ get suggestive packing by taking parametes:
    + type of item
    + size of item
    + weight of item
    + location which comes in route of shipping
    + weather conditions of these locations
+ Get rush Calender
+ Get shipping charges calculated anytime, anywhere.
+ #### All the features are done using phone app only. No extra hardware required.

## How to run

+ clone or download the directory
+ Get into the folder `objectDetectionToSuggestPacking`
+ run flask app
  `python3 app.py`
+ do SSH tunneling on serveo
  `ssh -R shellkore:80:localhost:5000 serveo.net`
+ run android app

> Thanks pitney bowes for this oppurtunity.
