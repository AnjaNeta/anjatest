smth = input("enter some words ")
symbols = ['''!()-[]{};:'"\,<>./?@#$%^&*_~''']
lst = (list(filter(lambda x: x not in symbols, smth)))
print(" ".join(lst))
