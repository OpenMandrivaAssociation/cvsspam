%define name	cvsspam
%define version 0.2.12
%define release  8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Emails you diffs when someone commits a change to your CVS repository
License:	GPL
Group:		System/Servers
Source:		http://www.badgers-in-foil.co.uk/projects/cvsspam/releases/%{name}-%{version}.tar.bz2
URL:		http://www.badgers-in-foil.co.uk/projects/cvsspam/
Requires:	cvs
BuildArch:	noarch

%description
CVSspam sends email when a change is committed to the CVS repository.
Syntax-highlighted diffs describe the changes made, and links to Web
frontends on CVS and bug tracking systems are generated where
possible.

%prep
%setup -q

%install

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 *.rb %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 cvsspam.conf %{buildroot}%{_sysconfdir}/%{name}

%clean

%files
%doc CREDITS TODO cvsspam-doc.pdf cvsspam-doc.html
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.12-6mdv2011.0
+ Revision: 617486
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.2.12-5mdv2010.0
+ Revision: 425822
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.12-4mdv2009.0
+ Revision: 243839
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.2.12-2mdv2008.1
+ Revision: 123613
- kill re-definition of %%buildroot on Pixel's request
- import cvsspam


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.12-2mdv2007.0
- %%mkrel

* Fri Jul 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.12-1mdk 
- New release 0.2.12
- fix source URL

* Sun Jun 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.11-2mdk 
- fix config file location

* Sun Jun 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.11-1mdk 
- first mdk release
