with open("artifact.txt","r") as f:
    text=f.read()

with open("artifact.txt","w") as f:
    text=f.write(text + " im adding one more line.  ")

print(text)
print("its end of stage 3 ")
