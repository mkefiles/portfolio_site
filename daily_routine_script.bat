REM Initiate VPN software, then wait until connected
START C:\"Program Files (x86)"\Cisco\"Cisco AnyConnect Secure Mobility Client"\vpnui.exe
PAUSE

REM Open other programs and file-explorer windows
START firefox
START notepad
START C:\"Program Files"\"Microsoft Office"\root\Office16\OUTLOOK.exe
EXPLORER "C:\Users\mfiles\Downloads"
EXPLORER "C:\Users\mfiles\OneDrive - loanDepot"
