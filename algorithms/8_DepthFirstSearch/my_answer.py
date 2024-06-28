data = {
        "karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        "tanuj": {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
 }

def find_underlings(name, start): #can use wrapper function to take out start from signature
    underlings=[name]
    for u in data[name]:
        underlings.extend(find_underlings(u, start))
    if start in underlings:
        underlings.remove(start)
    return list(set(underlings))

print(find_underlings('karan', 'karan'))