%define module yamllint

Name:		python-yamllint
Version:	1.38.0
Release:	1
Summary:	A linter for YAML files.
License:	GPLv3
Group:		Development/Python
URL:		https://pypi.org/project/yamllint/
Source0:	https://files.pythonhosted.org/packages/source/y/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A linter for YAML files.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
