# config.py

# List of malicious patterns for WAF (Regular Expressions)
patterns = [
    r'<script.*?>.*?</script>',  # Detects <script> tags
    r'(?i)union.*select.*from',  # Detects SQL injection attempts
    r'(?i)base64_decode',       # Detects base64 encoding attempts
    r'(?i)eval\(.*\)',           # Detects eval function usage
    r'(?i)alert\(',              # Detects JavaScript alerts
]

# Optionally, you can add more configuration settings, such as logging or rate-limiting.
