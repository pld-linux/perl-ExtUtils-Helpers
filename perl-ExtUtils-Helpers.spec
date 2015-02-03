#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	Helpers
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils::Helpers - Various portability utilities for module builders
Summary(pl.UTF-8):	ExtUtils::Helpers - narzędzia ułatwiające przenośność dla budowniczych modułów
Name:		perl-ExtUtils-Helpers
Version:	0.022
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cf4fd6f8caa6daac33b1111c9e93162b
URL:		http://search.cpan.org/dist/ExtUtils-Helpers/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(Exporter)
BuildRequires:	perl-Text-ParseWords >= 3.24
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/Helpers.pm
%{perl_vendorlib}/ExtUtils/Helpers
%{_mandir}/man3/ExtUtils::Helpers*.3pm*
