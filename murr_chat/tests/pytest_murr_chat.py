import pytest
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.test import Client
from channels.testing.websocket import WebsocketCommunicator
from murr.routing import application


@database_sync_to_async
def create_user(username, email, password):
    user = get_user_model().objects.create_user(
        username, email, password
    )
    return user


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def pytest_chat():

    # create and authorize users
    client_1 = Client()
    client_2 = Client()
    user_1 = await create_user('TestOne', 'TestOne@TestOne.test', 'Murrengan1')
    user_2 = await create_user('TestTwo', 'TestTwo@TestTwo.test', 'Murrengan1')
    client_1.force_login(user=user_1)
    client_2.force_login(user=user_2)
    communicator_1 = WebsocketCommunicator(application, '/ws/chat/', headers=[(
        b'cookie',
        f'sessionid={client_1.cookies["sessionid"].value}'.encode('ascii')
    )])
    connected, _ = await communicator_1.connect()
    assert connected

    await communicator_1.send_json_to({'event': 'group.create', 'data': {'name': 'Murrengan from test'}})
    message = await communicator_1.receive_json_from()
    assert message['status'] == 'ok'
    assert message['event'] == 'group.create'
    assert message['data']['name'] == 'Murrengan from test'
    group_url = message['data']['link']

    await communicator_1.disconnect()
    communicator_1 = WebsocketCommunicator(application, group_url, headers=[(
        b'cookie',
        f'sessionid={client_1.cookies["sessionid"].value}'.encode('ascii')
    )])
    connected1, _ = await communicator_1.connect()
    assert connected1

    communicator_2 = WebsocketCommunicator(application, '/ws/chat/', headers=[(
        b'cookie',
        f'sessionid={client_2.cookies["sessionid"].value}'.encode('ascii')
    )])
    connected2, _ = await communicator_2.connect()
    assert connected2

    await communicator_1.send_json_to({'event': 'add.chat.member', 'data': {'user_id': user_2.id}})
    message = await communicator_1.receive_json_from()
    assert message['status'] == 'ok'
    assert message['event'] == 'add.chat.member'
    assert len(message['data']) == 2

    message = await communicator_2.receive_json_from()
    assert message['status'] == 'ok'
    assert message['event'] == 'new.group'

    await communicator_1.send_json_to({'event': 'send.message', 'data': {'message': 'Hello Murrengan'}})
    message = await communicator_1.receive_json_from()
    assert message['status'] == 'ok'
    assert message['event'] == 'send.message'
    assert message['data']['message'] == 'Hello Murrengan'

    message = await communicator_2.receive_json_from()
    assert message['status'] == 'ok'
    assert message['event'] == 'new.message'

    await communicator_2.disconnect()

    communicator_2 = WebsocketCommunicator(application, group_url, headers=[(
        b'cookie',
        f'sessionid={client_2.cookies["sessionid"].value}'.encode('ascii')
    )])
    connected2, _ = await communicator_2.connect()
    assert connected2

    await communicator_1.send_json_to({'event': 'send.message', 'data': {'message': 'Hello Murrengan 2'}})
    message = await communicator_1.receive_json_from()
    assert message['status'] == 'ok'
    assert message['event'] == 'send.message'
    assert message['data']['message'] == 'Hello Murrengan 2'

    message = await communicator_2.receive_json_from()
    assert message['status'] == 'ok'
    assert message['event'] == 'send.message'
    assert message['data']['message'] == 'Hello Murrengan 2'

    await communicator_1.disconnect()
    await communicator_2.disconnect()