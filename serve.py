#!/usr/bin/env python3
"""
Worldwave Radio 2077 Local Server
Usage: python3 serve.py

Local server with CORS proxy for real oscilloscope waveform.
Open http://localhost:8080 in your browser.
"""
import http.server
import urllib.request
import urllib.parse
import ssl
import sys
import os

PORT = 8080

class RadioHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/proxy'):
            self.handle_proxy()
        else:
            super().do_GET()

    def handle_proxy(self):
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)
        stream_url = qs.get('url', [''])[0]

        if not stream_url:
            self.send_error(400, 'Missing url parameter')
            return

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            req = urllib.request.Request(stream_url, headers={
                'User-Agent': 'WorldwaveRadio/1.0',
                'Icy-MetaData': '1',
            })

            resp = urllib.request.urlopen(req, timeout=15, context=ctx)

            # 转发响应头 + CORS
            self.send_response(resp.status)
            for key, value in resp.getheaders():
                kl = key.lower()
                if kl in ('content-type', 'content-length', 'icy-name',
                          'icy-description', 'icy-genre', 'icy-url',
                          'icy-br', 'ice-audio-info'):
                    self.send_header(key, value)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()

            # 流式转发
            while True:
                chunk = resp.read(4096)
                if not chunk:
                    break
                try:
                    self.wfile.write(chunk)
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError):
                    break

        except Exception as e:
            self.send_error(502, f'Stream error: {e}')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def log_message(self, format, *args):
        # 只显示有用的日志
        msg = format % args
        if '/proxy' in msg:
            print(f'  📻 {msg}')
        elif '200' in msg or '404' in msg:
            pass  # 静默静态文件
        else:
            print(f'  {msg}')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)) or '.')
    server = http.server.HTTPServer(('', PORT), RadioHandler)
    print(f"""
╔══════════════════════════════════════════════════╗
║   🌊 Worldwave Radio 2077 — Local Server        ║
║                                                  ║
║   Open: http://localhost:{PORT}                   ║
║                                                  ║
║   ✅ Real oscilloscope waveform                  ║
║   ✅ All radio stations work                     ║
║   ✅ CORS proxy enabled                          ║
║                                                  ║
║   Press Ctrl+C to stop                           ║
╚══════════════════════════════════════════════════╝
""")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nBye!')
