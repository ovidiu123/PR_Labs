import socket

def fetch_via_socket(host, path):
    port = 80
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode())
        response = b""
        while chunk := s.recv(4096):
            response += chunk

    headers, body = response.split(b"\r\n\r\n", 1)
    return body.decode()

if __name__ == "__main__":
    host = "example.com"  # Replace with your host
    path = "/products"
    content = fetch_via_socket(host, path)
    print(content)
