Summary:     	Cleans up files in directories based on their age
Summary(de): 	Entfernt Dateien eines bestimmten Alters aus Verzeichnissen
Summary(fr): 	Nettoie les fichiers dans les répertoires en fonction de leur age
Summary(pl): 	Kasuje pliki w podtstawowych katalogach (tmp)
Name:        	tmpwatch
Version:     	1.7
Release:     	2
Source:      	%{name}-%{version}.tar.gz
Patch:		tmpwatch-Makefile.patch
Copyright:   	GPL
Group:      	Utilities/System
Group(pl):	Narzêdzia/System
Buildroot:   	/tmp/%{name}-%{version}-root

%description
This package provides a program that can be used to clean out directories. It
recursively searches the directory (ignoring symlinks) and removes files that
haven't been accessed in a user-specified amount of time.

%description -l de
Dieses Paket enthält ein Programm zum Aufräumen von Verzeichnissen. Es 
durchsucht das Verzeichnis (Symlinks werden ignoriert) rekursiv und entfernt 
Dateien, auf die in der vom Benutzer definierten Zeit nicht zugegriffen 
wurde.

%description -l fr
Ce paquetage offre un programme permettant de nettoyer les répertoires. Il
recherche récursivement dans le répertoire (en ignorant les liens symboliques)
et supprime les fichiers qui n'ont pas été accédés depuis une période donnée.

%description -l pl
W pakiecie znajduje siê program, który czy¶ci katalogi tmp ze starych plików.

%description -l tr
Bu paket, dizinleri temizleyen bir program içerir. Simgesel baðlarý gözönüne
almadan dizinleri rekürsif olarak arar ve kullanýcýnýn önceden belirlediði
bir sürede eriþilmemiþ olanlarý siler.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{cron.daily,profile.d}

make PREFIX=$RPM_BUILD_ROOT install
echo '/usr/sbin/tmpwatch 240 /tmp /var/cache/man/cat?' \
	> $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch

echo '/usr/sbin/tmpwatch 240 ~/tmp' >$RPM_BUILD_ROOT/etc/profile.d/tmpwatch.sh
ln -sf tmpwatch.sh $RPM_BUILD_ROOT/etc/profile.d/tmpwatch.csh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/sbin/tmpwatch
%attr(750,root,root) %config %verify(not size mtime md5) /etc/cron.daily/*
%attr(755,root,root) /etc/profile.d/*
/usr/man/man8/*

%changelog
* Thu Apr 22 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.5.1-4]
- fixed %attr (now users allow to run tmpwatch)
- added /etc/profile.d/tmpwatch.{sh,csh}
- compiled on rpm 3

* Thu Nov 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.1-3]
- changed permission on tmpwatch to 750.

* Fri Jun 12 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation.

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- make /etc/cron.daily/tmpwatch executable

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- version 1.5
- fixed flags passing
- cleaned up message()

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added man page to package
- uses a buildroot and %attr
- fixed error message generation for directories
- fixed flag propagation

* Mon Mar 24 1997 Erik Troan <ewt@redhat.com>
- Don't follow symlinks which are specified on the command line
- Added a man page

* Sun Mar 09 1997 Erik Troan <ewt@redhat.com>
Rebuilt to get right permissions on the Alpha (though I have no idea
how they ended up wrong).
