Summary:	A utility for removing files based on when they were last accessed
Summary(de):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(es):	Limpia archivos en directorios basado en sus edades
Summary(fr):	Nettoie les fichiers dans les r�pertoires en fonction de leur age
Summary(pl):	Narz�dzie kasuj�ce pliki w oparciu o czas ostatniego dost�pu
Summary(pt_BR):	Limpa arquivos em diret�rios baseado em suas idades
Summary(ru):	������� �������� ������ �� �������� �������� ���������� �������
Summary(uk):	���̦�� ��������� ���̦� �� �����Ҧ�� ������Ԧ ���������� �������
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
aufzur�umen, in denen tempor�re Dateien gelagert werden (z.B. /tmp).
Tmpwatch ignoriert symlinks, wechselt kein Filesystem und entfernt nur
normale Dateien und leere Verzeichnisse.

%description -l es
Este paquete nos ofrece un programa que puede ser usado para limpiar
directorios. Peri�dicamente remueve el directorio (ignorando symlinks)
y elimina archivos que no fueron accedidos en un tiempo especificado
por el usuario.

%description -l fr
Ce paquetage offre un programme permettant de nettoyer les
r�pertoires. Il recherche r�cursivement dans le r�pertoire (en
ignorant les liens symboliques) et supprime les fichiers qui n'ont pas
�t� acc�d�s depuis une p�riode donn�e.

%description -l pl
tmpwatch rekursywnie przeszukuje wyspecyfikowane katalogi szukaj�c
plik�w, kt�re nie by�y u�ywane przez okre�lony okres czasu, w celu
ich usuni�cia. Jest on zazwyczaj u�ywany do czyszczenia katalog�w
w kt�rych przechowywane s� pliki tymczasowe (na przyk�ad /tmp).
tmpwatch ignoruje symlinki, nie zmienia systemu plik�w podczas
przeszukiwania katalog�w, usuwa tylko puste katalogi i zwyczajne
pliki.

%description -l pt_BR
Este pacote oferece um programa que pode ser usado para limpar
diret�rios. Ele periodicamente vasculha o diret�rio (ignorando
symlinks) e remove arquivos que n�o foram acessados em um tempo
especificado pelo usu�rio.

%description -l tr
Bu paket, dizinleri temizleyen bir program i�erir. Simgesel ba�lar�
g�z�n�ne almadan dizinleri rek�rsif olarak arar ve kullan�c�n�n
�nceden belirledi�i bir s�rede eri�ilmemi� olanlar� siler.

%description -l ru
������� tmpwatch ���������� ������� � ��������� ��������� �����, �
������� �� ���� ������� ��������� �����. ������ ������������ ���
������� ���������, �������� ��������� ����� (��������, /tmp). ���
������� ���������� ��������, �� ��������� �� ������ �������� ������� �
������� ������ ������ �������� � ������� (�� �����������) �����.

%description -l uk
���̦�� tmpwatch ���������� �����Ѥ � �������� ��������� �����, ��
���� �� ���� ������� �������� ���. �������� ����������դ���� ���
������� ������Ǧ�, �� ���Ҧ����� �������צ ����� (���������, /tmp). ��
���̦�� �����դ ���̦���, �� ���������� �� ��ۦ �����צ ������� �
�����Ѥ Ԧ���� �����Φ �������� �� ������Φ (�� ���æ���Φ) �����.

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
