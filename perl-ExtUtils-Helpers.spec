#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	Helpers
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils::Helpers - Various portability utilities for module builders
#Summary(pl.UTF-8):	
Name:		perl-ExtUtils-Helpers
Version:	0.021
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94aa8eaf92def26d9af0cb25fcb1570f
URL:		http://search.cpan.org/dist/ExtUtils-Helpers/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides various portable helper functions for module
building modules.

# %description -l pl.UTF-8
# TODO

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
%doc Changes INSTALL README
%{perl_vendorlib}/ExtUtils/*.pm
%{perl_vendorlib}/ExtUtils/Helpers
%{_mandir}/man3/*
