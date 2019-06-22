import requests
import Identity
import JwtReader
import jwt
import logging
import sys
import subprocess

logging.basicConfig(stream=sys.stdout,level=logging.INFO)
url = "http://5.253.27.28/module/status"

def submit_token():
    file = Identity.Identity()
    init = file.read("Initial")
    if init == "True":
        ID = file.read("Id")
        payload = {'Id': ID}
        encoded_jwt = jwt.encode(payload, 'IamALittleFuckingRPI', algorithm='HS256')
        tokenFile.ChangeSharedPref("Initial","True")
        tokenFile.ChangeSharedPref("Token",encoded_jwt.decode("utf-8"))
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
    cpu = int(int(subprocess.check_output(["cat","/sys/class/thermal/thermal_zone0/temp"]).decode("utf-8"))/1000)
    gpu = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"]).decode("utf-8")[5:7]
    HardwareModel = subprocess.check_output("dmesg | grep model",shell=True).decode("utf-8")[39:]
    OsModel =  subprocess.check_output("cat /etc/os-release | grep VERSION=",shell=True).decode("utf-8")[9:-2]
    SoftwareVersion = tokenFile.read("SoftwareVersion")
    payload = {"cpu":cpu,"gpu":gpu,
               "HardwareModel":HardwareModel,
               "OsModel": OsModel,
               "SoftwareVersion": SoftwareVersion
               }
    print(payload)
    dmesg | less
    headers = {'authorization': mToken}
    requests.post(url, data=payload,headers=headers)
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
