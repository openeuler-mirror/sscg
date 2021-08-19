Name:           sscg
Version:        2.6.2
Release:        2
Summary:        Simple Signed Certificate Generator
License:        GPL-3.0 
URL:            https://github.com/sgallagher/sscg
Source0:        https://github.com/sgallagher/sscg/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc libtalloc-devel openssl-devel popt-devel libpath_utils-devel meson ninja-build help2man

%description
SSCG(Simple Signed Certificate Generator) makes it easy to generate usable and secure
"self-signed" certificates.The certificates created by this tool are generated in a way
so as to create a CA certificate that can be safely imported into a client machine to trust
the service certificate without needing to set up a full PKI environment and without exposing
the machine to a risk of false signatures from the service certificate.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%pre

%preun

%post

%postun

%files
%defattr(-,root,root)
%license COPYING
%doc README.md
%{_bindir}/sscg
%{_mandir}/man8/sscg.8*

%changelog
* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 2.6.2-2
- DESC: delete -Sgit from %autosetup, and delete BuildRequires git

* Sat Jul 25 2020 yang_zhuang_zhuang<yangzhuangzhuang1@huawei.com> - 2.6.2-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update version to 2.6.2

* Fri Sep 27 2019 shenyangyang<shenyangyang4@huawei.com> - 2.3.3-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:modify license

* Tue Aug 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3.3-4
- Package init
