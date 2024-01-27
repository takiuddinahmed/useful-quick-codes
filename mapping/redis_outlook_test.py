import traceback
from redis import asyncio as aioredis
import asyncio
import json
 
redis = aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)
 
async def publish_to_redis():
    # publish to redis
    # data = {
    #     "event": "agreement_submitted_for_approval",
    #     "data": {
    #         'agreement_id': 'a123e456-12d4-a123-a456-426614174001',
    #         'agreement_display_id': 'LAX-10',
    #         'users': [
    #             'c123e456-12d4-a123-a456-426614174000',
    #             'd123e456-12d4-a123-a456-426614174001'
    #         ],
    #         "lax_action": "goto:agreement",
    #         "lax_action_data": {
    #             "id": "e123e456-12d4-a123-a456-426614174001"
    #         }
    #     }
    # }
 
    # data = {
    #     "event": "agreement_created",
    #     "data": {
    #         "agreement_id": "a123e456-12d4-a123-a456-426614174000",
    #         "user_id": "c123e456-12d4-a123-a456-426614174000",
    #     },
    # }
 
    data = {'event': 'new_mail_received', 
            'data': 
                json.dumps({'subject': None, 
                 'body': {'contentType': 'html', 'content': '<html><head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><div style="background-color:#ffe000; border:1px dotted #003333; padding:.8em"><span style="font-size:20pt; font-family:\'Cambria\',\'times new roman\',\'garamond\',serif; color:#ff0000"><b>EXTERNAL</b></span> </div><div><div dir="ltr">Yes, mail received...............</div></div></body></html>'}, 
                 'from': {'emailAddress': {'name': 'shahed jamil', 'address': 'shahedjamil108@gmail.com'}}, 
                 'toRecipients': [{'emailAddress': {'name': 'Shahed Jamil', 'address': 'sjamil@cognitus.com'}}], 
                 'receivedDateTime': '2023-12-18T16:20:29Z', 
                 'sentDateTime': '2023-12-18T16:20:11Z', 
                 "attachments": None,
                 "plugin_connection_id": 2
                 
                 })}
   
    try:
        await redis.xadd(
            "outlook",
            data,
        )
        print("DONE")
    except Exception as e:
        print(traceback.format_exc())
    finally:
        await redis.aclose()
 
 
if __name__ =="__main__":
    asyncio.run(publish_to_redis())