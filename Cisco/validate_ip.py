import re
def validateIPAddress(queryIP):
    return_value = ""
    
    ipv4 = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
    pattern_ipv4 = re.compile(r'^(' + ipv4 + r'\.){3}' + ipv4 + r'$')
    
    ipv6 = r"[0-9a-fA-F]{1,4}"
    pattern_ipv6 = re.compile(r'^(' + ipv6 + r'\:){7}' + ipv6 + r'$')
    
    if re.match(pattern=pattern_ipv4, string=queryIP):
        return_value = "IPv4"
    elif re.match(pattern=pattern_ipv6, string=queryIP):
        return_value = "IPv6"
    else:
        return_value = "Neither"

    return return_value
    
if __name__ == "__main__":
    final_value = validateIPAddress("12.12.12")
    print(final_value)