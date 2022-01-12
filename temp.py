import requests
import sys

from pprint import pprint

from requests.structures import CaseInsensitiveDict


def Gogo(uinput):
    dalist = []
    continues = True
    while continues:
        quantity = 0
        KEY = "ISEC-WGQN-DROP-FNZX"
        url = "https://api.weleakinfo.to/api?value="+ uinput +"&type=email&key=" + KEY
        resp = requests.get(url)
        jresp = resp.json()

        if bool(jresp["success"]) == False:
            result = "No results found"
            return result
        else:
            quantity = jresp["found"]
            print("Results\n")
            for i in range(quantity):
                result = jresp["result"][i]["line"]
                dalist.append(result)
                print(result)
            print("There are " + str(quantity) + " passwords")
            return dalist

