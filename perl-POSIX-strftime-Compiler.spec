#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-POSIX-strftime-Compiler
Version  : 0.42
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/POSIX-strftime-Compiler-0.42.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/POSIX-strftime-Compiler-0.42.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libposix-strftime-compiler-perl/libposix-strftime-compiler-perl_0.42-1.debian.tar.xz
Summary  : 'GNU C library compatible strftime for loggers and servers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-POSIX-strftime-Compiler-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
[![Build Status](https://travis-ci.org/kazeburo/POSIX-strftime-Compiler.svg?branch=master)](https://travis-ci.org/kazeburo/POSIX-strftime-Compiler)
# NAME

%package dev
Summary: dev components for the perl-POSIX-strftime-Compiler package.
Group: Development
Provides: perl-POSIX-strftime-Compiler-devel = %{version}-%{release}

%description dev
dev components for the perl-POSIX-strftime-Compiler package.


%package license
Summary: license components for the perl-POSIX-strftime-Compiler package.
Group: Default

%description license
license components for the perl-POSIX-strftime-Compiler package.


%prep
%setup -q -n POSIX-strftime-Compiler-0.42
cd ..
%setup -q -T -D -n POSIX-strftime-Compiler-0.42 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/POSIX-strftime-Compiler-0.42/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-POSIX-strftime-Compiler
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-POSIX-strftime-Compiler/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/POSIX/strftime/Compiler.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/POSIX::strftime::Compiler.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-POSIX-strftime-Compiler/LICENSE
