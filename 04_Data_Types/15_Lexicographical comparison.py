s1 = "apple"
s2 = "banana"

# "apple" appears before "banana" alphabetically, therefore it is True
print(s1 < s2)

# "banana" comes after "apple", therefore it is True
print(s2 > s1)


s1 = "Apple"
s2 = "apple"

# Both strings are same ignoring case, therefore it is True
print(s1.lower() == s2.lower())