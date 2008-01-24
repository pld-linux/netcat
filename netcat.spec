Summary:	Versatile network test and debugging tool
Summary(es.UTF-8):	Herramienta de prueba e depuración para servicios de red
Summary(pl.UTF-8):	Proste narzędzie do testowania sieci
Summary(pt_BR.UTF-8):	Ferramenta de teste e depuração para serviços de rede
Name:		netcat
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/netcat/netcat-%{version}.tar.bz2
# Source0-md5:	0a29eff1736ddb5effd0b1ec1f6fe0ef
URL:		http://netcat.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netcat is a simple Unix utility which reads and writes data across
network connections, using TCP or UDP protocol. It is designed to be a
reliable "back-end" tool that can be used directly or easily driven by
other programs and scripts. At the same time, it is a feature-rich
network debugging and exploration tool, since it can create almost any
kind of connection you would need and has several interesting built-in
capabilities. Netcat, or "nc" as the actual program is named, should
have been supplied long ago as another one of those cryptic but
standard Unix tools.

%description -l es.UTF-8
NetCat es un cliente de red mínimo. Puede ser usado para crear
conexiones TCP a puertos arbitrarios y puede simular conexiones
sobre UDP. También puede oír puertos.

%description -l pl.UTF-8
Netcat to proste uniksowe narzędzie, które odbiera i wysyła dane
poprzez połączenia sieciowe protokołami TCP lub UDP. Jest
zaprojektowane jako wiarygodny "back-end", który może być używany
bezpośrednio albo sterowany przez inne programy i skrypty.
Jednocześnie może pomóc w wykrywaniu usterek w sieci albo poznawaniu
jej od środka, ponieważ może stworzyć prawie dowolny rodzaj
połączenia, jaki może być potrzebny, i ma wbudowanych kilka ciekawych
funkcji. Netcat - albo "nc", jak się nazywa właściwy program, powinien
był być dostarczany już dawno temu jako kolejne tajemnicze, ale
standardowe uniksowe narzędzie.

%description -l pt_BR.UTF-8
O NetCat é um cliente de rede mínimo. Pode ser usado para criar
conexões TCP para portas arbitrárias e pode simular conexões sobre
UDP. Também pode receber conexões.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang netcat

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Change* NEWS README TODO 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
