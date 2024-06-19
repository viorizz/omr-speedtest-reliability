import speedtest
import time
import json
from datetime import datetime

duration_hours = 12
interval_seconds = 60
results = []

end_time = time.time() + duration_hours * 3600

while time.time() < end_time:
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        st.get_best_server()

        timestamp = datetime.now().strftime("%H:%M:%S")

        # Extract and format the results
        download_mbps = round(st.results.download / 10**6, 1)  # Convert to Mbps
        upload_mbps = round(st.results.upload / 10**6, 1)      # Convert to Mbps
        ping = round(st.results.ping, 1)                         # Round to one decimal place

        result = {
            "timestamp": timestamp,
            "download": download_mbps,  
            "upload": upload_mbps,
            "ping": ping,
        }
        results.append(result)
        print(f"[{timestamp}] Connection still going strong 💪, no down for now\n[ 🔼 {upload_mbps}Mb/s | 🔽 {download_mbps}Mb/s | ⏱️ {ping}ms ]")
    except Exception as e:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Connection is down sadly 😭 Error: {e}")

    time.sleep(interval_seconds)

with open("speedtest_results.json", "w") as f:
    json.dump(results, f, indent=4)
