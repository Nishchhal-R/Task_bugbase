# Task_bugbase
Final Task Solution

## Design
### script1.py
<ul>
  <li>script1.py allows users to upload a file from the command line to a specified IP address and port and recieve the output of file command from script2.py.</li>

## Setup
1.Python3 needs to be installed.

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
