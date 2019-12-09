from urllib.request import Request, urlopen, HTTPError as httperr
import sys

request_header="session=53616c7465645f5f069dde587533d6ddb4e373795a60441f1773cce5ddcc80f801739c7a1626256b114a0e08df3216c3"

def get_data(day):
    print("[GET] waiting for HTTP response...")
    req = Request("https://adventofcode.com/2019/day/" + str(day) + "/input")
    req.add_header("cookie", request_header)
    try:
        content = urlopen(req).read().decode('utf-8')
    except httperr as err:
        print("[HTTP] HTTP Error")
        print("[HTTP] " + str(err.reason))
        return 1

    filename = "inputs/day" + str(day) + ".txt"
    f = open(filename, "w")
    f.write(content)
    f.close()
    print("[GET] success! wrote " + str(len(content)) + " characters to " + filename)

if len(sys.argv) != 2:
    print("Invalid number of arguments.")
    print("Provided arguments should simply be the day #")
else:
    arg1 = sys.argv[1]
    if not (str(arg1).isnumeric()):
        print("Invalid argument")
    else:
        get_data(int(arg1))
