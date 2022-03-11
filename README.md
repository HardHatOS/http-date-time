# http-date-time
Set the system date and time using HTTP headers instead of NTP, which is susceptible to time attacks [1]. This script is a rewrite of [madaidan](https://github.com/madaidan)'s original code: [Secure Time Synchronization](https://gitlab.com/madaidan/secure-time-sync).

## Instructions:
This package is in the Hard Hat OS Copr repository. To install it, enter the following commands as the root user:

1. Enable the Copr repository: `dnf copr enable hardhatos/release`

2. Update the cache: `dnf update`

3. Install the package: `dnf install http-date-time`

### References
[1] https://www.whonix.org/wiki/Time_Attacks; [[Archive Link](https://web.archive.org/web/20211117201245/https://www.whonix.org/wiki/Time_Attacks)]
