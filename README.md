# Introduction

Freshpy is a simple and tiny python read-only client
for the Fresh Service ticket system licensed under the
GPLv2. It's purpose is to allow you to check your current
queue of tickets or any of the other "views" you have
defined in Fresh Service quickly and easily from the
command line (bash or cmd.exe or whatever you are using).

It also allows you to quickly get some information
about individual tickets.

# Requirements

 - Python 3
 - A command line (cmd.exe or bash or whatever)
 - A Fresh Service account somewhere
 - An API key for your Fresh Service account.

# Data you need

 - **API Key**: To get the API key, go to Fresh Service on the web,
   click on your avatar image or whatever it's
   called in the upper-right, click on Profile
   Settings, then click on the "I'm not a robot"
   captcha, and then cut and paste your api key
   into the place it says to in the freshpyconf.py
   file.

 - **Organization name**: You will also need to know the 
   name use in the Fresh Service URL for your organization.
   If your URL you use to access Fresh Service is
   "https://frobulators.freshservice.com/... " then the name
    you need is "frobulators". That too needs to be
    added to the place it asks for it in freshpyconf.py

 - **View ID numbers**: When you create a view of tickets
   in Fresh Service and name and save that view, when 
    you go to that view, you will see that the URL for it
    ends in a number. Mine are all six digit numbers.
    Any view that you want to see in Freshpy you will
    need to make up a simple name for (no spaces or funny
    characters, please) and then also have that six-digit
    number handy. Open up freshpyconf.py and you will see
    where they go.

# Installation

Download freshpy.py and freshpyconf.py and put them
together somewhere in the same directory. The obvious
way to do this is to clone the repository, but you
don't have to. You just nee those two files and a
working pythong 3 installation.

My way of doing this is something like this in .bashrc or
.zshrc or whatever, if you are so lucky as to work for an
organization that allows you to use Linux or similar:

```
alias tt="python3 ~/path/to/freshpy.py "
```

Or if you're sad and stuck on Windows like me, Google
for the registry hack that allows you to have something
like an rc file for cmd.exe. This is to say, add a Registry DWORD
value called "AutoRun" to 
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor called 
and set it to the path to a .bat file with anything in
it you want, including something like this:

```
doskey tt=python %HOME%\path\to\freshpy.py $* ^| more
```

"tt" is short for "ticket" -- you can use whatever shortcut 
you like, of course.


# Use

Once set up as above, you can do something like 

```
$ tt me
```

assuming that you have defined "me" to corespond to a valid
view number in freshpyconf.py, and it will list out your
tickets (or whatever view "me" is) and give some basic information
about each ticket.


The other thing you can do is, given a ticket number like 123456:

```
$ tt 123456
```

and it will give you a little information about the ticket.

Now that wasn't so bad, was it?

If you want more information it's pretty easy to read the API
docs and add it to freshpy.py. Patches welcome and all that.

# Testing
This has been unextensively tested on Windows 10 using whatever
version of Python Microsoft is pushing at the moment. Three-point-
something. More testing appreciated.

Speaking of testing, I am working on testing with tests.py and
that's lots of fun. Mostly. Patches welcome and all that. Did I
already say that?

Peace out, man.

# TODO

 - Unit tests, because I don't know; why not?
 - Allow conf file to be ~/.freshpy or
   ~/config/freshpy/freshpy.conf or something like that
 - Generalize the output routines so that you can output
   to .csv or whatever else.
 - Read more from the Ticket JSON response and make output
   more customizable
