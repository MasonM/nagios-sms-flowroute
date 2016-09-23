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
import argparse
import sys
import pprint

# Replace these with your API credentials at
# https://manage.flowroute.com/accounts/preferences/api/
ACCESS_KEY = '1111111'
SECRET_KEY = 'longbase64stringhere'

def parse_cmdline_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help="Print debugging info to STDOUT")
    parser.add_argument('message', help="Message to send")
    parser.add_argument('--from_number', required=True,
                        help="Sender phone number (must be a DID number)")
    parser.add_argument('--to_number', required=True,
                        help="Recipient phone number")
    return parser.parse_args()

def send_message(to_number, from_number, message):
    message = Message(to=to_number, from_=from_number, content=message)
    controller = APIController(username=ACCESS_KEY, password=SECRET_KEY)
    return controller.create_message(message)

args = parse_cmdline_args()
try:
    response = send_message(args.to_number, args.from_number, args.message)
    if args.debug:
        pprint.pprint(response)
except APIException as e:
    if args.debug:
        pprint.pprint(e.response_body['errors'])
    sys.exit("Error - " + str(e.response_code) + '\n')
