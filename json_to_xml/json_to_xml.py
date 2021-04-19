input_json_path = "file.json"
output_xml_path = "parsedjson.xml"

# -------------------------------------------

import xml.etree.cElementTree as ET
from xml.dom import minidom
import json


with open(input_json_path) as f:
    data = json.load(f)

print(json.dumps(data, indent=4, sort_keys=True))



def addnode(root, data):
    for ele in data:
        
        if "_" in ele: # tag or attribute
            
            if ele.index("_") == 0: # attribute
                root.set(ele.split("_")[1], data[ele])
                
            else: # tag
                subele = ET.SubElement(root, ele.split("_")[1])
                addnode(subele, data[ele])
                
        elif "@" in ele: # text
            root.text = data[ele]


data.keys()

for ele in data:
    root = ET.Element(ele.split("_")[1])
    addnode(root, data[ele])
        
# ET.tostring(root)
print(minidom.parseString(ET.tostring(root)).toprettyxml(indent="    "))


xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
with open(output_xml_path, "w") as f:
    f.write(xmlstr)



# For understanding

# root = ET.Element("root")
# doc = ET.SubElement(root, "doc")

# ET.SubElement(doc, "field1", name="blah").text = "some value1"
# ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"



# root = ET.Element("root")

# addnode(root, data)

# for ele in data:
#     print(ele)

#     # create element
#     root = ET.Element(ele.split("_")[1])

#     # add attributes    
#     for elechild in data[ele]:
#         print(elechild)
#         subele = ET.SubElement(root, elechild.split("_")[1])
        
#         for elechildchild in data[ele][elechild]:
#             print(elechildchild)
#             if "_" in elechildchild:
#                 if elechildchild.index("_") == 0:
#                     subele.set(elechildchild.split("_")[1], data[ele][elechild][elechildchild])
#                 else:
#                     subsubele = ET.SubElement(subele, elechildchild.split("_")[1])
                    
#                     for elechildchildchild in data[ele][elechild][elechildchild]:
#                         print(elechildchildchild)
#                         if "_" in elechildchildchild:
#                             if elechildchildchild.index("_") == 0:
#                                 subsubele.set(elechildchildchild.split("_")[1], data[ele][elechild][elechildchild][elechildchildchild])
#                             else:
#                                 ET.SubElement(subsubele, elechildchildchild.split("_")[1])
#                         elif "@" in elechildchild:
#                             subsubele.text = data[ele][elechild][elechildchild][elechildchildchild]
                            
#             elif "@" in elechildchild:
#                 subele.text = data[ele][elechild][elechildchild]

