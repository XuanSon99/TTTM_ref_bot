import mexc_spot_v3
import requests
import json
import time
from datetime import datetime, timedelta
from telegram import *
from telegram.ext import *

domain = "https://api.taitientrenmang.com"
token = "7990958051:AAFdbbvQHda4fKvN6-Dy7Cc8obh_lDnr14A"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Chào mừng bạn đến với <b>TTTM</b>",
        parse_mode=constants.ParseMode.HTML,
    )

async def messageHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.effective_user.username
    chat_id = update.effective_chat.id

app = (
    ApplicationBuilder().token(token).build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, messageHandler))

async def updateData(context: ContextTypes.DEFAULT_TYPE):
    rebate = mexc_spot_v3.mexc_rebate()

    current_time = int(time.time() * 1000)
    current_date = datetime.fromtimestamp(current_time / 1000)

    params = {
            "startTime": int((current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)).timestamp() * 1000),
            "endTime": current_time,
            "pageSize": 100
        }

    list = rebate.get_affiliate_commission(params)
    data = list["data"]["resultList"]
    page = list["data"]["totalPage"]
    if page > 1:
        for i in range(2, page + 1):
            l = rebate.get_affiliate_commission({
            "startTime": int((current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)).timestamp() * 1000),
            "endTime": current_time,
            "pageSize": 100,
            "page": i
        })
            data.extend(l["data"]["resultList"])

            if i == page:
                requests.put(f"{domain}/api/ref/cm", {'data': json.dumps(data)})


job_queue = app.job_queue

job_minute = job_queue.run_repeating(updateData, interval=60, first=10)

app.run_polling()

