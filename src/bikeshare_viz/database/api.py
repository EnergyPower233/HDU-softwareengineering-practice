"""零额外依赖的本地 JSON 查询 API，可供前端或答辩演示调用。"""

from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from bikeshare_viz.database.db_helper import get_hourly_stat, get_kpi_summary, get_weather_stat


class BikeApiHandler(BaseHTTPRequestHandler):
    """提供 /api/kpi、/api/weather、/api/hourly 三个 GET 接口。"""

    ROUTES = {
        "/api/kpi": get_kpi_summary,
        "/api/weather": get_weather_stat,
        "/api/hourly": get_hourly_stat,
    }

    def do_GET(self) -> None:  # noqa: N802 - HTTP 标准方法名
        handler = self.ROUTES.get(self.path)
        if handler is None:
            self.send_error(HTTPStatus.NOT_FOUND, "接口不存在")
            return
        payload = json.dumps(handler(), ensure_ascii=False).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def serve(port: int = 8000) -> None:
    """启动本地 API 服务。"""
    server = ThreadingHTTPServer(("127.0.0.1", port), BikeApiHandler)
    print(f"查询 API 已启动：http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    serve()
