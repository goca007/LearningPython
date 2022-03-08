f = open("Sherlock_Holmes.txt", "r")
for x in f:
    x = x.replace("\n", " ")
    print(x)
    text = text + x

f.close()

text = text.lower()
cleaned_text = ""
for c in text:
    if c in string.ascii_lowercase:
        cleaned_text = cleaned_text + c
    else:
        cleaned_text = cleaned_text + " "


while "  " in cleaned_text:
    cleaned_text = cleaned_text.replace("  ", " ")

print(cleaned_text[0:500])

words = cleaned_text.split(" ")
print(words[0:100])

london_count = 0
for w in words:
    if w == "london":
        london_count = london_count + 1
print(london_count)
    