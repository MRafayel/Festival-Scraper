import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL").format(minDate=datetime.now().strftime('%Y-%m-%d'),
                              maxDate=(datetime.now() + timedelta(days=31)).strftime('%Y-%m-%d'))

headers = {
    "User-Agent": os.getenv("USERAGENT"),
    "Accept": "*/*"
}
