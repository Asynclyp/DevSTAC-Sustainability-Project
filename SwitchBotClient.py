import json
import time
import hashlib
import hmac
import base64
import uuid
import requests

BASE_URL = 'https://api.switch-bot.com'
DevSTACBulb1 = '6055F9422326'


# Declare empty header dictionary
apiHeader = {}
# open token
token = '398eed07c195a76682bbe0fb8c75484d01a86f5828475ff9ef1aea87ff5b790d9a9a3ebf19a96278b6158ad4a751f271' # copy and paste from the SwitchBot app V6.14 or later
# secret key
secret = 'a3a9f395ec65bafa2933b2430a509bb8' # copy and paste from the SwitchBot app V6.14 or later
nonce = uuid.uuid4()
t = int(round(time.time() * 1000))
string_to_sign = '{}{}{}'.format(token, t, nonce)

string_to_sign = bytes(string_to_sign, 'utf-8')
secret = bytes(secret, 'utf-8')

sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
print ('Authorization: {}'.format(token))
print ('t: {}'.format(t))
print ('sign: {}'.format(str(sign, 'utf-8')))
print ('nonce: {}'.format(nonce))

#Build api header JSON
apiHeader['Authorization']=token
apiHeader['Content-Type']='application/json'
apiHeader['charset']='utf8'
apiHeader['t']=str(t)
apiHeader['sign']=str(sign, 'utf-8')
apiHeader['nonce']=str(nonce)


def getDevices():
    url = BASE_URL+'/v1.1/devices'
    rsp = requests.get(url, headers=apiHeader)

    print(rsp.text)  # uncomment to see raw response
    return rsp.json()

def getDeviceStatus(deviceId):
    url = BASE_URL+f'/v1.1/devices/{deviceId}/status'
    rsp = requests.get(url, headers=apiHeader)

    print(rsp.text)  # uncomment to see raw response
    return rsp.json()

def turnLightBulbOn(deviceId):
    params = {
    "command": "setColor",
    "parameter": "0:80:20", 
    "commandType": "command"
}
    url = BASE_URL+f'/v1.1/devices/{deviceId}/commands'
    rsp = requests.post(url, headers=apiHeader,json=params)

    print(rsp.text)  # uncomment to see raw response
    return rsp.json()

getDeviceStatus(DevSTACBulb1)
turnLightBulbOn(DevSTACBulb1)