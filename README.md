# NoPremiumTelegram

Простой скрипт для удаления сообщений с премиум смайликами или анимированными стикерами в Telegram. Очистите ваш чат от лишнего и поддержите удобство общения.

## Установка

1. Убедитесь, что у вас установлен Python 
2. Установите необходимые зависимости

   ```bash
   pip install pyrogram
3. Получите сессию телеграмм аккаунта 
   ```python
    from pyrogram import Client

    api_id = 12345678
    api_hash = "XXX111XXX222XXX"

    app = Client("my_account", api_id=api_id, api_hash=api_hash)

    app.run()

Теперь вы можете использовать NoPremiumTelegram для чистки вашего чата от нежелательных сообщений с премиум смайликами и анимированными стикерами в Telegram.

