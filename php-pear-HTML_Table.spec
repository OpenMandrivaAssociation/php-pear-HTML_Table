%define		_class		HTML
%define		_subclass	Table
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.8.3
Release:	4
Summary:	Makes HTML tables easy, flexible, reusable and efficient
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Table/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The PEAR::HTML_Table package provides methods for easy and efficient
design of HTML tables.
- Lots of customization options.
- Tables can be modified at any time.
- The logic is the same as standard HTML editors.
- Handles col and rowspans.
- PHP code is shorter, easier to read and to maintain.
- Tables options can be reused.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.3-3mdv2011.0
+ Revision: 667506
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.3-2mdv2011.0
+ Revision: 607106
- rebuild

* Sun Apr 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.3-1mdv2010.1
+ Revision: 538751
- update to new version 1.8.3

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.2-4mdv2010.1
+ Revision: 477884
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.8.2-3mdv2010.0
+ Revision: 426642
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.2-2mdv2009.1
+ Revision: 321862
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.2-1mdv2009.0
+ Revision: 272589
- 1.8.2

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.8.0-3mdv2009.0
+ Revision: 224742
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-2mdv2008.1
+ Revision: 178513
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-1mdv2008.0
+ Revision: 28896
- 1.8.0

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.7.5-1mdv2008.0
+ Revision: 15540
- 1.7.5


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-1mdv2007.0
+ Revision: 81105
- Import php-pear-HTML_Table

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.0-1mdk
- 1.7.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-3mdk
- new group (Development/PHP)

* Tue Nov 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.6.1-2mdk
- Install Table/Storage.php too
- Shorten summary too long

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6.1-1mdk
- 1.6.1

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5-1mdk
- initial Mandriva package (PLD import)

