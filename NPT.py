from pyrogram import Client, filters

app = Client("my_account")

@app.on_message(filters=filters.private)
async def new_message(event, message):

    # Проверка на анимированный стикер
    if hasattr(message.sticker, "is_video"):
        await app.delete_messages(
            chat_id= message.chat.id,
            message_ids= message.id
        )
        log = f'{message.from_user.first_name} отправил вам стикер ({message.date})'
        print(log)
        with open('history.txt', 'a', encoding='utf-8') as w:
            w.write(f'{log}\n')
            
    # Проверка на тест с премиум эмоджи
    if hasattr(message, "entities"):
        for entity in message.entities:
            if str(entity.type) == "MessageEntityType.CUSTOM_EMOJI":
                await app.delete_messages(
                    chat_id= message.chat.id,
                    message_ids= message.id
                )
                log = f'{message.from_user.first_name} отправил вам CUSTOM_EMOJI ({message.date})'
                print(log)
                with open('history.txt', 'a', encoding='utf-8') as w:
                    w.write(f'{log}\n')

print('Бот работает')
app.run() 