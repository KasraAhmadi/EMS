import requests
import Identity
import JwtReader
import jwt
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
url = "http://localhost/module/db_handler"
filePath = "./DB/Elv.db"

def submit_token():
    file = Identity.Identity()
    init = file.read("Initial")
    if init == "True":
        ID = file.read("Id")
        payload = {'Id': ID}
        encoded_jwt = jwt.encode(
            payload, 'IamALittleFuckingRPI', algorithm='HS256')
        tokenFile.ChangeSharedPref("Initial", "True")
        tokenFile.ChangeSharedPref("Token", encoded_jwt.decode("utf-8"))
        return True
    else:
        return False


def read_token():
    init = tokenFile.read("Initial")
    if(init == "True"):
        return tokenFile.read("Token")
    else:
        return None


def main(mToken):
    multiple_files = [
        ('db_file', ('Elv.db', open(filePath, 'rb'), 'file'))]
    headers = {'authorization': mToken}
    payload = {"fileName":"Elv.db"}
    r = requests.post(url,data=payload,files=multiple_files, headers=headers)
    logging.info("compeleted")


try:
    tokenFile = JwtReader.JwtReader()
    myToken = read_token()
    if myToken == None:
        if submit_token() == False:
            raise SystemExit
    main(myToken)
except Exception as e:
    logging.error(e)