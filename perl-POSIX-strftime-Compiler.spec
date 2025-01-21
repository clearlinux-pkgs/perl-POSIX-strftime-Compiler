#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : perl-POSIX-strftime-Compiler
Version  : 0.46
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/POSIX-strftime-Compiler-0.46.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/POSIX-strftime-Compiler-0.46.tar.gz
Summary  : 'GNU C library compatible strftime for loggers and servers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-POSIX-strftime-Compiler-license = %{version}-%{release}
Requires: perl-POSIX-strftime-Compiler-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build Status](https://travis-ci.org/kazeburo/POSIX-strftime-Compiler.svg?branch=master)](https://travis-ci.org/kazeburo/POSIX-strftime-Compiler)
# NAME

%package dev
Summary: dev components for the perl-POSIX-strftime-Compiler package.
Group: Development
Provides: perl-POSIX-strftime-Compiler-devel = %{version}-%{release}
Requires: perl-POSIX-strftime-Compiler = %{version}-%{release}

%description dev
dev components for the perl-POSIX-strftime-Compiler package.


%package license
Summary: license components for the perl-POSIX-strftime-Compiler package.
Group: Default

%description license
license components for the perl-POSIX-strftime-Compiler package.


%package perl
Summary: perl components for the perl-POSIX-strftime-Compiler package.
Group: Default
Requires: perl-POSIX-strftime-Compiler = %{version}-%{release}

%description perl
perl components for the perl-POSIX-strftime-Compiler package.


%prep
%setup -q -n POSIX-strftime-Compiler-0.46
cd %{_builddir}/POSIX-strftime-Compiler-0.46
pushd ..
cp -a POSIX-strftime-Compiler-0.46 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-POSIX-strftime-Compiler
cp %{_builddir}/POSIX-strftime-Compiler-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-POSIX-strftime-Compiler/220fe941787679d8a043c0444548ac186c86f309 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/POSIX::strftime::Compiler.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-POSIX-strftime-Compiler/220fe941787679d8a043c0444548ac186c86f309

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
