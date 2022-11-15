Name:		python-yamllint
Version:	1.28.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/y/yamllint/yamllint-%{version}.tar.gz
Summary:	A linter for YAML files.
URL:		https://pypi.org/project/yamllint/
License:	GPLv3
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A linter for YAML files.

%prep
%autosetup -p1 -n yamllint-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/yamllint
%{py_sitedir}/yamllint
%{py_sitedir}/yamllint-*.*-info
