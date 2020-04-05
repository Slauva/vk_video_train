# VK Video Train
## Simple code to scrape videos from one album to other.

## Description:
```
    The program collects all the id numbers of the video 
    from the album of the group or user and copies them  
    in the newly created album on your page. 
```

## Structure:
```
    config.py - file contain all configuration options
    vk.py     - main body of program
```

## Help:
```
    Zero step, please install module vk_api to correct work:

        $pip3 install vk_api

    Firstly, you must fill all parametrs in file config.py
    They are user name, password, group id(owner_id), 
    and collect all id of albums like "[1,2,3,4]"
    Secondly, you must run vk.py and that's all.

    With large volumes, downloading videos, 
    VK will throw out captcha, the program will issue them to the console, 
    after which you must enter the code in the picture, also many have 
    two-factor account protection, this is also provided in the code.
```
