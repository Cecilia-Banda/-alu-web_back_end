#!/usr/bin/env python3
"Filter datum"
import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(fr'({separator.join(fields)})=(.*?){separator}', fr'\1={redaction}{separator}', message)
