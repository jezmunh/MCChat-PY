# MCChat-PY
The bot for synchronization minecraft chat with telegram one.
# How to use
First of all you should create your telegram bot via BotFather and get token. After you need to find out about address and port of your own or friend's minecraft server.
Further you just should follow several steps.
1. Add your bot to your telegram chat
2. Run ``pip install -r requirements.txt`` in terminal.
3. Open ``.env`` file and insert previously received Telegram Bot token, address of MC Server and Port respectively.
4. Run ``python bot.py`` for running your bot.
5. Run ``/getID`` command in telegram chat.
6. Copy received id and put it into ``admins`` value in ``boyt.py``.
7. Reboot your bot and use ``/connect`` command in telegram chat.
Enjoy it! Now bot can get sent messages in telegram chat and send that in MC Chat!
If you want to remove bot from server just use ``/quit`` command in telegram chat.
# Features 
* Getting messages from telegram chat and sending it to Minecraft chat
* Commands ``/connect``, ``/quit``, ``/getID`` for connecting bot, quiting it and getting your Telegram user id
# ToDO
Sending messages from MC Chat to Telegram one.
