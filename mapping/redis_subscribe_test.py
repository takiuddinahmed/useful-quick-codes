import asyncio
import redis.asyncio as aioredis
import json

async def main():
    # Create a Red
    # is connection
    redis = aioredis.from_url("redis://localhost:6379")
    
    async with redis.pubsub() as pubsub:
        await pubsub.subscribe("lax")
        async for message in pubsub.listen():
            if message["type"] == "message":
                print(message["data"].decode("utf-8"))

if __name__ == "__main__":
    asyncio.run(main())
