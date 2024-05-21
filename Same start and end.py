stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

def same_start_end(s):
    return s[0].lower() == s[-1].lower()

count = sum(same_start_end(s) for s in stringsList)

print(f"The number of strings that have the same character at the start and end is: {count}")