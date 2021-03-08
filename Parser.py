import re

#REGEXs
patternIP = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

patternMETHOD = re.compile(r'(GET|POST|OPTION|HEAD|PUT|MOVE|DEL)')

patternAGENT = re.compile(r'(MSIE|Trident|(?!Gecko.+)Firefox|(?!AppleWebKit.+Chrome.+)Safari(?!.+Edge)|(?!AppleWebKit.+)Chrome(?!.+Edge)|(?!AppleWebKit.+Chrome.+Safari.+)Edge|AppleWebKit(?!.+Chrome|.+Safari)|Gecko(?!.+Firefox))(?: |\/)([\d\.apre]+)')

patternURL = re.compile(r'(//[\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')

patternStatusCode = re.compile(r'(\s{1}\d{3}\s{1})')


#VARS
statusCodes = [200,206,301,302,403,404,500,503]

IPs = []

uIPs = ()

Methods = []

Agents = []

userAgent_Temp = []

uAGENTS = ()

URLs = []

AllTheReq = []



#READING THE FILE
with open('C:\\Users\KnightBoom\PycharmProjects\pythonProject\log.txt', 'r') as F:
    for line in F:

        IPs.append(patternIP.search(line)[0])

        Methods.append(patternMETHOD.search(line)[0])

        Agents.append(patternAGENT.search(line))

        URLs.append(patternURL.search(line))

F.close()



#functions
def ips():
    print("All IPs: ")
    try:
        print(IPs)
        print("All IPs have been displayed")
    except:
        print("there is an error and we can't print the ips")

def u_ips():
    uIPs = set(IPs)
    print("Unique IPs: ")
    try:
        print(uIPs)
        print("Unique IPs have been displayed")
    except:
        print("there is an error and we can't print the unique ips")

def urls():
    print("All URLs: ")
    try:
        for item in URLs:
            if item is not None:
                print(item[0])
        print("All URLs have been displayed")
    except:
        print("there is an error and we can't print the URLs")

def user_agents():
    print("Unique User Agents: ")
    try:
        for item in Agents:
            if item is not None:
                userAgent_Temp.append(item[0])
        uAGENTS = set(userAgent_Temp)
        print(uAGENTS)
        print("Unique User Agents have been displayed")
    except:
        print("there is an error and we can't print the user agents")

def reqs_methods():
    print("All Request Methods: ")
    try:
        print(Methods)
        print("All Methods have been displayed")
    except:
        print("there is an error and we can't print the request's methods")

def reqs():
    UserDefinedIP = input("enter the ip ")
    print("IP is being checked")
    print("Displaying all requests of this IP")
    if re.match(patternIP, UserDefinedIP):
        with open('C:\\Users\KnightBoom\PycharmProjects\pythonProject\log.txt', 'r') as F:
            for line in F:
                if UserDefinedIP == (patternIP.search(line)[0]):
                    AllTheReq.append(patternIP.search(line)[0])
                    print(line)
        F.close()
    else:
        print("Invalid IP")



#MAIN
userChoice = input('''Enter 1 ------> to show the ips \nEnter 2 ------> to show the unique ips 
Enter 3 ------> to show the URLs \nEnter 4 ------> to show the user_agents \nEnter 5 ------> to show the requests_methods 
Enter 6 ------> to show the request of your ip\n''')

if userChoice == '1':
    ips()

elif userChoice == '2':
    u_ips()

elif userChoice == '3':
    urls()

elif userChoice == '4':
    user_agents()

elif userChoice == '5':
    reqs_methods()

elif userChoice == '6':
    reqs()
