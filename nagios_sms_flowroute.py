#!/usr/bin/env python

"""
nagios_sms_flowroute.py

Plugin for Nagios to send SMS alerts using Flowroute (www.flowroute.com).
Homepage: https://github.com/MasonM/nagios-sms-flowroute

Copyright Mason Malone 2016
"""

from FlowrouteMessagingLib.APIException import APIException
from FlowrouteMessagingLib.Controllers.APIController import APIController
from FlowrouteMessagingLib.Models.Message import Message
import optparse
import sys
import pprint

# Replace these with your API credentials at
# https://manage.flowroute.com/accounts/preferences/api/
ACCESS_KEY = '1111111'
SECRET_KEY = 'longbase64stringhere'

def parse_cmdline_args():
    usage = "usage: %prog [--debug] FROM_NUMBER TO_NUMBER MESSAGE"
    description = "Send SMS message given by MESSAGE to TO_NUMBER, with " +\
        "FROM_NUMBER as the sender. Example:\n" +\
        "%prog 11234567891 11234567890 \"foobar\""
    parser = optparse.OptionParser(usage=usage, description=description)
    parser.add_option('--debug', action='store_true',
                      help="Print debugging info to STDOUT")
    (options, args) = parser.parse_args()
    if len(args) != 3:
        parser.error("incorrect number of arguments")
    return options.debug, args

def send_message(to_number, from_number, message):
    message = Message(to=to_number, from_=from_number, content=message)
    controller = APIController(username=ACCESS_KEY, password=SECRET_KEY)
    return controller.create_message(message)

debug, args = parse_cmdline_args()
try:
    response = send_message(from_number=args[0], to_number=args[1], message=args[2])
    if debug:
        pprint.pprint(response)
except APIException as e:
    if debug:
        pprint.pprint(e.response_body['errors'])
    sys.exit("Error - " + str(e.response_code))
