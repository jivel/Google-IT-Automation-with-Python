import telnetlib

HOST = "localhost"
PORT = 10000
ENCODING = 'ISO-8859-1'

def open_socket(host, port):
	return telnetlib.Telnet(host, port)

def get_input(file) -> str:
    file_input = open(file, "r", encoding=ENCODING)
    return file_input.read()

def save_response(file, response):
	file_response = open(file,"w+", encoding=ENCODING)
	file_response.write(response)
	file_response.close()

def send():
	with open_socket(HOST, PORT) as tn:
		input = get_input("input.txt") 
		tn.write(b"%s\n" % input.encode(ENCODING))
		save_response("response.txt", tn.read_all().decode(ENCODING))

if __name__== "__main__":
    send()
