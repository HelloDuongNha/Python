import urllib.request


#url = "https://www.gre.ac.uk/"
url = input("Enter an URL for a file: ").strip()
infile = urllib.request.urlopen(url)
content = infile.read().decode() # Read the content as string

print(content)

print()
input("Press return to continue ...")
