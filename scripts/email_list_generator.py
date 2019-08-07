# a quick common email list generator
# first you need to create a list of common names and save it as names.txt
# then modify the suffixList array so it contains only the suffixes you want
# then just run the script...though you might need to output the results to file...or just copy and paste from the terminal

suffixList = ["hotmail.com", "microsoft.net", "yahoo.com", "hotmail.co.jp", "googlemail.com", "live.co", "aol.net"]
prefixListLocation = ""

# load in the list of common names/prefixes
prefixListLocation = "names.txt"
with open(prefixListLocation) as f:
    mylist = f.read().splitlines()

# loop through each one and create the email
for word in mylist:
    for i in range(len(suffixList)):
        email = word + "@" + suffixList[i]
        print(email)
