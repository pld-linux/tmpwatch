Summary:	A utility for removing files based on when they were last accessed
Summary(de):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(es):	Limpia archivos en directorios basado en sus edades
Summary(fr):	Nettoie les fichiers dans les répertoires en fonction de leur age
Summary(pl):	Narzêdzie kasuj±ce pliki w oparciu o czas ostatniego dostêpu
Summary(pt_BR):	Limpa arquivos em diretórios baseado em suas idades
Summary(ru):	õÔÉÌÉÔÁ ÕÄÁÌÅÎÉÑ ÆÁÊÌÏ× ÐÏ ËÒÉÔÅÒÉÀ ÄÁ×ÎÏÓÔÉ ÐÏÓÌÅÄÎÅÇÏ ÄÏÓÔÕÐÁ
Summary(uk):	õÔÉÌ¦ÔÁ ×ÉÄÁÌÅÎÎÑ ÆÁÊÌ¦× ÚÁ ËÒÉÔÅÒ¦¤Í ÄÁ×ÎÏÓÔ¦ ÏÓÔÁÎÎØÏÇÏ ÄÏÓÔÕÐÕ
Name:		tmpwatch
Version:	2.9.1
Release:	4
License:	GPL
Group:		Applications/System
# New versions are taken from:
# ftp://download.fedora.redhat.com/pub/fedora/linux/core/development/SRPMS/
Source0:	http://piorun.ds.pg.gda.pl/~blues/SOURCES/%{name}-%{version}.tar.gz
# Source0-md5:	0780803e5ab13cb6b5858b5ed6dca9f5
Source1:	%{name}.sysconfig
Patch0:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tmpwatch utility recursively searches through specified
directories and removes files which have not been accessed in a
specified period of time. tmpwatch is normally used to clean up
directories which are used for temporarily holding files (for example,
/tmp). tmpwatch ignores symlinks, won't switch filesystems and only
removes empty directories and regular files.

%description -l de
Das tmpwatch-Utility sucht rekursiv durch angegebene Verzeichnisse und
entfernt Dateien, die in einer angegebenen Zeitspanne nicht benutzt
wurden. Tmpwatch wird normalerweise benutzt, um Verzeichnisse
aufzuräumen, in denen temporäre Dateien gelagert werden (z.B. /tmp).
Tmpwatch ignoriert symlinks, wechselt kein Filesystem und entfernt nur
normale Dateien und leere Verzeichnisse.

%description -l es
Este paquete nos ofrece un programa que puede ser usado para limpiar
directorios. Periódicamente remueve el directorio (ignorando symlinks)
y elimina archivos que no fueron accedidos en un tiempo especificado
por el usuario.

%description -l fr
Ce paquetage offre un programme permettant de nettoyer les
répertoires. Il recherche récursivement dans le répertoire (en
ignorant les liens symboliques) et supprime les fichiers qui n'ont pas
été accédés depuis une période donnée.

%description -l pl
tmpwatch rekursywnie przeszukuje wyspecyfikowane katalogi szukaj±c
plików, które nie by³y u¿ywane przez okre¶lony okres czasu, w celu
ich usuniêcia. Jest on zazwyczaj u¿ywany do czyszczenia katalogów
w których przechowywane s± pliki tymczasowe (na przyk³ad /tmp).
tmpwatch ignoruje symlinki, nie zmienia systemu plików podczas
przeszukiwania katalogów, usuwa tylko puste katalogi i zwyczajne
pliki.

%description -l pt_BR
Este pacote oferece um programa que pode ser usado para limpar
diretórios. Ele periodicamente vasculha o diretório (ignorando
symlinks) e remove arquivos que não foram acessados em um tempo
especificado pelo usuário.

%description -l tr
Bu paket, dizinleri temizleyen bir program içerir. Simgesel baðlarý
gözönüne almadan dizinleri rekürsif olarak arar ve kullanýcýnýn
önceden belirlediði bir sürede eriþilmemiþ olanlarý siler.

