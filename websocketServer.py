# -*- coding:utf-8 -*-
import asyncio
import websockets


# 클라로부터 접속시 호출.
async def accept(websocket, path):
    while True:
        # 클라로부터의 메세지 대기탐.
        data = await websocket.recv()
        print("receive:", data)
        # 클라에게 재전송 (echo)
        await websocket.send("echo: " + data)


# main() 자체가 동기함수이므로 이를 돌리는데 await가 들어갈 수 없음.
def main():
    print('websocket server started')


if __name__ == "__main__":
    # main()
    print('websocket server started')
    # 웹소켓 서버 생성. localhost:9998
    start_server = websockets.serve(accept, "localhost", 9998)
    # 비동기로 서버 대기
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    pass

