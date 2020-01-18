import zipfile

zip = input("Please enter the location of the ZIP file:")
wloc = input("Please enter the location of the Wordlist:")
success = 1

try:
   z = zipfile.ZipFile(zip)
except:
   print("Failed to load ZIP File!")
   exit(1)

try:
   wlist = open(wloc,"r")
except:
   print("Failed to load Wordlist!")
   exit(1)

wlist = wlist.readlines()

for i in wlist:
   i = i.strip()
   print()
   print("Trying Password "+i.strip())
   try:
      z.extractall(pwd=i.encode())
      print("ZIP File extracted!!")
      success = 0
      break
   except:
      print("Incorrect Password! Trying the next password")

if success != 0:
   print()
   print("Unable to extract the zip file. The Password was not found in the wordlist")
   exit(1)
else:
   exit(0)