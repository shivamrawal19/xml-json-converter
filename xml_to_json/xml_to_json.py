input_xml_path = "file.xml"
output_json_path = "parsedxml.json"

# -------------------------------------------

import xml.etree.ElementTree as ET
import json


tree = ET.parse(input_xml_path)
root = tree.getroot()


def addnode(root, rootindex = 0):
    
    y = json.loads('{}')

    # attributes
    for rootattr in root.attrib.keys():
        y["_"+rootattr] = root.attrib[rootattr]

    # end text
    if root.text.strip() != "":
        y["@val"] = root.text.strip()

    # children
    for rootchildindex, rootchild in enumerate(root):
        y[str(rootchildindex)+"_"+rootchild.tag] = addnode(rootchild, rootchildindex)
        
    return y


y = json.loads('{}')

y["0_"+root.tag] = addnode(root)

print(json.dumps(y, indent=4, sort_keys=True))


with open(output_json_path, 'w') as outfile:
    outfile.write(json.dumps(y, indent=4, sort_keys=True))
