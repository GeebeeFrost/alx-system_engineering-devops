# Postmortem

## Issue Summary

There was an outage on an isolated Ubuntu 14.04 container running a WordPress application on an Apache web server for about 2 hours between 8:20am and 10:15am West African Time on Monday, 16th January, 2023. This caused users to recieve an error message of "500 - Internal Server Error" when trying to access the site. The cause of the issue was a typographical error in the WordPress configuration settings.

## Timeline

- Time detected - 9:00am, Monday 16th January, 2023
- How the issue was detected - a user called in to complain
- Actions taken - the Apache web server was initially thought to be the root cause of the issue and the following actions were taken in that regard:

  - Apache server was restarted;
  - Ubuntu container was restarted.
    These actions did not fix the issue.

- Escalation - the issue was escalated to me, Gbolahan Oyeniyi, renowned debugger and developer.
- Resolution - the issue was resolved by correcting a typographical error in a Wordpress configuration file (/var/www/html/wp-settings.php)

## Root Cause & Resolution

- The issue was being caused by a typographical error - The extension for a file was written as "phpp" instead of "php".
- After checking running processes using `ps`, two processes - `root` and `www-data` were running correctly.
- `strace` debugger reported an error `ENOENT (No such file or directory)` when attempting to access the file `/var/www/html/wp-includes/class-wp-locale.phpp`.
- Checked through the `wp-settings.php` file to locate the erroneous configuration. Found it on line 137 using Vim pattern matching.
- Removed the erroneous `p` from the extension.
- Ran the `curl` command again and the issue was fixed.

## Corrective & Preventive Measures

- Daily testing should be done on the servers.
- I wrote a Puppet manifest to automate this process in case it comes up again.
