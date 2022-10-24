#JDU CATEGORY ADDER BY Just gemer
import os
print("JDU CATEGORY ADDER BY Just gemer")
en = str(input("title on eng: "))

# Category Adder 
category = open("categories.json", "w", encoding="utf-8")
category.write('''[{
    "__class": "Category",
    "title": {
        "en": "''' + en + '''",
        "ru": ""
    },
    "filter": {
        "type": "",
        "": 0
    },
    "act": "ui_carousel",
    "isc": "grp_row",
    "items": []    
}]    ''')
category.close()
