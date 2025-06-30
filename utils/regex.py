import re

PRODUCT_COLOR_REGEX = re.compile(r'Color:\s*([^\n\r]+)', re.IGNORECASE)