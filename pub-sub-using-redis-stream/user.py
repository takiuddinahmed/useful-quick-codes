import redis
from uuid import uuid4
import json


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def publish_to_stream(stream_name, message):
    redis_client.xadd(stream_name, message)

# Example usage
if __name__ == "__main__":
    data =  {"id":"95dcd87b-9d0a-409d-ac89-18d32a6e5a55", "firstname": "Takim", "lastname": "Uddin", "email": "taki+108@user.com" }

    data = {"group_id": "6643d833-b331-435b-8f96-bb1c1a6ed079", "user_ids": json.dumps(["fde3a54f-600e-48b0-b38b-477a09029e42"])}
    # publish_to_stream('user_created',data)
    # publish_to_stream('user_deleted',data,)
    # publish_to_stream('user_updated',data)
    # publish_to_stream('user_test',data)
    # publish_to_stream("user_group_users_removed", data)
    publish_to_stream("check", data)
    print("data sent to stream", data)