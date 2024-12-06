import json

def to_json(data):
    return json.dumps(data)

def to_xml(data):
    xml = "<products>"
    for product in data:
        xml += "<product>"
        for key, value in product.items():
            xml += f"<{key}>{value}</{key}>"
        xml += "</product>"
    xml += "</products>"
    return xml

def custom_serialize(data):
    return '|'.join([f"{key}={value}" for key, value in data[0].items()])

if __name__ == "__main__":
    data = [{"name": "Product1", "price": 100, "link": "http://example.com", "color": "red"}]
    print("JSON:", to_json(data))
    print("XML:", to_xml(data))
    print("Custom:", custom_serialize(data))
