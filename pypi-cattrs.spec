#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cattrs
Version  : 22.2.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/fc/da/ff3239eb4241cbc6f8b69f53d4ca27a178d51f9e5a954f1a3588c8227dc5/cattrs-22.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/da/ff3239eb4241cbc6f8b69f53d4ca27a178d51f9e5a954f1a3588c8227dc5/cattrs-22.2.0.tar.gz
Summary  : Composable complex class support for attrs and dataclasses.
Group    : Development/Tools
License  : MIT
Requires: pypi-cattrs-license = %{version}-%{release}
Requires: pypi-cattrs-python = %{version}-%{release}
Requires: pypi-cattrs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
======
cattrs
======
.. image:: https://img.shields.io/pypi/v/cattrs.svg
:target: https://pypi.python.org/pypi/cattrs

%package license
Summary: license components for the pypi-cattrs package.
Group: Default

%description license
license components for the pypi-cattrs package.


%package python
Summary: python components for the pypi-cattrs package.
Group: Default
Requires: pypi-cattrs-python3 = %{version}-%{release}

%description python
python components for the pypi-cattrs package.


%package python3
Summary: python3 components for the pypi-cattrs package.
Group: Default
Requires: python3-core
Provides: pypi(cattrs)
Requires: pypi(attrs)
Requires: pypi(exceptiongroup)

%description python3
python3 components for the pypi-cattrs package.


%prep
%setup -q -n cattrs-22.2.0
cd %{_builddir}/cattrs-22.2.0
pushd ..
cp -a cattrs-22.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664806487
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cattrs
cp %{_builddir}/cattrs-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cattrs/3653db1449ea3f615f459c4fe8abea217a320666 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cattrs/3653db1449ea3f615f459c4fe8abea217a320666

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
