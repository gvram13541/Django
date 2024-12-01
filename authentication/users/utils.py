import requests
import json
from django.conf import settings

def send_otp(mobile_number, otp):
    # For testing purposes - remove this in production
    print(f"OTP for {mobile_number}: {otp}")
    # return True
    
    # Uncomment below code when you have MSG91 credentials
    try:
        url = "https://control.msg91.com/api/v5/flow/"
        
        payload = json.dumps({
            "template_id": settings.MSG91_TEMPLATE_ID,
            "sender": settings.MSG91_SENDER_ID,
            "short_url": "0",
            "mobiles": mobile_number,
            "VAR1": otp
        })
        
        headers = {
            'authkey': settings.MSG91_AUTH_KEY,
            'content-type': "application/json"
        }
        
        response = requests.post(url, data=payload, headers=headers)
        
        if response.status_code == 200:
            return True
        return False
        
    except Exception as e:
        print(f"Error sending OTP: {str(e)}")
        return False