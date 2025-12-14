from datetime import datetime
from .models import DailyOperatingHours

def get_today_operating_hours():
    today_day = datetime.now().strftime('%A')

    try:
        operating_hours = DailyOperatingHours.objects.get(daya=today_day)

        return operating_hours.open_time,operating_hours.close_time

        except DailyOperatingHours.DoesNotExit:
            return None,None