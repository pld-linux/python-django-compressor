#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		pypi_name	django_compressor
%define 	module	django-compressor
Summary:	Compresses linked and inline JavaScript or CSS into single cached files
Name:		python-%{module}
Version:	2.1.1
Release:	8
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	5e74141076b70272149ed07e6ce0ea56
URL:		http://django-compressor.readthedocs.io/
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Django Compressor combines and compresses linked and inline JavaScript
or CSS in a Django templates into cacheable static files.

%package -n python3-django-compressor
Summary:	Compresses linked and inline JavaScript or CSS into single cached files
Group:		Libraries/Python

%description -n python3-django-compressor
Django Compressor combines and compresses linked and inline JavaScript
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
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/compressor/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/compressor/test_*.py*
%py_postclean
%endif

%if %{with python3}
%py3_install
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/compressor/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/compressor/__pycache__/test_*.pyc
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/compressor/test_*.py
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
