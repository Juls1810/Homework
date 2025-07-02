from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iphone 16", "+79046841027"),
    Smartphone("Apple", "iphone 15", "+79525983501"),
    Smartphone("Apple", "iphone 14", "+79513042296"),
    Smartphone("Apple", "iphone 13", "+79205006215"),
    Smartphone("Apple", "iphone 12", "+79525983501")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand}, {smartphone.phone_model}, {smartphone.phone_number}")
