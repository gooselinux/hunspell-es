Name: hunspell-es
Summary: Spanish hunspell dictionaries
%define upstreamid 20081215
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://es.openoffice.org/files/documents/73/3001/es_ANY.zip
Group: Applications/Text
URL: http://es.openoffice.org/programa/diccionario.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv3+ or GPLv3+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Spanish (Spain, Mexico, etc.) hunspell dictionaries.

%prep
%setup -q -c -n hunspell-es

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p es_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/es_ES.dic
cp -p es_ANY.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/es_ES.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
es_ES_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"

for lang in $es_ES_aliases; do
	ln -s es_ES.aff $lang.aff
	ln -s es_ES.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt Changelog.txt GPLv3.txt MPL-1.1.txt LGPLv3.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20081215-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081215-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081215-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081215-1
- latest version

* Mon Sep 29 2008 Caolan McNamara <caolanm@redhat.com> - 0.20051031-3
- add es_CU as Cuba for OOo

* Tue Jul 08 2008 Caolan McNamara <caolanm@redhat.com> - 0.20051031-2
- add es_US

* Mon Aug 20 2007 Caolan McNamara <caolanm@redhat.com> - 0.20051031-1
- latest version
- clarify license version

* Thu Aug 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20050510-2
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20050510-1
- initial version
