import time
from datetime import datetime

def add_gigasecond(date):
	future_date = time.mktime(date.utctimetuple()) + 1e9
	return datetime.fromtimestamp(future_date)