import re
def validateIPAddress(queryIP):
    return_value = ""
    
    pattern_ipv4 = "^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$"
    
    pattern_ipv6 = "^([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])\:([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])\:([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])\:([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])\:([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])\:([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])\:([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])\:([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F][0-9a-fA-F]|[0-9a-fA-F])$"
    
    
    if re.search(pattern=pattern_ipv4, string=queryIP):
        return_value = "IPV4"
    elif re.search(pattern=pattern_ipv6, string=queryIP):
        return_value = "IPV6"
    else:
        return_value = "Neither"

    return return_value
    
if __name__ == "__main__":
    final_value = validateIPAddress("1.0.1.")
    print(final_value)