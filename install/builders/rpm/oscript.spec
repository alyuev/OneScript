%global debug_package %{nil}
%define _version 1.0.13

Name:           onescript-engine
Version:        %{_version}
Release:        1%{?dist}
Summary:        1Script execution engine.

License:        MPL 2.0
URL:            https://github.com/EvilBeaver/OneScript
Source0:        OneScript-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	wget
Requires:		mono-core

%define _empty_manifest_terminate_build 0
%define _subdir OneScript-%{version}

%description
1Script execution engine.
  Cross-platform scripting engine
  for DevOps who use 1C:Enterprise Platform (http://1c-dn.com/1c_enterprise)

%prep
pwd
%setup -c %{source0}

%build
echo "build"
pwd

%install
%{__rm} -rf %{buildroot}
pushd %{_subdir}
mkdir -p %{buildroot}%{_datadir}/oscript/
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
install -p oscript -m 755 %{buildroot}%{_bindir}/oscript
rm oscript
%{__cp} -fpr ./ %{buildroot}%{_datadir}/oscript/
popd

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/oscript/*
%doc



%changelog
* Sat Apr 23 2016 shenja@sosna.zp.ua
-