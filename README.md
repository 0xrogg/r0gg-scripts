# r0gg-scripts                                                                                                                                                     
                                                                                                                                                                   
offensive security scripts built alongside HTB labs and research.                                                                                  
                                                                                                                                                                   
---                                                                                                                                                                
                                                          
## hitbutton.py — HTB Client-Side Bypass / Lucky                                                                                                                   
 
Automates repeated POST requests to an endpoint protected only by a client-side                                                                                    
`disabled` attribute. Designed for the HTB *Lucky* challenge, where the flag is
returned probabilistically and may require multiple hits.  

https://rogg.red/post.html?slug=htbcwes-using-web-proxies---skills-assessment         
                                                          
### Usage                                                                                                                                                          
                                                          
```bash                                                                                                                                                            
python3 hitbutton.py <target_url>
                                                                                                                                                                   
Example:                                                  
python3 hitbutton.py http://154.57.164.83:30361/lucky.php

Requirements                                                                                                                                                       
 
pip install requests                                                                                                                                               
                                                          
How it works

The script mirrors the exact HTTP request a browser would send if the disabled                                                                                     
attribute were removed from the button including Referer and Origin headers.
It loops up to 8 attempts and exits as soon as the flag pattern HTB{...} is                                                                                        
found in the response.                                                                                                                                    
 
Download the script:
                                                                                                                                                                            
wget https://raw.githubusercontent.com/0xrogg/r0gg-scripts/main/hitbutton.py
                                                                                                                                                                   
Usage:
python3 hitbutton.py http://154.57.164.83:30361/lucky.php 
