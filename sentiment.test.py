import os
import requests

import argparse

parser = argparse.ArgumentParser(
        prog="Sentiment tester",
        description="Run different tests on sentiment route to confirm it's working as expected.")
parser.add_argument("-a", "--address", required=True, help="API address")
parser.add_argument("-p", "--port", required=True, help="API port")
parser.add_argument("-r", "--result", choices=["0", "1"], required=True, help="Expected status code")
parser.add_argument("-l", "--username", required=True, help="User name for login")
parser.add_argument("--password", required=True, help="User password for login")
parser.add_argument("-v", "--version", required=True, help="Model version (1 or 2)")
parser.add_argument("--sentence", required=True, help="Sentence to analyze")

args = parser.parse_args()

url=f'http://{args.address}:{args.port}/v{args.version}/sentiment'

# requête
r = requests.get(
    url=url,
    params= {
        'username': args.username,
        'password': args.password,
        'sentence': args.sentence,
    }
)

# statut de la requête
status_code = r.status_code
response_body = r.json()

# affichage des résultats
test_status = "FAILURE"
if str(status_code) == "200":
    if((response_body["score"] > 0 and args.result == "1") 
       or (response_body["score"] < 0 and args.result == "0")):
        test_status = 'SUCCESS'

output = f'''
============================
         SENTIMENTS 
============================

request done at "{url}"
| username="{args.username}"
| password="{args.password}"
| sentence="{args.sentence}"

expected result = {args.result}
actual result = {1 if response_body["score"] > 0 else 0}

==>  {test_status}

'''
print(output)

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)
