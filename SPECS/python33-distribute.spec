
%define pyver 33 
%define pybasever 3.3

%define __python /usr/bin/python%{pybasever}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}


%define real_name python-distribute

Name:           python%{pyver}-distribute
Version:        0.6.46
Release:        1.ius%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages
Vendor:         IUS Community Project 
Group:          Development/Languages
License:        PSFL/ZPL
URL:            http://bitbucket.org/tarek/distribute/wiki/Home 
Source0:        http://pypi.python.org/packages/source/d/distribute/distribute-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{pyver}, python%{pyver}-devel, python%{pyver}-tools
Requires:       python%{pyver}, python%{pyver}-devel
Provides:       python%{pyver}-setuptools


%description
Distribute is a fork of the Setuptools project. It is intended to replace 
Setuptools as the standard method for working with Python module distributions.

Setuptools was a collection of enhancements to the Python distutils that 
allowed you to more easily build and distribute Python packages.  It has since
been abandoned and there are no plans for supporting Python 3.


%prep
%setup -q -n distribute-%{version}

find -name '*.py' -print0 | xargs -0 sed -i '1s|^#!python|#!%{__python}|'


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} %{buildroot}%{_bindir}

%{__python} setup.py install -O1 --skip-build \
    --root $RPM_BUILD_ROOT \
    --single-version-externally-managed
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.exe' | xargs rm -f
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.txt' | xargs chmod -x

mv %{buildroot}%{_bindir}/easy_install %{buildroot}%{_bindir}/easy_install-%{pybasever}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc *.txt 
%{_bindir}/easy_install-%{pybasever}
%{python_sitelib}/distribute-%{version}-py%{pybasever}.egg-info
%{python_sitelib}/easy_install.py*
%{python_sitelib}/pkg_resources.py*
%{python_sitelib}/setuptools
%{python_sitelib}/setuptools-0.6c11-py%{pybasever}.egg-info
%{python_sitelib}/setuptools.pth
%{python_sitelib}/__pycache__/
%{python_sitelib}/_markerlib

%changelog
* Mon Jul 01 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.46-1.ius
- Latest sources from upstream

* Mon Jun 03 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.45-1.ius
- Latest sources from upstream

* Wed May 29 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.44-1.ius
- Latest sources from upstream

* Tue May 28 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.43-1.ius
- Latest sources from upstream
- remove %{python_sitelib}/site.py* from %files

* Tue May 14 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.40-1.ius
- Latest sources from upstream

* Mon May 13 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.39-1.ius
- Latest sources from upstream

* Mon May 06 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.38-1.ius
- Latest sources from upstream

* Mon Apr 08 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.36-1.ius
- Latest sources from upstream

* Thu Feb 28 2013 Ben Harper <ben.harper@rackspace.com> - 0.6.35-1.ius
- Latest sources from upstream

* Wed Jan 02 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.34-1.ius
- Latest sources from upstream

* Mon Dec 31 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.33-1.ius
- Latest sources from upstream

* Mon Oct 22 2012 Ben Harper <ben.harper@rackspace.com> - 0.6.30-1.ius
- Latest sources from upstream

* Tue Oct 16 2012 Ben Harper <ben.harper@rackspace.com> - 0.6.28-1.ius
- Porting from python32-distribute

* Mon Jul 23 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 0.6.28-1.ius
- New package for python32
