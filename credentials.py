import os

# These elements are actually stored as my environment variables( for security purposes).
# Instead of using environment variables, you can directly put the values in this script too.

# my account sid
account_sid = os.environ['twilio_account_sid']

# my auth token
auth_token = os.environ['twilio_auth_token']

# my own cell phone number
my_cell = os.environ['my_cell']

# my twilio cell number
my_twilio = os.environ['my_twilio_number']