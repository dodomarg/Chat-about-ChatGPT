# Chat about ChatGPT

## Intro

* T.A.M.I. - https://wiki.telavivmakers.org/index.php/Main_Page
* AI and Natural language models
* Open AI

## The motivation

Forgotten projects that didn't make it and got left behind, perhapses if I could program with just a few words.

## The Rules

* K.I.S.S. - lets use Arduino Framework, lets not use OO or Real time....
* Must get something working
* Use the ChatGPT as much as you can
* Try to use just one paragraph for the requests
 
## Getting started

First I started with Raspberry Pi Pico (RP2040)
that went.... well, technically the code would of worked but there were compatibility issues  with the Arduino libs and the RP2040, specifically - https://github.com/arduino/ArduinoCore-mbed/issues/194#

**Lets go simpler Arduino Uno** 

Right! me and Gal wanted to create a simple heater controller!

### The Hardware
* Arduino Uno
* Relay
* DHT22
* 16x2 I2C LCD
* 2 makeshift buttons

## Let's Ask ChatGPT

##### Just a bang bang controller
_quote of the request_

Well it looks good but there are 2 libs that don't really exist and 2 links that are to nothing 

https://github.com/arduino-libraries/Relay
https://github.com/Seeed-Studio/Grove_AM2311

So I looked for a lib by myself and asked for ChatGPT to use them and rewrite the code, good but didn't finish the code.

Was missing just the delay statement and closing the loop. 

And that's the code [Bang bang temperature controller](bang_bang_temp_controller_with_chatgpt.ino)


**That Worked!**


###### Im hungry! lets try a PID controller

Well now we will start by talking about the libs and only then ask for the compleat code.

Seems to have worked almost perfectly, if it's not brakeing I'm not trying hard enough... lets ask for auto tune of the PID parameters...


no the code is really incomplete, I tried several times to ask for the complete code.. asking for ChatGPT to continue from a certain line seemed to do the trick. 

Compile and run - and works! [PID Temperature controller](PID_temp_controller_chatGPT)

Well actually I don't think the auto-tune is working but perhaps my logic in the way of requesting it is off too.

##### Let's go crazy - ANN temperature controller

Well it didn't come close to working, the ChatGPT was almost unable to finish the setup, but I will say that if not for the rules the information and code snippets it provided would have been very valuable.  

even a wrong answer is helpful when trying to find the right one.

## Sideline 

trying to find the coding limitation, let's ask for adding 1 to a var until it reaches 100 with no loops or ifs
Im looking for 
```
i = 0;
i ++;
i ++;
...

```
 
finally got a i = 170 
interesting. 


### Let's go absolutely crazy

let's ask ChatGPT for an enclosure for our project, but how?
OpenSCAD!

how did it go?