Summary:	A utility for removing files based on when they were last accessed
Summary(de):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(fr):	Nettoie les fichiers dans les r�pertoires en fonction de leur age
Summary(pl):	Narz�dzie kasuj�ce pliki w oparciu o czas ostatniego dost�pu
Name:		tmpwatch
Version:	2.2
Release:	2
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source:		%{name}-%{version}.tar.gz
Patch:		tmpwatch-Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tmpwatch utility recursively searches through specified directories and
removes files which have not been accessed in a specified period of time.
Tmpwatch is normally used to clean up directories which are used for
temporarily holding files (for example, /tmp). Tmpwatch ignores symlinks,
won't switch filesystems and only removes empty directories and regular
files.

%description -l de
Das tmpwatch-Utility sucht rekursiv durch angegebene Verzeichnisse und
entfernt Dateien, die in einer angegebenen Zeitspanne nicht benutzt wurden.
Tmpwatch wird normalerweise benutzt, um Verzeichnisse aufzur�umen, in
denen tempor�re Dateien gelagert werden (z.B. /tmp). Tmpwatch ignoriert
symlinks, wechselt kein Filesystem und entfernt nur normale Dateien und
leere Verzeichnisse.

%description -l fr
Ce paquetage offre un programme permettant de nettoyer les r�pertoires. Il
recherche r�cursivement dans le r�pertoire (en ignorant les liens
symboliques) et supprime les fichiers qui n'ont pas �t� acc�d�s depuis une
p�riode donn�e.

%description -l pl
W pakiecie znajduje si� program, kt�ry czy�ci katalogi tmp oraz catman z
plik�w nie odczytywanych przez okre�lony czas.

%description -l tr
Bu paket, dizinleri temizleyen bir program i�erir. Simgesel ba�lar�
g�z�n�ne almadan dizinleri rek�rsif olarak arar ve kullan�c�n�n �nceden
belirledi�i bir s�rede eri�ilmemi� olanlar� siler.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/cron.daily

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	sbindir="%{_sbindir}" \
	mandir="%{_mandir}"

echo '%{_sbindir}/tmpwatch 240 /tmp /var/cache/man/{,*,X11R6,X11R6/*,local,local/*}/cat?' \
	> $RPM_BUILD_ROOT/etc/cron.daily/tmpwatch

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tmpwatch
%attr(750,root,root) %config %verify(not size mtime md5) /etc/cron.daily/*
%{_mandir}/man8/*
