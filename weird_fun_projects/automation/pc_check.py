import subprocess

def safe_check():
    results = subprocess.run([
        'bash', '-c',
        'echo "=== PRIVACY LEAK TEST ===" && echo "IPv4 (should show VPN):" && curl -s https://ipinfo.io | grep -E \'"ip"|"city"|"country"\' && echo "IPv6 (should timeout/fail):" && timeout 5 curl -s https://ipv6.icanhazip.com || echo "IPv6 BLOCKED ✅" && echo "DNS Leak Test:" && dig +short @8.8.8.8 whoami.akamai.net && echo "WebRTC Local IP:" && ip route get 8.8.8.8 | grep -oP \'src \\K\\S+\' && echo "Open Ports:" && sudo ss -tulpn | grep -E "LISTEN.*\\*:" | wc -l && echo "Done - Check results above"'

    ],  capture_output=True, text=True)
    print(results.stdout)
    
    
safe_check()