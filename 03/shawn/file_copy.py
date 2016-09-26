#encoding: utf-8

path = raw_input("Enter filename here: ")

# windows --> "rb"
f1 = open(path, 'r')
content = f1.read()
f1.close()

file_name = path.split(".")[0] + "_copy" + "." + path.split(".")[1]

# windows --> "wb"
f2 = open(file_name, 'w')
f2.write(content)
f2.close()
