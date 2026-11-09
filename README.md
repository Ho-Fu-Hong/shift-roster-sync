# Shift Roster Sync

Nightly job that syncs staff shift rosters from the Sands Macao partner portal
(`roster-api-int.sandsmacao.com`) into the scheduling service.

## Setup

1. Copy `config/roster.env` and fill in the service account.
2. Run `python src/sync.py --date today`.

The job runs at 02:00 HKT and writes a summary to `logs/sync.log`.
