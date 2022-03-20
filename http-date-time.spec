BuildArch: noarch
License: AGPLv3
Name: http-date-time
Recommends: tor
Release: 1%{?dist}
Requires: curl, python3
Source0: http-date-time
Source1: pool.txt
Source2: http-date-time.service
Source3: http-date-time-tor.service
Source4: http-date-time.timer
Source5: http-date-time-tor.timer
Source6: http-date-time.8
Summary: Set the date and time using HTTP headers
URL: https://github.com/HardHatOS/http-date-time
Version: 1.0

%description
Obtain the date and time from HTTP headers rather than NTP, which is unencrypted and susceptible to time attacks. By default, only non-Tor/clearnet URLs are used but Tor mode can be enabled to connect to only onion domains instead.

%pre
# RPM macro for the directory that will contain the pool.txt file of URLs to use
%define _pooldir %{_sysconfdir}/http-date-time

# RPM macro for the systemd directory where service files are located
%define _servicedir %{_prefix}/lib/systemd/system

%install
# Copy the Python script into /usr/bin
%{__install} -D %{SOURCE0} -t %{buildroot}%{_bindir}

# Copy the pool.txt file into the pool directory defined above
%{__install} -D -m 0644 %{SOURCE1} -t %{buildroot}%{_pooldir}

# Copy the systemd service files and their timers to the systemd service file directory
%{__install} -D -m 0644 %{SOURCE2} -t %{buildroot}%{_servicedir}
%{__install} -D -m 0644 %{SOURCE3} -t %{buildroot}%{_servicedir}
%{__install} -D -m 0644 %{SOURCE4} -t %{buildroot}%{_servicedir}
%{__install} -D -m 0644 %{SOURCE5} -t %{buildroot}%{_servicedir}

# Copy the man page to the section 8 man page directory
%{__install} -D -m 0644 %{SOURCE6} -t %{buildroot}%{_mandir}/man8

%files
%{_bindir}/http-date-time
%{_pooldir}/pool.txt
%{_servicedir}/http-date-time.service
%{_servicedir}/http-date-time-tor.service
%{_servicedir}/http-date-time.timer
%{_servicedir}/http-date-time-tor.timer
%{_mandir}/man8/http-date-time.8.*

%post
# Create a new user 'datetime' that will be used to set the system date and time
useradd --no-create-home --system --shell /usr/sbin/nologin datetime

%postun
# Remove the configuration file directory in /etc
%{__rm} -rf %{_pooldir}

# Remove the 'datetime' user
userdel datetime
