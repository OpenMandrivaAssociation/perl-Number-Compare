%define upstream_name    Number-Compare
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Numeric comparisons
License:	GPL+ or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/%{upstream_name}-%{upstream_version}.tar.bz2
Url:		http://search.cpan.org/dist/%{upstream_name}

BuildRequires:	perl-devel
BuildArch:	noarch

%description 
Number::Compare compiles a simple comparison to an anonymous subroutine, which
you can call with a value to be tested again.

Now this would be very pointless, if Number::Compare didn't understand
magnitudes.

The target value may use magnitudes of kilobytes (k, ki), megabytes (m, mi), or
gigabytes (g, gi). Those suffixed with an i use the appropriate 2**n version in
accordance with the IEC standard: http://physics.nist.gov/cuu/Units/binary.html

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Number
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-4mdv2012.0
+ Revision: 765540
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-3
+ Revision: 764063
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2
+ Revision: 676633
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 404279
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-9mdv2009.0
+ Revision: 258141
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-8mdv2009.0
+ Revision: 246252
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.01-6mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdv2008.0
+ Revision: 86719
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-5mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-4mdk
- spec cleanup
- better URL
- %%mkrel
- rpmbuildupdate aware

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-3mdk
- fix buildrequires in a backward compatible way

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-2mdk 
- fix directory ownership (distlint)

* Fri Apr 02 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-1mdk
- first mdk release

