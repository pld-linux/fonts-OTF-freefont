Summary:	Free UCS scalable fonts in OpenType format
Summary(pl.UTF-8):	Wolnodostępne skalowalne fonty UCS w formacie OpenType
Name:		fonts-OTF-freefont
Version:	20080912
Release:	1
License:	GPL v2
Group:		Fonts
Source0:	http://ftp.gnu.org/gnu/freefont/freefont-otf-%{version}.zip
# Source0-md5:	e584eea29d412192944f78c69f471a66
URL:		http://www.gnu.org/software/freefont/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		otffontsdir	%{_fontsdir}/OTF

%description
This project aims to provide a set of free scalable fonts covering the
ISO 10646/Unicode UCS (Universal Character Set).

%description -l pl.UTF-8
Celem tego projektu jest udostępnienie zestawu wolnodostępnych fontów
skalowalnych pokrywających zakres uniwersalnego zestawu znaków ISO
10646/Unicode.

%prep
%setup -q -n freefont-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{otffontsdir}

install *.otf $RPM_BUILD_ROOT%{otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README
%{otffontsdir}/FreeMono*.otf
%{otffontsdir}/FreeSans*.otf
%{otffontsdir}/FreeSerif*.otf
