from telegram.ext import Application, MessageHandler, filters
import json, os

TOKEN = "8535109588:AAE2vTYC3iJdv04NcMr680XN0PqRZ8YSweg"

FILE = "data.json"

if os.path.exists(FILE):
    with open(FILE,"r",encoding="utf-8") as f:
        data = json.load(f)
else:
    data = {}

async def reply(update, context):
    name = update.message.from_user.first_name
    text = update.message.text

    if "外宿" in text:
        if name not in data:
            data[name] = 0

        data[name] += 1

        with open(FILE,"w",encoding="utf-8") as f:
            json.dump(data,f)

        await update.message.reply_text(
            f"{name} 本月第 {data[name]} 次外宿"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()
