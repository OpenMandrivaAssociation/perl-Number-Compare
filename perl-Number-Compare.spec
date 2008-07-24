%define module  Number-Compare
%define name	perl-%{module}
%define version 0.01
%define release %mkrel 8

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Numeric comparisons
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description 
Number::Compare compiles a simple comparison to an anonymous subroutine, which
you can call with a value to be tested again.

Now this would be very pointless, if Number::Compare didn't understand
magnitudes.

The target value may use magnitudes of kilobytes (k, ki), megabytes (m, mi), or
gigabytes (g, gi). Those suffixed with an i use the appropriate 2**n version in
accordance with the IEC standard: http://physics.nist.gov/cuu/Units/binary.html

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Number
%{_mandir}/*/*

