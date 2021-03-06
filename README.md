Nagios-SMS-Flowroute
================

Nagios plugin to send SMS alerts using Flowroute (http://www.flowroute.com)

Project location: https://github.com/MasonM/nagios-sms-flowroute

## Requirements

* Python 2.x
* Pip

## Setup

1. Signup for an account at https://manage.flowroute.com/signup/
2. If you do not already have one, get a DID number from https://manage.flowroute.com/accounts/dids/
3. Update the `ACCESS_KEY` and `SECRET_KEY` constants in `nagios_sms_flowroute.py`
4. Run `pip install -r requirements.txt .` to install the script and its dependencies.
5. Define the commands to invoke the script, one for service notifications and one for host
   notifications:

        define command {
           command_name service-notify-by-sms
           command_line /usr/bin/nagios_sms_flowroute.py "$_CONTACTFROM_NUMBER$" "$_CONTACTTO_NUMBER$" "$NOTIFICATIONTYPE$ $SERVICESTATE$ $SERVICEDESC$ Host($HOSTNAME$) Info($SERVICEOUTPUT$) Date($SHORTDATETIME$)"
        }

        define command {
           command_name host-notify-by-sms
           command_line /usr/bin/nagios_sms_flowroute.py "$_CONTACTFROM_NUMBER$" "$_CONTACTTO_NUMBER$" "$NOTIFICATIONTYPE$ $HOSTSTATE$ Host($HOSTALIAS$) Info($HOSTOUTPUT$) Time($SHORTDATETIME$)"
        }

6. Update or add a contact to use the command(s). The `_from_number` and `_to_number` fields are
   required and must be in E.164 format.

        define contact {
           contact_name                    on-call-admin
           alias                           Support Engineer
           service_notification_period     24x7
           host_notification_period        24x7
           service_notification_options    w,u,c,r
           host_notification_options       d,u,r
           service_notification_commands   service-notify-by-sms
           host_notification_commands      host-notify-by-sms
           _from_number                    11234567891
           _to_number                      11234567890
        }
