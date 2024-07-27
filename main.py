import asyncio
import websockets
import json

LOWER_LIMIT = 68090.0
UPPER_LIMIT = 68100.0

async def track_bitcoin_price():
    url = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    
    async with websockets.connect(url) as websocket:
        print("Connected to Binance WebSocket")
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                price = float(data['p']) 

                print(f"Real-time Bitcoin Price: ${price}")
                if price < LOWER_LIMIT:
                    print(f"Alert: Price dropped below lower limit! Current Price: ${price}")
                elif price > UPPER_LIMIT:
                    print(f"Alert: Price exceeded upper limit! Current Price: ${price}")

            except websockets.ConnectionClosed:
                print("Connection closed, retrying...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(track_bitcoin_price())
