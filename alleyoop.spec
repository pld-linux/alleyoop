Summary:	Graphical Valgrind front-end
Name:		alleyoop
Version:	0.7.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sf.net/alleyoop/%{name}-%{version}.tar.gz
# Source0-md5:	df7bc031ab4925ba3bdf6a6ad4447d58
URL:		http://alleyoop.sourceforge.net/
BuildRequires:	binutils-static
BuildRequires:	valgrind
BuildRequires:	GConf2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libglade2-devel
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alleyoop is a graphical front-end to the increasingly popular Valgrind
memory checker for x86 GNU/ Linux using the Gtk+ widget set and other
GNOME libraries for the X-Windows environment.

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
