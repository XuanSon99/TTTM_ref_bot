import mexc_spot_v3
import requests
import json
import time
from datetime import datetime, timedelta


rebate = mexc_spot_v3.mexc_rebate()

current_time = int(time.time() * 1000)
current_date = datetime.fromtimestamp(current_time / 1000)

start_time_last_month = int((current_date.replace(day=1, month=2, year=2025, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)).replace(day=1).timestamp() * 1000)
end_time_last_month = int((current_date.replace(day=1, month=2, year=2025, hour=0, minute=0, second=0, microsecond=0) - timedelta(seconds=1)).timestamp() * 1000)

params = {
        "startTime": start_time_last_month,
        "endTime": end_time_last_month,
        "pageSize": 100
    }


list = rebate.get_affiliate_commission(params)
data = list["data"]["resultList"]
page = list["data"]["totalPage"]
if page > 1:
    for i in range(2, page + 1):
        l = rebate.get_affiliate_commission({
        "startTime": start_time_last_month,
        "endTime": end_time_last_month,
        "pageSize": 100,
        "page": i
    })
        data.extend(l["data"]["resultList"])

        if i == page:
            a = requests.put(f"https://hi.muabanusdt.xyz/api/ref/lm",{'data': json.dumps(data)})



