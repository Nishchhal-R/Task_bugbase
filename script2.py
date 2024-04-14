import socket
import os
import subprocess
import json
import logging
import time

PORT = 1234
BUFFER_SIZE = 1024
OUTPUT_DIR = "./received/"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_file_and_command(conn):
    try:
        #Receive the filename
        filename = conn.recv(4096).decode("utf-8")
        print("File to check:  ",filename)
        # Receive a message indicating the start of the file transfer
        start_message = conn.recv(BUFFER_SIZE)

        if start_message == b"START_TRANSFER":
            file_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                if data == b"END_TRANSFER":             #On receiving end message; stop receiving content and save the file
                    break
                file_data += data

            # Save the received file
            file_path = os.path.join(OUTPUT_DIR, filename)
            with open(file_path, "wb") as file:
                file.write(file_data)
            logger.info("File saved: %s", file_path)
            time.sleep(2)

            # Construct and execute the command
            command = ["file", file_path]

            # Send the output back to client formatted as JSON
            output = subprocess.check_output(command).decode("utf-8").strip()   #Execute file command and return output
            output_json = json.dumps({"output": output})
            conn.sendall(output_json.encode())
            logger.info("Output sent successfully.")


    except Exception as e:
        logger.error("An error occurred: %s", e)
    finally:
        conn.close()        #Close the connection with the client

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)  #make the directory if it does not exist

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", PORT))
        s.listen(1)
        logger.info("Waiting for connections...")
        while True:
            conn, addr = s.accept()
            logger.info("Connection established with: %s", addr)
            handle_file_and_command(conn)
