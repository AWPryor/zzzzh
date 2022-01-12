import requests
from pprint import pprint

from requests.structures import CaseInsensitiveDict

done = True
KEY = "ISEC-WGQN-DROP-FNZX"
while done:
    choise = input("Please select an option: \n1 for Email\n2 for Username\n3 for Hash\n\nYour choise: ")
    if choise == str(1):
        des = "email"
        done = False
    elif choise == str(2):
        des = "username"
        done = False
    elif choise == str(3):
        des = "hash"
        done = False
    else:
        print("No valid choise")
        done = True


value=input("Please enter a " + des + " to search\n")


url = "https://api.weleakinfo.to/api?value="+ value +"&type="+ des+ "&key=" + KEY

resp = requests.get(url)
jresp = resp.json()
quantity = jresp["found"]

print("Results\n")

for i in range(quantity):
    result = jresp["result"][i]["line"]
    print(result)










