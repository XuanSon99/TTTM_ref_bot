import mexc_spot_v3
import time
from datetime import datetime, timedelta


rebate = mexc_spot_v3.mexc_rebate()

current_time = int(time.time() * 1000)
current_date = datetime.fromtimestamp(current_time / 1000)



params = {
    "startTime": int((current_date.replace(hour=0, minute=0, second=0, microsecond=0)).timestamp() * 1000),
    "endTime": current_time,
    "uid": "08000298",
    # "inviteCode": "xxx",
    # "page": "xxx",
    # "pageSize": "xxx"
}
AffiliateReferral = rebate.get_affiliate_referral(params)
print(AffiliateReferral)