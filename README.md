# Password-Sentinel

A lightweight Python CLI tool that evaluates password strength using length, character diversity, and a common-password blocklist check.

Features


Length scoring — rewards passwords of 12+ characters, flags anything under 8 as too short
Character diversity check — scores presence of uppercase, lowercase, digits, and special characters
Common password blocklist — rejects well-known weak passwords (password, 123456, qwerty, letmein, admin)
Heuristic weak-pattern flag — an additional lightweight check using a SHA-256 hash prefix as a simple weak-pattern heuristic
Plain-English feedback — returns a human-readable strength verdict (Weak / Moderate / Strong) instead of just a score


How it works

The script scores a password out of a small point total based on length and character-class diversity, then maps that score to a strength verdict. Passwords matching the common-password blocklist are rejected outright regardless of score.

Requirements


Python 3.x (standard library only — no external dependencies)


Usage

bashpython3 pass-strength.py

You'll be prompted to enter a password, and the tool will print a strength verdict, e.g.:

Enter your password: Tr0ub4dor&3
Strong password! Keep it safe and avoid reusing it on multiple sites.

Roadmap / Possible Improvements


Replace the current SHA-256 prefix heuristic with a proper entropy calculation (e.g. Shannon entropy or zxcvbn-style scoring)
Expand the common-password blocklist using a real breached-password dataset (e.g. rockyou.txt or HaveIBeenPwned's Pwned Passwords API)
Add CLI flags for non-interactive/scripted use (e.g. --password, --json output)


License

No license file currently included — consider adding MIT for clarity on reuse.
