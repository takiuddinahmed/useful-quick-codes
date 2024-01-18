import asyncio
import redis.asyncio as aioredis
import json

import base64

def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        # Read the binary data from the file
        binary_data = file.read()
        
        # Encode the binary data into base64
        base64_data = base64.b64encode(binary_data)
        
        # Convert bytes to string (if needed)
        base64_string = base64_data.decode('utf-8')
        
        return base64_string

async def main():
    # Create a Red
    # is connection
    redis = aioredis.from_url("redis://localhost:6379")

    file_data = file_to_base64("file.txt")
    
    try:
        data = {
            "event": "manual_trigger",
            "data": {
                "string": "7d439a8c-3de5-4b6c-a188-e192333a6480",
                "file": file_data,
            }
        }

        data_json = json.dumps(data)

        # Publish the message
        await redis.publish("lax", data_json)
    finally:
        # Close the Redis connection
        await redis.aclose()

if __name__ == "__main__":
    asyncio.run(main())
