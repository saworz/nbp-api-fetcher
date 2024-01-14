from datetime import datetime, timedelta


def format_date(days_delta: int) -> str:
    """Return date days_delta prior to today in format YYYY-MM-DD"""
    date = datetime.now() - timedelta(days=days_delta)
    return date.strftime("%Y-%m-%d")
