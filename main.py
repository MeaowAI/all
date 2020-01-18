from manageFile import ManageFile
import json

profile = [
            {
                "name":"อารีฟ",
                "age":"30",
                "city":"narathiwat"
            },
            {
                "name":"แวยายอ",
                "age":"27",
                "city":"narathiwat"
            }
        ]
x = json.dumps(profile)
ManageFile().writeText("C:\\Users\\ROG\\Desktop\\text.txt","w",x)
a=ManageFile().readText("C:\\Users\\ROG\\Desktop\\text.txt","r")
for dat in json.loads(a):
    print(dat["name"])
