import sys
import socket
import os
import json
import time

def send_file(file_path, host, port):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File not found.")
        return
    filename = os.path.basename(file_path)
    print("File: "+ filename)
    # Open a socket connection to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            #Send the filename
            s.sendall(filename.encode("utf-8"))
            time.sleep(1) # Delay to keep the filename and the start of transfer message seperate
            # Send a message indicating the start of the file transfer
            s.sendall(b"START_TRANSFER")
            # Send the file contents over the socket
            with open(file_path, "rb") as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    s.sendall(data)

            # Send a message indicating the end of the file transfer
            time.sleep(1)       #delay to make sure end of transfer byte is not appended to file content buffer
            s.sendall(b"END_TRANSFER")
            print("File sent successfully.")

            # Receive the output of file command from the server
            output_bytes = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                output_bytes += data

            # Decode the received bytes as JSON
            output_json = json.loads(output_bytes.decode())
            print("File command Output:\n",output_json)


        except ConnectionRefusedError:
            print("Connection refused. Make sure the server is running.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:          # If correct amount of arguments aren't given; exit and tell usage of script
        print("Usage: python3 script1.py <file_path> <host> <port>")
        sys.exit(1)

    file_path = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])

    send_file(file_path, host, port)
