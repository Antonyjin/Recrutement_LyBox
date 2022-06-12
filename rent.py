#!/usr/bin/env python3
import re

def ExtractRent(content):
    pattern = '\d+'
    result = re.match(pattern, content)
    print(result)

content = "fjrk400porte43fjr324jfrejff12"
ExtractRent(content)