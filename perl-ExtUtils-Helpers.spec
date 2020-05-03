#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	Helpers
Summary:	ExtUtils::Helpers - Various portability utilities for module builders
Summary(pl.UTF-8):	ExtUtils::Helpers - narzędzia ułatwiające przenośność dla budowniczych modułów
Name:		perl-ExtUtils-Helpers
Version:	0.026
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83b00c1e401321c425ae5db6b2b2fd12
URL:		https://metacpan.org/release/ExtUtils-Helpers
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(Exporter)
BuildRequires:	perl-Text-ParseWords >= 3.24
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides various portable helper functions for module
building modules.

%description -l pl.UTF-8
Ten moduł dostarcza różne przenośne funkcje pomocnicze dla modułów
budujących moduły.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# foreign OSs (avoid ExtUtils::PL2Bat dependency)
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/Helpers/{VMS,Windows}.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/Helpers.pm
%{perl_vendorlib}/ExtUtils/Helpers
%{_mandir}/man3/ExtUtils::Helpers*.3pm*