%description -l ru
õÔÉÌÉÔÁ tmpwatch ÒÅËÕÒÓÉ×ÎÏ ÕÄÁÌÑÅÔ × ÕËÁÚÁÎÎÙÈ ËÁÔÁÌÏÇÁÈ ÆÁÊÌÙ, Ë
ËÏÔÏÒÙÍ ÎÅ ÂÙÌÏ ÄÏÓÔÕÐÁ ÕËÁÚÁÎÎÏÅ ×ÒÅÍÑ. ïÂÙÞÎÏ ÉÓÐÏÌØÚÕÅÔÓÑ ÄÌÑ
ÏÞÉÓÔËÉ ËÁÔÁÌÏÇÏ×, ÈÒÁÎÑÝÉÈ ×ÒÅÍÅÎÎÙÅ ÆÁÊÌÙ (ÎÁÐÒÉÍÅÒ, /tmp). üÔÁ
ÕÔÉÌÉÔÁ ÉÇÎÏÒÉÒÕÅÔ ÓÉÍÌÉÎËÉ, ÎÅ ÐÅÒÅÈÏÄÉÔ ÎÁ ÄÒÕÇÉÅ ÆÁÊÌÏ×ÙÅ ÓÉÓÔÅÍÙ É
ÕÄÁÌÑÅÔ ÔÏÌØËÏ ÐÕÓÔÙÅ ËÁÔÁÌÏÇÉ É ÏÂÙÞÎÙÅ (ÎÅ ÓÐÅÃÉÁÌØÎÙÅ) ÆÁÊÌÙ.

%description -l uk
õÔÉÌ¦ÔÁ tmpwatch ÒÅËÕÒÓÉ×ÎÏ ×ÉÄÁÌÑ¤ Õ ×ËÁÚÁÎÉÈ ËÁÔÁÌÏÇÁÈ ÆÁÊÌÉ, ÄÏ
ÑËÉÈ ÎÅ ÂÕÌÏ ÄÏÓÔÕÐÕ ×ËÁÚÁÎÉÊ ÞÁÓ. ú×ÉÞÁÊÎÏ ×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ÄÌÑ
ÏÞÉÓÔËÉ ËÁÔÁÌÏÇ¦×, ÝÏ ÚÂÅÒ¦ÇÁÀÔØ ÔÉÍÞÁÓÏ×¦ ÆÁÊÌÉ (ÎÁÐÒÉËÌÁÄ, /tmp). ãÑ
ÕÔÉÌ¦ÔÁ ¦ÇÎÏÒÕ¤ ÓÉÍÌ¦ÎËÉ, ÎÅ ÐÅÒÅÈÏÄÉÔØ ÎÁ ¦ÎÛ¦ ÆÁÊÌÏ×¦ ÓÉÓÔÅÍÉ ¦
×ÉÄÁÌÑ¤ Ô¦ÌØËÉ ÐÏÒÏÖÎ¦ ËÁÔÁÌÏÇÉ ÔÁ Ú×ÉÞÁÊÎ¦ (ÎÅ ÓÐÅÃ¦ÁÌØÎ¦) ÆÁÊÌÉ.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{cron.daily,sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch <<EOF
#!/bin/sh
# Some defaults:
AMAVIS_QUARANTINE="1440"
if [ -f /etc/sysconfig/tmpwatch ]; then
	. /etc/sysconfig/tmpwatch
fi

%{_sbindir}/tmpwatch -x /tmp/.X11-unix -x /tmp/.XIM-unix -x /tmp/.font-unix \
-x /tmp/.ICE-unix -x /tmp/.Test-unix 240 /tmp
if [ -d /var/cache/man ]; then
	%{_sbindir}/tmpwatch -f 240 /var/cache/man/{,*,X11R6,X11R6/*,local,local/*}/cat? 
fi
%{_sbindir}/tmpwatch 720 /var/tmp
# Cleanup temporary files for php:
if [ -d /var/run/php ]; then
	%{_sbindir}/tmpwatch 720 /var/run/php
fi
# Cleanup amavis quarantine:
if [ -d /var/spool/amavis/virusmails ]; then
	if [ ${AMAVIS_QUARANTINE} -ne 0 ]; then
		%{_sbindir}/tmpwatch ${AMAVIS_QUARANTINE} /var/spool/amavis/virusmails
	fi
fi
EOF

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 2.9.1-4
if [ -f /usr/sbin/amavisd ]; then
	echo "WARNING!! Take a look at /etc/sysconfig/%{name}"
	echo "That version has enabled amavis-spool cleaning"
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tmpwatch
%attr(750,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.daily/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/%{name}
%{_mandir}/man8/*
