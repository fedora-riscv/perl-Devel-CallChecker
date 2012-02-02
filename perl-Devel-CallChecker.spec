# This file is licensed under the terms of GNU GPLv2+.
Name:           perl-Devel-CallChecker
Version:        0.004
Release:        1%{?dist}
Summary:        Custom op checking attached to subroutines
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Devel-CallChecker/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Devel-CallChecker-%{version}.tar.gz
BuildRequires:  perl(DynaLoader::Functions)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File) >= 1.03
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
# Tests:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# XXX: This package stores build-time Perl version and checks it at run-time.
# This package must be recompiled on each Perl upgrade. See bug #754159.
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(DynaLoader)
Requires:       perl(Exporter)
Requires:       perl(IO::File) >= 1.03

%{?perl_default_filter}

%description
This module makes some new features of the Perl 5.14.0 C API available to
XS modules running on older versions of Perl. The features are centered
around the function cv_set_call_checker, which allows XS code to attach a
magical annotation to a Perl subroutine, resulting in resolvable calls to
that subroutine being mutated at compile time by arbitrary C code. This
module makes cv_set_call_checker and several supporting functions
available. (It is possible to achieve the effect of cv_set_call_checker
from XS code on much earlier Perl versions, but it is painful to achieve
without the centralized facility.)

%prep
%setup -q -n Devel-CallChecker-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
* Thu Feb 02 2012 Petr Pisar <ppisar@redhat.com> - 0.004-1
- 0.004 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 Petr Pisar <ppisar@redhat.com> - 0.003-2
- Rebuild against Perl 5.14.2 (bug #754159)

* Mon Jul 11 2011 Petr Pisar <ppisar@redhat.com> 0.003-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr
