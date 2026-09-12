# -*- coding: UTF-8 -*-
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8080

class OpenManulHTTPRequestHandler(SimpleHTTPRequestHandler):
    """自定义请求处理器，添加 UTF-8 编码响应头与基础 MIME 类型支持"""
    def end_headers(self):
        # 强制针对 HTML、JSON、YAML 等文本资源添加 UTF-8 字符集，防止前端乱码
        if self.path.endswith((".html", ".json", ".yaml", ".yml", ".js", ".css")):
            self.send_header("Content-Type", f"{self.guess_type(self.path)}; charset=utf-8")
        # 允许跨域请求（方便后续前端跨域测试 API 或拉取 openManul 数据）
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


def run_server():
    # 确保运行工作目录为当前脚本所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir+"/../../template")

    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, OpenManulHTTPRequestHandler)

    print(f" site: http://{HOST}:{PORT}")
    print(f" path: {base_dir}")
    print("press Ctrl+C to stop server...\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nserver shutdown...")
        httpd.server_close()
        sys.exit(0)


if __name__ == "__main__":
    run_server()