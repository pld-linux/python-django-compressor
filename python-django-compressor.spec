#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		pypi_name	django_compressor
%define 	module	django-compressor
Summary:	Compresses linked and inline JavaScript or CSS into single cached files
Name:		python-%{module}
Version:	2.0
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	98254da44f1676d7b871ffeb14115175
URL:		http://pypi.python.org/pypi/django_compressor/2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-django
Requires:	python-django-appconf >= 0.4
Requires:	python-rcssmin
Requires:	python-rjsmin
Requires:	python-versiontools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files.

%package -n python3-django-compressor
Summary:	Compresses linked and inline JavaScript or CSS into single cached files
Group:		Libraries/Python
Requires:	python3-django
Requires:	python3-django-appconf
Requires:	python3-rcssmin
Requires:	python3-rjsmin
Requires:	python3-versiontools

%description -n python3-django-compressor
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/compressor
%{py_sitescriptdir}/%{pypi_name}-%{version}-py*.egg-info

%if %{with python3}
%files -n python3-django-compressor
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/compressor
%{py3_sitescriptdir}/%{pypi_name}-%{version}-py*.egg-info
%endif