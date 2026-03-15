#!/usr/bin/env python3
"""Serve this repository's static files from any current working directory."""

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 4173
ROOT_DIR = Path(__file__).resolve().parent


class RepoRootHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", PORT), RepoRootHandler)
    print(f"Serving {ROOT_DIR} at http://localhost:{PORT}")
    print(f"Open: http://localhost:{PORT}/index.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
