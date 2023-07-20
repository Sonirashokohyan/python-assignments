Afghanistan = ["kabul", "herat", "jowzjan", "kandahar", "farah", "ghor", "ghazni", "balkh", "bamyan", "helmand"]
print(Afghanistan[1])
print(Afghanistan[-2])
print(Afghanistan[2:4])
print(Afghanistan[:5])
print(Afghanistan[-4:-1])


head = ["head", "hair", "eyes", "mouth", "tooth", "ear", "face", "nose"]
print(head[5])
print(head[-1])
print(head[3:5])
print(head[3:])
print(head[-7:-1])


friends = ["zhara", "diba", "fershta", "kamela", "fariha", "hamasa", "maryam", "khojesta"]
print(friends[0])
print(friends[-5])
print(friends[1:4])
print(friends[:6])
print(friends[-1:-4])


siblings = ["sajida", "mohammad monir", "elaha", "yusof", "bozorg omid"]
print(siblings[3])
print(siblings[-4])
print(siblings[2:6])
print(siblings[3:])
print(siblings[-2:-3])


colors = ["blue", "white", "black", "green", "yellow", "orange", "red", "pink", "violet"]
if "green" in colors:
    print("yes 'green' is in the colors list")
    
if "navy blue" not in colors:
    print('no "navy blue"is not in colors list')