import xmlplain
import time
import json

t = time.time()
with open("xml.txt") as inf:
    root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

with open("json1.txt", "w") as outf:
    json.dump(root, outf, ensure_ascii=False, indent=2)
print(time.time() - t)
