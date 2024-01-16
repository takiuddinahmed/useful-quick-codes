import redis
from typing import List

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def subscribe_to_stream(stream_handlers: List[any], group_name, consumer_name):
    for stream_handler in stream_handlers:
        stream_name = stream_handler["stream_name"]
        handler = stream_handler["handler"]

        try:
            print("Try to create")
            redis_client.xgroup_create(stream_name, group_name, mkstream=True)
        except Exception as e:
            print(e)

    while True:
        for stream_handler in stream_handlers:
            stream_name = stream_handler["stream_name"]
            handler = stream_handler["handler"]
            

            messages_list = redis_client.xreadgroup(group_name, consumer_name, {stream_name: '>'}, count=1, block=100)
            for messages in messages_list:
                stream, messages = messages

                for message_id, message_data in messages:
                    data = {key.decode('utf-8'): value.decode('utf-8') for key, value in message_data.items()}
                    # print(data_str)
                    # print(type(data_str))
                    handler(data)
                    # print(f"Stream: {stream}, Message ID: {message_id}, Data: {message_data}")

                    redis_client.xack(consumer_name, stream, message_id)


def user_created(data):
    print("User created", data)

def user_deleted(data):

    print("User deleted", data['id'])

def user_updated(data):

    print("User updated", data)

def user_test(data):
    print("User test", data)

handler_stream = [
    {
        "stream_name": "user_created",
        "handler": user_created
    },
    {
        "stream_name": "user_deleted",
        "handler": user_deleted
    },
    {
        "stream_name": "user_test",
        "handler": user_test
    }
]


if __name__ == "__main__":
    stream_name = "user_created"  
    group_name = "agreement"  
    consumer_name = "agreement"  

    # try:
    #     redis_client.xgroup_create(stream_name, group_name, id='0', mkstream=True)
    # except Exception as e:
    #     print(e)


    # redis_client.xgroup_destroy(stream_name, group_name)

    # redis_client.xgroup_create(stream_name, group_name, id='0', mkstream=True)

    subscribe_to_stream(handler_stream, group_name, consumer_name)