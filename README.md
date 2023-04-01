# Attack of the XSS

Poison a JWT and return a different user.

1. Attacker finds API that has an endpoint open 
2. The secret is available in almost plain text (md5)
3. Use secret to decrypt JWT and sign a new one
4. 