import sleep
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import  GetMessagesViewsRequest
from telethon import TelegramClient
from telethon import errors

channel = client.get_entity('username')

posts = client(GetHistoryRequest(
    peer=channel,
    limit=10,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))

for message in posts.messages:
    client(GetMessagesViewsRequest(
        peer=channel,
        id=[message.id],
        increment=True
    ))
    sleep(random.uniform(1, 3))
