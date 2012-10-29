Summary:	Free space simulation
Name:		celestia
Version:	1.6.1
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://heanet.dl.sourceforge.net/celestia/%{name}-%{version}.tar.gz
# Source0-md5:	02208982a431b984502fac909bf380f4
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gcc46.patch
Patch2:		%{name}-gcc47.patch
Patch3:		%{name}-libpng15.patch
Patch4:		%{name}-link.patch
BuildRequires:	gtkglext-devel
BuildRequires:	libtheora-devel
BuildRequires:	lua-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The free space simulation that lets you explore our universe
in three dimensions.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__automake}
%{__autoconf}
%configure \
	--with-gtk
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/celestia
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/extras
%{_datadir}/%{name}/extras-standard
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/models
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/shaders
%{_datadir}/%{name}/splash
%{_datadir}/%{name}/textures

%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/*.cfg
%{_datadir}/%{name}/*.png

%{_datadir}/%{name}/controls.txt
%{_datadir}/%{name}/demo.cel
%{_datadir}/%{name}/guide.cel
%{_datadir}/%{name}/start.cel

%lang(de) %{_datadir}/%{name}/controls_de.txt
%lang(de) %{_datadir}/%{name}/demo_de.cel
%lang(de) %{_datadir}/%{name}/guide_de.cel
%lang(de) %{_datadir}/%{name}/start_de.cel

%lang(pl) %{_datadir}/%{name}/controls_pl.txt
%lang(pl) %{_datadir}/%{name}/demo_pl.cel
%lang(pl) %{_datadir}/%{name}/guide_pl.cel
%lang(pl) %{_datadir}/%{name}/start_pl.cel

%{_desktopdir}/celestia.desktop
%{_pixmapsdir}/celestia.png

