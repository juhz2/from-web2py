import requests

url = input("url where the code for program is: ")
path = input("Full path (for .py file, local): ")



page = requests.get(url).text

try:
    f = open(path, "w")
except:
    print("invalid path")

try:
    f.write("import requests\n")
    f.write("page = str(requests.get('" + url + "').text)" + "\n")
    f.write("exec(page)" + "\n")
    
except:
    print("error!")

print("file generated; path: " + path)

