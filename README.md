# Rain Alert

This project fetches weather data from OpenWeatherMap and sends an SMS via Twilio with a short rain alert and the day's temperature range.

## Requirements

- Python 3.11+
- An OpenWeatherMap API key
- A Twilio account (SID, Auth Token, phone numbers)

## Local Run

1. Install dependencies:
   ```bash
   pip install requests twilio
   ```
2. Set environment variables:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `MY_LAT`
   - `MY_LONG`
   - `OWN_API_KEY`
   - `MY_NUMBER`
   - `VIRTUAL_NUMBER`
3. Run the script:
   ```bash
   python main.py
   ```

## GitHub Actions

The workflow file is located at:

- `.github/workflows/rain-alert.yml`

It is triggered by:

- `workflow_dispatch` (manual)
- `schedule` via cron: `0 7 * * *` (daily at 07:00 UTC)

### Required GitHub Secrets

Create the following secrets under `Settings > Secrets and variables > Actions`:

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `MY_LAT`
- `MY_LONG`
- `OWN_API_KEY`
- `MY_NUMBER`
- `VIRTUAL_NUMBER`
