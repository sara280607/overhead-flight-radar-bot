# ✈️ Automated Overhead Airspace Radar & Telegram Notification Engine

An enterprise-ready, event-driven aviation tracking application built with Python. This script establishes a virtual radar grid over a target geographic coordinate using direct API endpoints. When a physical transponder signature cuts through the designated airspace, the system extracts the live flight parameters, structures a plain-text payload, and deploys an instant notification banner directly to a user's mobile device via the Telegram Bot API framework.

## 🚀 Architectural Deep Dive
- **Official API Abstraction**: Leverages `pyTelegramBotAPI` to abstract transmission pipelines, ensuring error-resilient connections that bypass local system string deconstructions.
- **Dynamic Bounded Radius**: Utilizes a coordinate-point vector geometry query (`/v2/point/`) to restrict processing scopes specifically to the target location, preventing server and network overhead.
- **State-Isolation Cache**: Implements an localized runtime signature verification memory (`notified_aircraft = set()`) to track flights across scanning intervals, guaranteeing precisely one alert banner push per flight entry.
- **Fail-Safe Sanitization**: Encapsulates variables within protective data sanitization layers to automatically inject fallback attributes (`N/A`) if the incoming satellite server transmission contains missing parameters.

## 🛠️ Execution & Deployment Guide

### 1. Provision Local System Dependencies
Open your system console or terminal environment and execute the underlying command to map the necessary network processing engines:
```bash
pip install pyTelegramBotAPI requests
```

### 2. Configure Local Authentication Keys
Open your cloned `main.py` template file and configure the target settings container with your real-world coordinates and secret authorization tokens:
```python
# ==================== GUARANTEED CONFIGURATION ====================
TELEGRAM_TOKEN = "your_private_chatid:alphanumeric_bot_token"
TELEGRAM_CHAT_ID = your_numerical_account_id_without_quotes

MY_LATITUDE = 17.345    # Update to your roof latitude
MY_LONGITUDE = 75.453   # Update to your roof longitude
SCAN_RADIUS_NM = 15        # Airspace tracking sweep area radius
# ==================================================================
```

### 3. Initiate the Background Process Loop
Initialize the live tracker terminal application:
```bash
python flight_git.py
```

---

## 🛰️ Real-Time Production Output Log Architecture
When an active transponder intersects your perimeter, the application handles telemetry parsing and outputs execution updates directly into your command-line workspace:

```text
Connecting securely to official Telegram communication pipeline...
🔒 Official Certified Live Flight Radar Launched Successfully!
---------------------------------------------------------------------------
🕒 [14:45:02] Radar active. Scanning airspace bubble...
✈️ RADAR SPOTTED FLIGHT: IGO6166
🟢 SUCCESS! Flight details pushed to your phone top screen!
🕒 [14:45:32] Radar active. Scanning airspace bubble...
```
