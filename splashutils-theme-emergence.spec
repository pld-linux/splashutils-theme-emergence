
%define		theme	emergence

Summary:	Splashutils - emergence theme
Summary(pl):	Splashutils - motyw emergence
Name:		splashutils-theme-%{theme}
Version:	1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://dev.gentoo.org/~spock/projects/gensplash/current/fbsplash-theme-emergence-r1.tar.bz2
# Source0-md5:	c6afab93416bc4c8fe8bc328d4e432a0
Requires:	splashutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gentoo emergence theme for splashutils.

%description -l pl
Motyw gentoo emergence do splashutils.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/splash/%{theme}

install -d $THEME_DIR/images
install %{theme}/*.cfg $THEME_DIR
install %{theme}/images/* $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/splash/%{theme}
