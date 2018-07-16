# urs
A local cli program to shorten urls and open them with an assigned short word. 

# Why Use urs?
urs allows users to set a short word to associate with a url, they can then open the url by typing: `urs <short word>`
in the terminal. This saves the user time as they no longer need to open a browser and then search for a particular 
website or type the url. 

#Getting Started
Follow these instructions on a Linux system to install the program.
###Prerequisites
Python 3 is required, if you do not know if it is installed on your system then type in the terminal: <br>
```
$ python3 --version
``` 
If this does not display the version number installed, download it from <a>https://www.python.org</a>.

###Installing
Clone this repository to the directory that you want with:<br> 
```
$ git clone https://github.com/DCoventry97/urs.git
``` 
Then create a symbolic link from `/usr/local/bin` to `/path/to/directory/containing/this/project`:<br>
```
$ sudo ln -s /path/to/directory/containing/this/project/url-cli/src/main.py /usr/local/bin/urs
```
Replace `/path/to/directory/containing/project` with the real path to the directory where the urs project is stored. 

#How To Use urs
###Adding a new url
To add a new url:
```
$ urs --new <short word> <url>
```
For example:
```
$ urs --new urs_github https://github.com/DCoventry97/urs
```
###Opening a url
A page can then be opened using urs with a url's associated short word: 
```
$ urs <short word>
```
for example:
```
$ urs urs_github
```

###Renaming a short word
To rename a short word so that a url is associated with a different short word:  
```
$ urs --rename <new short word> <old short word>
```
For example:
```
$ urs --rename urs_g urs_github
```

###Deleting a url and its short word
To delete a url and it's associated short word:
```
$ urs --delete <short word>
```
For example:
```
$ urs --delete urs_github 
```

###View all short words and associated url's
To view a list of all short words and associated url's:
```
$ urs --view-all-urls
```

###Help
To get help with this program use this command:
``` 
$ urs help 
```