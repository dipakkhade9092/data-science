txt = "dipak"
size = len(text)
palindrone = True 
for i in range(size//2):
    if text[i] != text[size-1-i]:
        palindrone = false
        break

if(palindrone == True):
    print(f"{text} is palindrone")
else:
    print(f"{text} is NOT palindrone")