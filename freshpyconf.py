"""Configuration file for freshpy."""
from typing import Dict

# Put your Fresh Service API key here
KEY: str = ""

# Put the name of your organization's subdomain here
ORG_NAME: str = ""

# Put the number for the view you want to be the default when you run the
# program without any arguments here
DEFAULT_VIEW: str = "000000"

# Here are your views. Each one is two strings. The first is what you will
# type at the command line as an argument; the second is the view number
# you see at the end of the URL when you look at the view on the web
# version of Fresh Service. See the README.md file for details.
VIEWS: Dict[str, str] = {
    "me": "281671",
    "new": "297585",
    "l2": "291175",
    "l1": "284029",
    "sitevisit": "292323",
    "ingeniconeeded": "297178",
    "johnny": "295959",
    "janine": "295527",
    "isi": "294253",
    "melissa": "293218",
    "systems": "292605",
    "kevin": "291209",
    "pos": "291077",
    "eunice": "289194",
    "ken": "289192",
    "shawn": "289191",
    "travis": "289189",
    "orders": "288356",
    "joe": "288340",
    "mike": "284926",
    "unresolved": "297594",
    "greg": "285908",
}


BASEURL: str = "https://" + ORG_NAME + ".freshservice.com/helpdesk/"
