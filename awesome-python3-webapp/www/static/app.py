# logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
# 这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），
# 默认的日志格式为日志级别：Logger名称：用户输出消息。
import logging; logging.basicConfig(level=logging.INFO)

# asyncio是支持协程的库 异步IO
import asyncio, os, json, time
from datetime import datetime

# aiohttp是基于asyncio实现的HTTP框架
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
