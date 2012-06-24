Summary:     	Cleans up files in directories based on their age
Summary(de): 	Entfernt Dateien eines bestimmten Alters aus Verzeichnissen
Summary(fr): 	Nettoie les fichiers dans les r�pertoires en fonction de leur age
Summary(pl): 	Kasuje pliki w podtstawowych katalogach (tmp)
Name:        	tmpwatch
Version:     	1.7
Release:     	4
Source:      	%{name}-%{version}.tar.gz
Patch:		tmpwatch-Makefile.patch
Copyright:   	GPL
Group:      	Utilities/System
Group(pl):	Narz�dzia/System
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This package provides a program that can be used to clean out directories. It
recursively searches the directory (ignoring symlinks) and removes files that
haven't been accessed in a user-specified amount of time.

%description -l de
Dieses Paket enth�lt ein Programm zum Aufr�umen von Verzeichnissen. Es 
durchsucht das Verzeichnis (Symlinks werden ignoriert) rekursiv und entfernt 
Dateien, auf die in der vom Benutzer definierten Zeit nicht zugegriffen 
wurde.

%description -l fr
Ce paquetage offre un programme permettant de nettoyer les r�pertoires. Il
recherche r�cursivement dans le r�pertoire (en ignorant les liens symboliques)
et supprime les fichiers qui n'ont pas �t� acc�d�s depuis une p�riode donn�e.

%description -l pl
W pakiecie znajduje si� program, kt�ry czy�ci katalogi tmp ze starych plik�w.

%description -l tr
Bu paket, dizinleri temizleyen bir program i�erir. Simgesel ba�lar� g�z�n�ne
almadan dizinleri rek�rsif olarak arar ve kullan�c�n�n �nceden belirledi�i
bir s�rede eri�ilmemi� olanlar� siler.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/cron.daily

make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	sbindir="%{_sbindir}" \
	mandir="%{_mandir}"
	
echo '%{_sbindir}/tmpwatch 240 /tmp /var/cache/man/{cat?,X11R6/cat?,local/cat?,pl/cat?}' \
	> $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tmpwatch
%attr(750,root,root) %config %verify(not size mtime md5) /etc/cron.daily/*
%{_mandir}/man8/*

%changelog
* Thu May 20 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.7-2]
- rebuild in new evn.
- based on RH spec
- pl translation by Wojtek �lusarczyk <wojtek@shadow.eu.org>
- start at RH spec file.
