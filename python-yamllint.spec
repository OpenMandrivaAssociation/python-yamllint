%define module yamllint

Name:		python-yamllint
Version:	1.37.1
Release:	1
Summary:	A linter for YAML files.
License:	GPLv3
Group:		Development/Python
URL:		https://pypi.org/project/yamllint/
Source0:	https://files.pythonhosted.org/packages/source/y/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
A linter for YAML files.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
