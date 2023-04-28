from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime
import json

def handler(event, context):
    load_dotenv()

    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")

    time: str = str(datetime.utcnow())

    supabase: Client = create_client(url, key)
    
    res = supabase.table("User").update({
        "searchQuota": 5,
        "quotaRefreshTs": time
        }).eq("role", "FREEUSER").execute()
    
    return json.dumps(res, default=str)