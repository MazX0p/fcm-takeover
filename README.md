# fcm-takeover

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# What is Firebase Cloud Messaging Service
Firebase Cloud Messaging (FCM) is a cross-platform messaging solution that lets you reliably send messages at no cost.
Using FCM, you can notify a client app that new email or other data is available to sync. You can send notification messages to drive user re-engagement and retention. For use cases such as instant messaging, a message can transfer a payload of up to 4000 bytes to a client app.
attacker could control the content of push notifications to any application that runs the FCM SDK and has it’s *FCM server key exposed* 
and send notifications to every single user of the vulnerable application!

# Finder and checker ScreenShot
![finderpc](https://user-images.githubusercontent.com/54814433/127259850-e7f2eafc-d7da-4d16-b45b-ead1711c45dd.png)


# notifications ScreenShot
![send not pc](https://user-images.githubusercontent.com/54814433/127259869-bf9756bc-1d59-4794-91eb-e1e0efd146c2.png)


# Features of FcmKf.py

 - With this Script you will be able to Find Valid Server Keys of the FCM from APK file
 - Also it will be able to decode the apk file for you !
 - NOTE!: YOU NEED TO INSTALL APKTOOL BEFORE CONTINUING WITH THIS 
 
 # Features of FcmPushNotification.py
 - This Script will Send Notification by using Server Key with IID token from the client app

### USAGE

```sh
$ git clone https://github.com/MazX0p/fcm-takeover.git
$ cd fcm-takeover
$ python3 FcmKf.py
$ pyhton3 FcmPushNotification.py
```


| Name | README |
| ------ | ------ |
| APKtool | [Apktool/documentation][PlDb] |
| FCM | [FCM][PlGh] |
| ME! | [Linkedin][PlGc] |

License
----

MIT


**Free Software, Hell Yeah!**

   [PlDb]: <https://ibotpeaches.github.io/Apktool/documentation/>
   [PlGh]: <https://firebase.google.com/docs/cloud-messaging?hl=en>
   [PlGc]: <https://www.linkedin.com/in/0xmaz/>
