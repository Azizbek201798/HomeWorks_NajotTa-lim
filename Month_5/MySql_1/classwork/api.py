# import time

# from pyrogram import Client, filters

# api_id = 20868804
# api_hash = '770cb7b5d13c3cb32d49be1a0bbac216'

# session_name = 'nodir'

# app = Client(session_name, api_id, api_hash)

# send_id = 5326554039
# @app.on_message(filters.me & filters.command("set", ["!", ".", "$", "#"]))
# def save_msg(client, msg):
#     for i in range(20):
#         time.sleep(0.5)
#         client.send_message(chat_id=send_id, text="Kartoshka")

# app.run()