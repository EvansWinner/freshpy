#!/usr/bin/env python
"""Get useful information from Fresh Service about tickets."""

import pprint
import sys
from typing import Dict
import requests
import freshpyconf as conf

PASSWORD = "x"  # Required by the API
BASEURL: str = "https://" + conf.ORG_NAME + ".freshservice.com/helpdesk/"
pp = pprint.PrettyPrinter(indent=4)


def construct_url(view_id: str) -> str:
    """Create a URL for getting the views (not a single ticket)."""
    return BASEURL + "tickets/view/" + view_id + "?format=json"


def print_line_maybe(
    dictionary: Dict[str, str], key: str, description: str
) -> str:
    """Return a string from a dict only if it exists."""
    if dictionary[key] is not None:
        return description + "\t" + str(dictionary[key]) + "\n"
    return ""


def get_tickets(url: str) -> str:
    """Print a list of current tickets starting with most recent."""
    response: requests.models.Response = requests.get(
        url, auth=(conf.KEY, PASSWORD)
    )
    if not response:
        bail_out("No response from server")
    json = response.json()
    result: str = (
        "  ID  Status        Requester     Priority    Owner        Subject"
        + "\n"
    )
    for ticket in json:
        result += (
            str(ticket["display_id"]).ljust(6)
            + ticket["status_name"].ljust(9)
            + ticket["requester_name"].ljust(20)[0:20]
            + " "
            + ticket["priority_name"].ljust(7)
            + ticket["responder_name"].ljust(15)[0:15]
            + " "
            + ticket["subject"]
            + "\n"
        )
    return result


def get_ticket(url: str) -> str:
    """Print some information about the ticket supplied at the command line."""
    response: requests.models.Response = requests.get(
        url, auth=(conf.KEY, PASSWORD)
    )
    if not response:
        bail_out("No response from server")
    json = response.json()
    ticket: Dict[str, str] = json["helpdesk_ticket"]
    return (
        print_line_maybe(ticket, "display_id", "ID:\t")
        + print_line_maybe(ticket, "priority_name", "Priority:")
        + print_line_maybe(ticket, "created_at", "Created:")
        + print_line_maybe(ticket, "responder_name", "Owner:\t")
        + print_line_maybe(ticket, "requester_name", "Requester:")
        + print_line_maybe(ticket, "department_name", "Department:")
        + print_line_maybe(ticket, "subject", "Subject:")
        + print_line_maybe(ticket, "description", "Description:\n")
    )


def bail_out(message: str) -> int:
    """Print an error message and exit."""
    print(message)
    sys.exit(1)
    return 1


# Dispatch on command line
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] in conf.VIEWS:
            VIEW = conf.VIEWS[sys.argv[1]]
        else:
            print(get_ticket(BASEURL + "tickets/" + sys.argv[1] + ".json"))
            sys.exit()
    else:
        VIEW = conf.DEFAULT_VIEW
    print(get_tickets(construct_url(VIEW)))
    sys.exit()
