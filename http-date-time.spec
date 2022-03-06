Name:       http-date-time
Version:    1.0
Release:    1%{?dist}
Summary:    Set the date and time using HTTP headers

Group:      System Environment/Base
License:    AGPLv3
URL:        https://github.com/HardHatOS/http-date-time
Source0:    http-date-time
Source1:    pool.txt
BuildArch:  noarch
Requires:   curl, python3
Recommends:	tor

%description
Obtain the date and time from HTTP headers rather than NTP, which is unencrypted and susceptible to time attacks. By default, only non-Tor/clearnet URLs are used but Tor mode can be enabled to connect to only onion domains instead.

%pre
# RPM macro for the directory that will contain the pool.txt file of URLs to use
%define _pooldir %{_sysconfdir}/http-date-time

%install
# Copy the Python script into /usr/bin
install -D -m 755 %{SOURCE0} -t %{buildroot}%{_bindir}

# Copy the pool.txt file into the pool directory defined above
install -D %{SOURCE1} -t %{buildroot}%{_pooldir}

%files
%{_bindir}/http-date-time
%{_pooldir}/pool.txt

%postun
# Remove the configuration file directory
%{__rm} -rf %{_pooldir}
