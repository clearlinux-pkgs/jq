#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v3
# autospec commit: 750e50d
#
Name     : jq
Version  : 1.7.1
Release  : 13
URL      : https://github.com/stedolan/jq/archive/jq-1.7.1/jq-1.7.1.tar.gz
Source0  : https://github.com/stedolan/jq/archive/jq-1.7.1/jq-1.7.1.tar.gz
Summary  : Command-line JSON processor
Group    : Development/Tools
License  : MIT
Requires: jq-bin = %{version}-%{release}
Requires: jq-lib = %{version}-%{release}
Requires: jq-license = %{version}-%{release}
Requires: jq-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : onig-dev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
jq is a command-line JSON processor

%package bin
Summary: bin components for the jq package.
Group: Binaries
Requires: jq-license = %{version}-%{release}

%description bin
bin components for the jq package.


%package dev
Summary: dev components for the jq package.
Group: Development
Requires: jq-lib = %{version}-%{release}
Requires: jq-bin = %{version}-%{release}
Provides: jq-devel = %{version}-%{release}
Requires: jq = %{version}-%{release}

%description dev
dev components for the jq package.


%package doc
Summary: doc components for the jq package.
Group: Documentation
Requires: jq-man = %{version}-%{release}

%description doc
doc components for the jq package.


%package lib
Summary: lib components for the jq package.
Group: Libraries
Requires: jq-license = %{version}-%{release}

%description lib
lib components for the jq package.


%package license
Summary: license components for the jq package.
Group: Default

%description license
license components for the jq package.


%package man
Summary: man components for the jq package.
Group: Default

%description man
man components for the jq package.


%prep
%setup -q -n jq-jq-1.7.1
cd %{_builddir}/jq-jq-1.7.1
pushd ..
cp -a jq-jq-1.7.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707079095
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707079095
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jq
cp %{_builddir}/jq-jq-%{version}/COPYING %{buildroot}/usr/share/package-licenses/jq/c4c65d618ba4ba1c37ea9c2f7c5954066d0d3bed || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/jq
/usr/bin/jq

%files dev
%defattr(-,root,root,-)
/usr/include/jq.h
/usr/include/jv.h
/usr/lib64/libjq.so
/usr/lib64/pkgconfig/libjq.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/jq/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libjq.so.1.0.4
/usr/lib64/libjq.so.1
/usr/lib64/libjq.so.1.0.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jq/c4c65d618ba4ba1c37ea9c2f7c5954066d0d3bed

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/jq.1
