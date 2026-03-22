import os
import redis
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 5000

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        count = r.incr("visits")

        message = f"""
        Request Flow:

        Browser → Nginx → App → Redis

        Visits Count: {count}
        """

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

with HTTPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
