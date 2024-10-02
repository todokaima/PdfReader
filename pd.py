import pypdf
from pypdf import PdfReader

file1 = PdfReader('1.pdf')
file2 = PdfReader('2.pdf')

print(len(file1.pages))
print(len(file2.pages))

print("\nText from file1 (line by line):")
for page in file1.pages:
    text = page.extract_text()
    if text:
        lines1 = text.split('\n')  # Split text by newline character
        for line in lines1:
            print(line)
            words1 = line.split(" ")
            print(words1)

print("\nText from file2 (line by line):")
for page in file2.pages:
    text = page.extract_text()
    if text:
        lines2 = text.split('\n')  # Split text by newline character
        for line in lines2:
            print(line)
            words2 = line.split(" ")
            print(words2)

print("____")
for lin1 in lines1:
    for lin2 in lines2:
        if lin1.split(" ")[0] == lin2.split(" ")[1]:
            print(lin1)