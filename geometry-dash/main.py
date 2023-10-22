import time, requests, random, base64, hashlib, urllib.parse, re
from itertools import cycle
from json import loads
from threading import Thread

# CONFIG
username = ""
password = ""
levelID = ""
accountID = ""
llamaURL = ""
# CONFIG END

emoji = re.compile("["
                           u"\U0001F600-\U0001F64F"  # Emoticons
                           u"\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
                           u"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
                           u"\U0001F700-\U0001F77F"  # Alchemical Symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           u"\U0001FA00-\U0001FA6F"  # Extended-A
                           u"\U0001FA70-\U0001FAFF"  # Extended-B
                           u"\U0001F004-\U0001F0CF"  # Mahjong Tiles
                           u"\U0001F200-\U0001F251"  # Enclosed Ideographic Supplement
                           "]+", flags=re.UNICODE)

def comment_chk(*,username,comment,levelid,percentage,type):
    part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
    return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()

def xor(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))

def gjp_encrypt(data):
    return base64.b64encode(xor(data,"37526").encode()).decode()

def gjp_decrypt(data):
    return xor(base64.b64decode(data.encode()).decode(),"37526")

def comment(name,passw,comment,perc,level):
        try:
                data = {
                    "secret": "Wmfd2893gb7",
                    "accountID": accountID,
                    "gjp": gjp_encrypt(passw),
                    "userName": name,
                    "comment": base64.b64encode(comment.encode()).decode(),
                    "levelID": level,
                    "percent": perc,
                    "chk": comment_chk(username=name,comment=base64.b64encode(comment.encode()).decode(),levelid=str(level),percentage=perc,type="0")
                }
                return requests.post("http://www.boomlings.com/database/uploadGJComment21.php",data=data,headers={"User-Agent": ""}).text
        except:
                return "problem"


def llama(level):
    url = f"http://gdbrowser.com/api/comments/{level}?count=1"
    r = loads(requests.get(url).text)[0]
    u, com = r['username'], r['content']

    if com.lower().startswith("/llama"):
        try:
            print(f"{u}: {com}")
            time.sleep(12)
            llamaUUID = ''.join(random.choice("0123456789") for i in range(12))
            response = requests.get(f"{llamaURL}/{llamaUUID}?q={urllib.parse.quote(com[5:])}").text
            response.replace("\n", " ")
            result = emoji.sub('', response)
            comment(username, password, f"@{u} {result}", "0", level)
        except Exception as e:
            print(str(e))

print("Roboworks is on")
while True:
    try:
        t = Thread(target=llama, args=(levelID,))
        t.start()
        time.sleep(1.5)
    except:
        print("err")
