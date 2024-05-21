cerealList = []

while True:
    cereal = input("Please enter a cereal: ")
    
    if cereal == 'sultana and bran' or cereal == 'weetbix':
        break
    else:
        cerealList.append(cereal)

print("Cereal list:", cerealList)