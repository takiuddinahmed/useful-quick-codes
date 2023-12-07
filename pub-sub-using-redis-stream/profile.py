import redis


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def subscribe_to_stream(stream_name, group_name, consumer_name):
    while True:
        #
        messages_list = redis_client.xreadgroup(group_name, consumer_name, {stream_name: '>'}, count=1, block=0)
        for messages in messages_list:
            stream, messages = messages

            for message_id, message_data in messages:
                print(f"Stream: {stream}, Message ID: {message_id}, Data: {message_data}")

                redis_client.xack(consumer_name, stream, message_id)


# Example usage
if __name__ == "__main__":
    stream_name = "user_created"  
    group_name = "profile"  
    consumer_name = "profile"  

    # redis_client.xgroup_destroy(stream_name, group_name)

    # redis_client.xgroup_create(stream_name, group_name, id='0', mkstream=True)


    subscribe_to_stream(stream_name, group_name, consumer_name)
