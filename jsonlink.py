import requests,json
import  numpy as np

a = requests.get("https://jsonplaceholder.typicode.com/posts")
for x in np.arange(3):
    print(json.loads(a.content)[x])
