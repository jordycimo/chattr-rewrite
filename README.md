# chattr-rewrite
python based http chat app server

rewritten to work with HTTP clients because telnet **SUCKS** and is really annoying to work with.

**when you run this program check that the board file does NOT contain any important information as it will be erased on every restart of the program!**

---how to run---
1. ensure that the conf/404 file exists because it might error if it doesnt!
   a. you can customize this error code as it is just a text file with no extension.
2. run main.py or run.bat/sh
3. input the PORT to host on
4. (optional) [*potential security risk!!*] forward this port on your router to allow external access.
5. it is now (hopefully) ready to use!

---as the user---
1. input a username
2. type your message and hit the *SEND* button to add a message to the board

---resources---
***check these out if you want to commit changes or write your own!***
[label](https://docs.python.org/3/library/http.server.html)
[label](https://docs.python.org/3/library/threading.html)
[label](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)
[label](https://p5js.org/reference/)
