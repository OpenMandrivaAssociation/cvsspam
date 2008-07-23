%define name	cvsspam
%define version 0.2.12
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	CVSspam emails you diffs when someone commits a change to your CVS repository
License:	GPL
Group:		System/Servers
Source:		http://www.badgers-in-foil.co.uk/projects/cvsspam/releases/%{name}-%{version}.tar.bz2
URL:		http://www.badgers-in-foil.co.uk/projects/cvsspam/
Requires:	cvs
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CVSspam sends email when a change is committed to the CVS repository.
Syntax-highlighted diffs describe the changes made, and links to Web
frontends on CVS and bug tracking systems are generated where
possible.

%prep
%setup -q

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 *.rb %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 cvsspam.conf %{buildroot}%{_sysconfdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS TODO cvsspam-doc.pdf cvsspam-doc.html
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf

