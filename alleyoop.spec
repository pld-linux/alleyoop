Summary:	Graphical Valgrind front-end
Summary(pl):	Graficzny frontend do Valgrinda
Name:		alleyoop
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sf.net/alleyoop/%{name}-%{version}.tar.gz
# Source0-md5:	4be84f90a2d69fb55a276698dafb24a1
URL:		http://alleyoop.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	binutils-static
BuildRequires:	libgnomeui-devel
BuildRequires:	libglade2-devel
BuildRequires:	valgrind
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alleyoop is a graphical front-end to the increasingly popular Valgrind
memory checker for x86 Linux using the Gtk+ widget set and other GNOME
libraries for the X Window environment.

%description -l pl
Alleyoop to graficzny frontend do Valgrinda - coraz bardziej
popularnego narzêdzia kontroluj±cego dostêp do pamiêci dla Linuksa
na x86. Alleyoop u¿ywa zestawu widgetów Gtk+ i innych bibliotek GNOME
w ¶rodowisku X Window.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
