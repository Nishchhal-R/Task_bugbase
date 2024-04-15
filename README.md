# Task_bugbase
Final Task Solution

## Design
### script1.py
<ul>
  <li>script1.py allows users to upload a file from the command line to a specified IP address and port and recieve the output of file command from script2.py.</li>
  <li>Uses the socket module to establish a TCP connection with the server.</li>
<li>Checks if the specified file exists on the client-side.</li>
<li>Sends the filename to the server.</li>
<li>Sends a start-of-transfer message to indicate the beginning of file transfer.</li>
<li>Reads the file in chunks and sends them over the socket.</li>
<li>Sends an end-of-transfer message to indicate the completion of file transfer.</li>
<li>Receives the output of a command executed on the file from the server.</li>
<li>Prints the received output in JSON format.</li>
</ul>

### script2.py
<ul>
  <li>Uses the socket module to listen for incoming connections from clients.</li>
<li>Receives the filename and file data from the client.</li>
<li>Saves the received file to a "received" folder on the server.</li>
<li>Constructs and executes a specified command on the received file using the subprocess module.</li>
<li>Sends the output of the command back to the client in JSON format.</li>
</ul>

## Setup
<ul>
  <li>Python3 needs to be installed.</li>
</ul>

## Usage
### script2.py
script2.py needs to run first as it will wait for conenction and file from script1.py
```
python script2.py
```

### script1.py
script1.py requires the file path, the address to send to and the port.
```
python script1.py <file_path> <host> <port>
```
