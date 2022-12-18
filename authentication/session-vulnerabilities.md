# Common Session Vulnerabilities

## [Session Fixation](https://secureteam.co.uk/articles/web-application-security-articles/understanding-session-fixation-attacks/)

An attacker obtains or generates a valid session ID and tricks victim to authenticating with that session ID. Attacked uses the SDI to impersonate the victim in the session.

### Mitigation
- Ensure that the session ID changes when a user logs in.
- Ensure every session ID is generated on the server.
- Don’t expose session IDs in GET/POST params.
- Ensure sessions are revoked on logout.
- Set reasonable session expiration.

## [Cross site scripting (XSS)](https://pentest-tools.com/blog/xss-attacks-practical-scenarios)

An attacker injects malicious script onto page. Script can access cookies with session IDs and hijack user’s session. 

### Mitigation
- Set HTTPOnly flag on session cookie (don’t allow JS to access)
- Set Secure flag (restrict to HTTPS)
- Use CSP policies

## [Cross Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf)
An attacker tricks an authenticated victim into performing actions on attacker’s behalf. Takes advantage of the fact that the browser sends session cookie along automatically with each request.

### Mitigation
- Tie a CSRF token to user session


# Common JWT Vulnerabilities

## Changing the JWT header alg field to: none

An attacker can modify the JWT header alg field to `none`, not provide a signature, and some JWT validation implementations may accept the JWT as correctly signed.

### Mitigation
- Use a JWT library that fails tokens with a none alg field.
- Specify the expected algorithm to use during token validation.
 
## Changing  the JWT header alg from an asymmetric algorithm to a symmetric one

An attacker can modify the JWT header alg field from an asymmetric algorithm (RS256) to a symmetric one (HS256).
 
### Mitigation
- Never let the JWT or its header drive the verification process alone.
- Specify the expected algorithm to use during token validation.
 
## Brute-forcing weak secret keys

An attacker can brute force guess the key used to sign a JWT.

### Mitigation
- Ensure secret used to sign JWT is string and unique enough.

## Leaking the secret key

An attacker can exploit vulnerabilities in where the key is stored and use it to sign arbitrary tokens.

## Manipulating the KID

KID = Key ID, an optional JWT header field that allows developers to specify the key used to verify the token (retrieves key file from file system). 
Directory traversal attack
- An attacker can modify the field and specify a separate file in the filesystem as the key.
- SQL injections
  - The KID could also be used to retrieve the key from a DB.
  - An attacker can use this injection to return any value.
  - Command injections
  - JKU/JWK/x5u/x5c headers used sending rogue keys

## Information leaks
- If the token is unencrypted, anyone can base64 decode it.

### Mitigation
- Consider additionally encrypting the JWT

-- 

# Resources

https://github.com/ticarpi/jwt_tool/wiki
https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
