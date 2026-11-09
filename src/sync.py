import os
import sys
from datetime import date, timedelta

BASE = os.environ.get("ROSTER_API_BASE", "https://roster-api-int.sandsmacao.com/v2")


def window(days):
    today = date.today()
    return today, today + timedelta(days=days)


def main(argv):
    start, end = window(int(os.environ.get("SYNC_WINDOW_DAYS", "7")))
    print(f"syncing rosters {start} to {end} from {BASE}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
