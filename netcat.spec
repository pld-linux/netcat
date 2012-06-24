Summary:	Versatile network test and debugging tool
Summary(es):	Herramienta de prueba e depuraci�n para servicios de red
Summary(pl):	Proste narz�dzie do testowania sieci
Summary(pt_BR):	Ferramenta de teste e depura��o para servi�os de rede
Name:		netcat
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/netcat/netcat-%{version}.tar.bz2
# Source0-md5:	0a29eff1736ddb5effd0b1ec1f6fe0ef
URL:		http://netcat.sourceforge.net/
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

%description -l es
NetCat es un cliente de red m�nimo. Puede ser usado para crear
conexiones TCP a puertos arbitrarios y puede simular conexiones
sobre UDP. Tambi�n puede o�r puertos.

%description -l pl
Netcat to proste uniksowe narz�dzie, kt�re odbiera i wysy�a dane
poprzez po��czenia sieciowe protoko�ami TCP lub UDP. Jest
zaprojektowane jako wiarygodny "back-end", kt�ry mo�e by� u�ywany
bezpo�rednio albo sterowany przez inne programy i skrypty.
Jednocze�nie mo�e pom�c w wykrywaniu usterek w sieci albo poznawaniu
jej od �rodka, poniewa� mo�e stworzy� prawie dowolny rodzaj
po��czenia, jaki mo�e by� potrzebny, i ma wbudowanych kilka ciekawych
funkcji. Netcat - albo "nc", jak si� nazywa w�a�ciwy program, powinien
by� by� dostarczany ju� dawno temu jako kolejne tajemnicze, ale
standardowe uniksowe narz�dzie.

%description -l pt_BR
O NetCat � um cliente de rede m�nimo. Pode ser usado para criar
conex�es TCP para portas arbitr�rias e pode simular conex�es sobre
UDP. Tamb�m pode receber conex�es.

%prep
%setup -q

%build
%{__intltoolize}
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang netcat

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Change* NEWS README TODO 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
