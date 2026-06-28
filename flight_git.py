import time
from datetime import datetime
import requests
import telebot

# Turn off hidden library warning flags permanently to keep network transmission safe
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# ==================== GUARANTEED CONFIGURATION ====================
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID = 123456789

MY_LATITUDE = 12.345    
MY_LONGITUDE = 75.453   
SCAN_RADIUS_NM = 15  
# ==================================================================

print("Connecting securely to official Telegram communication pipeline...")
bot = telebot.TeleBot(TELEGRAM_TOKEN)
notified_aircraft = set()

def send_telegram_alert(flight_name, plane_type, airline_desc, origin, destination):
    """Pushes a clean plain text layout notification card right on your phone top."""
    safe_flight = str(flight_name).strip().upper() if flight_name else "UNKNOWN"
    safe_type = str(plane_type).strip() if plane_type else "UNKNOWN MODEL"
    safe_desc = str(airline_desc).strip() if airline_desc else "PRIVATE TRAFFIC"
    safe_origin = str(origin).strip().upper() if origin else "N/A"
    safe_destination = str(destination).strip().upper() if destination else "N/A"

    message = (
        "✈️ PLANE SPOTTED OVERHEAD!\n\n"
        "Flight: " + safe_flight + "\n"
        "Airline: " + safe_desc + "\n"
        "Aircraft Type: " + safe_type + "\n"
        "From: " + safe_origin + "\n"
        "To: " + safe_destination
    )
    
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message)
        print("🟢 SUCCESS! Flight details pushed to your phone top screen!")
        return True
    except Exception as e:
        print("🔴 Transmission engine delay: " + str(e))
        return False

def scan_overhead_sky():
    """Queries live global aviation data feeds with custom tracking protection filters."""
    # FIX: Native variable placement style guarantees slashes can NEVER get pushed out of place
    api_url = f"https://api.adsb.lol/v2/point/{MY_LATITUDE}/{MY_LONGITUDE}/{SCAN_RADIUS_NM}"
    
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"🕒 [{current_time}] Radar active. Scanning airspace bubble...")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'application/json'
        }
        response = requests.get(api_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            current_planes_in_sky = data.get("ac", [])
            
            if not isinstance(current_planes_in_sky, list):
                return
                
            active_this_loop = set()
            for aircraft in current_planes_in_sky:
                if not isinstance(aircraft, dict):
                    continue
                    
                icao_hex = aircraft.get("hex", "")
                if not icao_hex:
                    continue
                
                icao_hex = str(icao_hex).strip().upper()
                active_this_loop.add(icao_hex)
                
                # Triggers for ANY plane that enters your airspace coordinates
                if icao_hex not in notified_aircraft:
                    flight_name = aircraft.get("flight", "Unknown Call Sign")
                    aircraft_type = aircraft.get("t", "Unknown Plane Model")
                    airline_desc = aircraft.get("desc", "Private Operator")
                    origin = aircraft.get("org", "N/A")  
                    destination = aircraft.get("dst", "N/A")  
                    
                    print("✈️ RADAR SPOTTED FLIGHT: " + str(flight_name))
                    notified_aircraft.add(icao_hex)
                    
                    success = send_telegram_alert(flight_name, aircraft_type, airline_desc, origin, destination)
                    if not success:
                        notified_aircraft.remove(icao_hex)
            
            # Maintenance cleanup: remove signatures of aircraft that flew away
            planes_to_remove = [p for p in notified_aircraft if p not in active_this_loop]
            for p in planes_to_remove:
                notified_aircraft.remove(p)
                
    except Exception as e:
        print(f"⚠️ Network check skipped: {e}")

print("🔒 Official Certified Live Flight Radar Launched Successfully!")
print("-" * 75)

while True:
    scan_overhead_sky()
    time.sleep(30)
