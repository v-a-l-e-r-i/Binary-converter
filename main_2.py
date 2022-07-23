import json

with open('file.json') as json_file:
    m_d = json.loads(json_file.read())


text = input("Enter your text: ")
lt = list(text.upper())
my_list = []


for x in lt:
    for key, value in m_d.items():
        if x == key:
            my_list.append(value)
        else:
            print(f"You entered a symbol that is not available")
            break

print(" ".join(my_list))