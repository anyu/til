# Mail Transfer Agent (MTA)

Sendmail, Postfix are commonly used MTAs.

## Sendmail
- one of the oldest, most well-known MTA for Unix systems
- highly flexible (advanced routing, security policies, custom filtering, etc), but more difficult to manage
- historically was a target for exploits, but has had more security enhancements
- supports SMTP
- config files: `/etc/mail/sendmail.cf`, `/etc/mail/submit.cf`

## Postfix
- more modern MTA, designed to be drop-in replacement for Sendmail
- one of the most popular MTAs and the default on many Linux distros
- simpler to configure, manage
- designed with security in mind
- more performant than Sendmail when handling large volumes

### On macOS
- macOS uses Postfix as local MTA (for system-generated email - alerts, logs), not for sending email via Gmail, Outlook, etc.
