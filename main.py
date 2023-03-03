from telethon import TelegramClient, sync

api_id = <ваш_API_ID>
api_hash = '<ваш_API_hash>'
phone_number = '<ваш_номер_телефона>'
message = 'Привет, это сообщение отправлено всем моим контактам!'

client = TelegramClient('my_session', api_id, api_hash)
client.start(phone_number)

contacts = client.get_contacts()

for contact in contacts:
 client.send_message(contact, message)

client.disconnect()