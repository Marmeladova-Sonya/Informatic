import xmlplain
import json

with open("xml.txt") as inf:
    root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

with open("json2.txt", "w") as outf:
    json.dump(root, outf, ensure_ascii=False, indent=2)
