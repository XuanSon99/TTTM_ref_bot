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

params = [
    {
        "startTime": int((current_date.replace(hour=0, minute=0, second=0, microsecond=0)).timestamp() * 1000),
        "endTime": current_time,
        "pageSize": 100
    },
    {
        "startTime": int((current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)).timestamp() * 1000),
        "endTime": current_time,
        "pageSize": 100
    },
    {
        "startTime": start_time_last_month,
        "endTime": end_time_last_month,
        "pageSize": 100
    }
]

for i, item in enumerate(params):
    data = rebate.get_affiliate_commission(item)
    
    if i == 0:
        code = "td"
    if i == 1:
        code = "cm"
    if i == 2:
        code = "lm"
    
    print(data)
    requests.put(f"https://hi.muabanusdt.xyz/api/ref/{code}",{'data': json.dumps(data["data"]["resultList"])})



