%define modname	Number-Compare
%define modver 0.03

Summary:	Numeric comparisons
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Number-Compare-%{modver}.tar.gz
Url:		http://search.cpan.org/dist/%{modname}
BuildArch:	noarch
BuildRequires:	perl-devel

%description 
Number::Compare compiles a simple comparison to an anonymous subroutine, which
you can call with a value to be tested again.

Now this would be very pointless, if Number::Compare didn't understand
magnitudes.

The target value may use magnitudes of kilobytes (k, ki), megabytes (m, mi), or
gigabytes (g, gi). Those suffixed with an i use the appropriate 2**n version in
accordance with the IEC standard:	http://physics.nist.gov/cuu/Units/binary.html

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*


