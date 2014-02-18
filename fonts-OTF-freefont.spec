Summary:	Free UCS scalable fonts in OpenType format
Summary(pl.UTF-8):	Wolnodostępne skalowalne fonty UCS w formacie OpenType
Name:		fonts-OTF-freefont
Version:	20120503
Release:	3
License:	GPL v2
Group:		Fonts
Source0:	http://ftp.gnu.org/gnu/freefont/freefont-otf-%{version}.tar.gz
# Source0-md5:	e23c149a4cc494ac1f473f13cca16b67
Source1:	%{name}-mono.conf
Source2:	%{name}-sans.conf
Source3:	%{name}-serif.conf
URL:		http://www.gnu.org/software/freefont/
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
install -d $RPM_BUILD_ROOT{%{otffontsdir},%{_sysconfdir}/fonts/conf.d,%{_datadir}/fontconfig/conf.avail}

cp -p *.otf $RPM_BUILD_ROOT%{otffontsdir}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/69-freefont-otf-mono.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/69-freefont-otf-sans.conf
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/69-freefont-otf-serif.conf

ln -s %{_datadir}/fontconfig/conf.avail/69-freefont-otf-mono.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/69-freefont-otf-sans.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/69-freefont-otf-serif.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

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
%{_datadir}/fontconfig/conf.avail/69-freefont-otf-*.conf
%{_sysconfdir}/fonts/conf.d/69-freefont-otf-*.conf
