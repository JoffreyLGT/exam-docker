import os
import requests
import datetime
import argparse

parser = argparse.ArgumentParser(
        prog="Permissions tester",
        description="Run different tests on permissions route to confirm it's working as expected.")
parser.add_argument("-a", "--address", required=True, help="API address")
parser.add_argument("-p", "--port", required=True, help="API port")
parser.add_argument("-s", "--statuscode", required=True, help="Expected status code")
parser.add_argument("-l", "--username", required=True, help="User name for login")
parser.add_argument("--password", required=True, help="User password for login")

args = parser.parse_args()

# requête
r = requests.get(
    url=f'http://{args.address}:{args.port}/permissions',
    params= {
        'username': args.username,
        'password': args.password
    }
)

# statut de la requête
status_code = r.status_code

# affichage des résultats
if str(status_code) == args.statuscode:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

output = f'''
{datetime.datetime.now()}
============================
          PERMISSION
============================

request done at "/permissions"
| username="{args.username}"
| password="{args.password}"

expected result = {args.statuscode}
actual result = {status_code}

==>  {test_status}

'''
print(output)

# impression dans un fichier
if os.environ.get('LOG') == "1":
    with open('logs/api_test.log', 'a') as file:
        file.write(output)
