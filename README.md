# Super Simple & Customizable XML to JSON & JSON to XML Converter

- No data loss
- Fully Customizable
- Maintains ordering

## Current settings
| XML          | JSON                     |
|--------------|--------------------------|
| Tags         | "`index`_`tag`": {}      |
| Attributes   | "_`attribute`": "`value`"|
| Inner Text   | "@val": "`inner_text`"   |
```
<?xml version="1.0" encoding="UTF-8"?>
<first-tag>
    <not-interested>
        blah blah
    </not-interested>
    <second-tag name="tagname">
        <the-tag-you-want-as-root>
            <row>
                <columnA link="a/at3.htm">
                    The data that you want
                </columnA>
                <columnB link="h/at3.htm">
                    More data that you want
                </columnB>
            </row>
            <row>
                <columnA link="e/at3.htm">
                    Yet more data that you want
                </columnA>
                <columnB link="s/at3.htm">
                    Eh, get this data too
                </columnB>
            </row>
        </the-tag-you-want-as-root>
    </second-tag>
    <another-irrelevant-tag>
        some other info that you do not want
    </another-irrelevant-tag>
</first-tag>
```
```
{
    "0_first-tag": {
        "0_not-interested": {
            "@val": "blah blah"
        },
        "1_second-tag": {
            "0_the-tag-you-want-as-root": {
                "0_row": {
                    "0_columnA": {
                        "@val": "The data that you want",
                        "_link": "a/at3.htm"
                    },
                    "1_columnB": {
                        "@val": "More data that you want",
                        "_link": "h/at3.htm"
                    }
                },
                "1_row": {
                    "0_columnA": {
                        "@val": "Yet more data that you want",
                        "_link": "e/at3.htm"
                    },
                    "1_columnB": {
                        "@val": "Eh, get this data too",
                        "_link": "s/at3.htm"
                    }
                }
            },
            "_name": "tagname"
        },
        "2_another-irrelevant-tag": {
            "@val": "some other info that you do not want"
        }
    }
}
```

## XML to Json
Have a look at xml_to_json/xml_to_json.ipynb 

## Json to XML
Have a look at json_to_xml/json_to_xml.ipynb 

