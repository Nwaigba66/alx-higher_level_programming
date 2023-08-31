 #!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the byte size of the body of the response.

curl -sI -X GET $1 | awk '/Content-Length/ {print $2}'
