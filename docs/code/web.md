# Web

## Check all ip on a network
```bash title=""
arp -a
```

## HTTP Request methods

### GET
**Request** data from a server

Used for retrieving information from a server and should not have any side effects on the server's state. Data is usually sent in the URL as query parameters

```http
GET /get-data?id=123 HTTP/1.1
Host: example.com
```
```bash title=""
curl -X GET "http://example.com/get-data?id=123"
```

### POST
**Send** data to a server

Used when you want to submit information to be processed by a server, such as submitting a form or creating a new resource on the server

```http
POST /submit-data HTTP/1.1
Host: example.com
Content-Type: application/json
{"key": "value"}
```
```bash title=""
curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' "http://example.com/submit-data"
```

### PUT
Update existing data on a server. Data is usually sent in the URL as query parameters

```http title=""
PUT /update-data?id=123 HTTP/1.1
Host: example.com
Content-Type: application/json
{"key": "value"}
```
```bash title=""
curl -X PUT -H "Content-Type: application/json" -d '{"key": "value"}' "http://example.com/update-data?id=123"
```

### DELETE
Delete data from a server. Data is usually sent in the URL as query parameters

```http title=""
DELETE /delete-data?id=123 HTTP/1.1
Host: example.com
```
```bash title=""
curl -X DELETE "http://example.com/delete-data?id=123"
```


## Server

### [flask](https://flask.palletsprojects.com/en/3.0.x/)

- API very easy to understand
- if issues with CORS, use `CORS(app)`

```python
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/update_markdown', methods=['POST'])
def update_markdown_route():
    post_data = request.get_data().decode("utf-8")
    data = urllib.parse.parse_qs(post_data)
    id = data.get("id", [""])[0]
    is_ok = data.get("is_ok", [""])[0] == "true"
    update_markdown(id, is_ok)
    return "OK", 200

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz_route():
    generate_quiz()
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Replace with your desired host and port

```

### [http.server](https://docs.python.org/3/library/http.server.html)

- Built-in python
- Very low level
- Overwrite `do_GET`, `do_POST` etc to define your custom behavior

```python
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/update_markdown":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            data = urllib.parse.parse_qs(post_data)
            id = data.get("id", [""])[0]
            is_ok = data.get("is_ok", [""])[0] == "true"
            update_markdown(id, is_ok)
            self.send_response_ok()
        elif self.path == "/generate_quiz":
            generate_quiz()
            self.send_response_ok()
        else:
            self.send_response_not_found()

    def send_response_ok(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"OK")

    def send_response_not_found(self):
        self.send_response(404)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"Not Found")


if __name__ == "__main__":
    port = 8080
    with socketserver.TCPServer(("", port), CustomRequestHandler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()

```

### [wsgiref](https://docs.python.org/3/library/wsgiref.html)

- Built-in python
- Used by mkdocs `LiveReloadServer`
- Use `start_response(code, headers)` to send headers

```python
start_response("200 OK", [("Access-Control-Allow-Origin", "*")])
```


??? question "Run a server to handle a post request sending a number"
    ```python title="server.py"
    import flask
    app = flask.Flask(__name__)
    @app.route('/number', methods=['POST'])
    def number_route():
        number = flask.request.json.get("number")
        return f"Received {number}", 200
    if __name__ == "__main__":
        app.run()
    ```

??? question "Write a POST request sending a number to localhost on a server running on port 5000"
    ```bash title=""
    curl -X POST -H "Content-Type: application/json" -d '{"number": 42}' http://localhost:5000/number
    ```

??? question "List all 4 http request methods along with their usage"
    - `GET` : request data from server
    - `POST`: send data to server
    - `PUT`: update data to server
    - `DELETE`: delete data from server

??? question "Get ip of all device connected to local network"
    ```bash title=""
    arp -a
    ```
