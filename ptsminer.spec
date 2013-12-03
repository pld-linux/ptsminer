%define	snap	20131203
Summary:	Protoshares Pool Miner
Name:		ptsminer
Version:	0.1
Release:	0.%{snap}.1
License:	GPL v2
Group:		Applications/Networking
URL:		https://github.com/thbaumbach/ptsminer
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	72eec7618cf33166a598c7c6f835c763
BuildRequires:	boost-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	yasm >= 1.1.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a miner for Bitcoin.

%prep
%setup -q -n %{name}

%build
%{__make} -C src -f makefile.unix

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install src/ptsminer $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
