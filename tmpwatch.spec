Summary:	A utility for removing files based on when they were last accessed
Summary(de):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(es):	Limpia archivos en directorios basado en sus edades
Summary(fr):	Nettoie les fichiers dans les r�pertoires en fonction de leur age
Summary(pl):	Narz�dzie kasuj�ce pliki w oparciu o czas ostatniego dost�pu
Summary(pt_BR):	Limpa arquivos em diret�rios baseado em suas idades
Summary(ru):	������� �������� ������ �� �������� �������� ���������� �������
Summary(uk):	���̦�� ��������� ���̦� �� �����Ҧ�� ������Ԧ ���������� �������
Name:		tmpwatch
Version:	2.8.4
Release:	5
License:	GPL
Group:		Applications/System
# ftp://ftp.redhat.com/pub/redhat/linux/rawhide/SRPMS/SRPMS/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5: 3fda94d7b052f83006e542c2e57b322b
Patch0:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tmpwatch utility recursively searches through specified
directories and removes files which have not been accessed in a
specified period of time. Tmpwatch is normally used to clean up
directories which are used for temporarily holding files (for example,
/tmp). Tmpwatch ignores symlinks, won't switch filesystems and only
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
W pakiecie znajduje si� program, kt�ry czy�ci katalogi tmp oraz catman
z plik�w nie odczytywanych przez okre�lony czas.

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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/cron.daily

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '%{_sbindir}/tmpwatch 240 /tmp /var/cache/man/{,*,X11R6,X11R6/*,local,local/*}/cat?' \
	> $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch
echo '%{_sbindir}/tmpwatch 720 /var/tmp' >> $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tmpwatch
%attr(750,root,root) %config %verify(not size mtime md5) /etc/cron.daily/*
%{_mandir}/man8/*
