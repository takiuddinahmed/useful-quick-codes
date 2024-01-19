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
                "text": "this is text",
                "file": file_data,
                "obj":"This is an object",
                "agreement_id":"a47b2e31-1a26-44f1-981d-bffb1fad895f"

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
