%define upstream_name    Number-Compare
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary: 	Numeric comparisons
License: 	GPL+ or Artistic
Group: 		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/%{upstream_name}-%{upstream_version}.tar.bz2
Url:        http://search.cpan.org/dist/%{upstream_name}

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

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
