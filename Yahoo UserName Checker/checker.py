# AUTHOR: ZYRO aka Jeevan

import requests, json
import random 
import time
import threading
from requests import api

class Checker_data:
    current = 0
    usernames_loaded = 0
    usernames_checked = 0
    usernames_remaining = 0
    un_fail = 0
    un_avail = 0

usernames = []
available_usernames = []
with open("usernames.txt", "r") as unl:
    for _ in unl.readlines():
        usernames.append(_.strip())
Checker_data.usernames_loaded = usernames.__len__()
Checker_data.usernames_remaining = Checker_data.usernames_loaded
# print(usernames)

uul = open("valid.txt", "w")
def check():
    un = usernames[Checker_data.current]
    Checker_data.current = Checker_data.current+1
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept":"*/*",
        "Accept-Language":f"en-US,en;q=0.{random.randint(2,9)}",
        "Accept-Encoding":"gzip, deflate",
        "Referer":"https://login.yahoo.com/account/create?.intl=in&.lang=en-US&src=ym&specId=yidregsimplified&activity=header-signup&pspid=1197806870&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.lang%3Den-US&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.lang%3Den-US",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With":"XMLHttpRequest",
        "Origin":"https://login.yahoo.com",
        "DNT":"1",
        "Connection":"keep-alive",
        "Cookie":"AS=v=1&s=rZh4vqt1&d=A6469d40c|AOTq2ST.2Tq7ynTVGb4KiNDNBJNgx.dJeH4c2mMsaG.iF4539JIYft2ZTN2nsrwp5hesMAkklDOWxuH5kkIipMuPbW.mhQrZVsRKoBwitDBIr0GR3NWVgJLEO6y1fxyxeXa8_5dqlq_0301tbgO8VbYDr8VEkpQjhMj7dMyqFgmVelxTMm7V6dQ8yIEaFUROEOzplo.HeyXdXOqalVTdzrRjtQesyC7vQDh2v201.xAz4OssUx26k3WyDhpoNrjouy2mRl3bO0wc4G02QnDf8t.BzahqnAaOcGT6FOpU.KDgHC_VS.9Ej291P.UMyAV9uoHldVjiTVrS2V_SO77MRpICdJsubBRAWl__AqQoob_NYCTK4WI1oeKPU2ZAG1uV0G4Gp8W3QM6FJVXAF9KBjzYvk0ysX7hi_f_ButtS8XxBmxipyTyIKPUfK.hfC1lLZuVAuaV92W1X0thw1PRcIxza6uP51dXGUrw4QoUgmVLj9m13oogPsCdaT1WNOaoIzKxYJaMd5ItH_0.VskrqZRzw01PZ4LVCsOs71CRTHZcY8e67HB9hwqCl7BrLYJxJJGTP4NDGV6NhKq27U21ljX24udF5YdLgtgCobko0KMbzSm_PPltGWCMbaO3wksDNIh8QKX1OiEBcCPecsDegjNHc_IjSLJvGOF3eVGIPZVnpAGfVkw3Q69mXlK5LkEZeShFCr9y.2_Z3CiDALwfLC7JhPB8_YNoQDjDZ6aAjNwwPO3Wo9oLoQ3NdpLTMNWgoD5VTRYM73JCVwcUBPfa9NwGMEoJNLeCVNRgJ0evLbC0LZ0.iwgIoVGNDg1wH9UjTD7rf2X3hjhP.kJUj5WcMPEUpqV.Yy7pE7fMlEqQNSXuveFr65u5JbPpE9RhYMZoHMuUyCPyNUVF_ms0X_SQ6w1mgmHgKhCc_hM0CauL3J5BD._bz7z7LEd6Wc4AU8X_Ws4FZFRYJ8dYaoKOBZF0xub1SpmJc5u5jsOSexyJ.~A;",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin"
    }

    dataa = {
        "specId":"yidregsimplified",
        "cacheStored":"",
        "crumb":"nZA1h15g7.h",
        "acrumb":"rZh4vqt1",
        "sessionIndex":"QQ--",
        "done":"https%3A%2F%2Fmail.yahoo.com%2Fd%3F.lang%3Den-IN",
        "googleIdToken":"",
        "authCode":"",
        "attrSetIndex":"0",
        "multiDomain":"",
        "tos0":"oath_freereg%7Cin%7Cen-IN",
        "firstName":"",
        "lastName":"",
        "userid-domain":"yahoo",
        "userId":f"{un}",
        "yidDomainDefault":"yahoo.com",
        "yidDomain":"yahoo.com",
        "password":"",
        "mm":"",
        "dd":"",
        "yyyy":"",
        "signup":""
    }

    # r = requests.post("https://login.yahoo.com/account/module/create?validateField=userId", headers=headers, data=dataa)
    r = api.post("https://login.yahoo.com/account/module/create?validateField=userId", headers=headers, data=dataa)
    print(r.status_code)
    if r.status_code == 200:
        print(r.content)
        resp = r.json()
        print(resp["errors"].__len__())
        Checker_data.usernames_checked = Checker_data.usernames_checked+1
        Checker_data.usernames_remaining = Checker_data.usernames_remaining-1
        for _ in range(int(resp["errors"].__len__())):
            if resp["errors"][_]["name"] == "userId":
                # print("not working")
                Checker_data.un_fail=Checker_data.un_fail+1
            else:
                available_usernames.append(un)
                uul.writeline(f"{un}\n")
                Checker_data.un_avail = Checker_data.un_avail+1

    else:
        print(f"something went wrong with status code {r.status_code}, here is the data: \n", r.text)


for p in range(int(usernames.__len__())):
    threading.Thread(target=check).start()
    time.sleep(0.1)

uul.close()
#with open("valid.txt", "W") as vl:
#    for _ in available_usernames:
#        vl.write(f"{_}\n")
if Checker_data.current != usernames.__len__():
    print("something went wrong with counter")
print("Current counter: ",Checker_data.current)
print("Available usernames: ",Checker_data.un_avail)
print("Unavailable usernames: ", Checker_data.un_fail)

