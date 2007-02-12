Summary:	Graphical Valgrind front-end
Summary(pl.UTF-8):   Graficzny frontend do Valgrinda
Name:		alleyoop
Version:	0.8.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/alleyoop/%{name}-%{version}.tar.gz
# Source0-md5:	a5507573d190352e7c77dccf05dbb2ef
Patch0:		%{name}-locale-names.patch
URL:		http://alleyoop.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils-static
BuildRequires:	libgnomeui-devel
BuildRequires:	libglade2-devel
BuildRequires:	valgrind
Requires(post):	GConf2
Requires:		valgrind
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alleyoop is a graphical front-end to the increasingly popular Valgrind
memory checker for x86 Linux using the GTK+ widget set and other GNOME
libraries for the X Window environment.

%description -l pl.UTF-8
Alleyoop to graficzny frontend do Valgrinda - coraz bardziej
popularnego narzędzia kontrolującego dostęp do pamięci dla Linuksa
na x86. Alleyoop używa zestawu widgetów GTK+ i innych bibliotek GNOME
w środowisku X Window.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
