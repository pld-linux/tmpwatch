Summary:	A utility for removing files based on when they were last accessed
Summary(de):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(fr):	Nettoie les fichiers dans les répertoires en fonction de leur age
Summary(pl):	Narzêdzie kasuj±ce pliki w oparciu o czas ostatniego dostêpu
Name:		tmpwatch
Version:	2.6.1
Release:	3
License:	GPL
Group:		Applications/System
Group(pl):	Aplikacje/System
Group(de):	Applikationen/System
Source0:	%{name}-%{version}.tar.gz
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
aufzuräumen, in denen temporäre Dateien gelagert werden (z.B. /tmp).
Tmpwatch ignoriert symlinks, wechselt kein Filesystem und entfernt nur
normale Dateien und leere Verzeichnisse.

%description -l fr
Ce paquetage offre un programme permettant de nettoyer les
répertoires. Il recherche récursivement dans le répertoire (en
ignorant les liens symboliques) et supprime les fichiers qui n'ont pas
été accédés depuis une période donnée.

%description -l pl
W pakiecie znajduje siê program, który czy¶ci katalogi tmp oraz catman
z plików nie odczytywanych przez okre¶lony czas.

%description -l tr
Bu paket, dizinleri temizleyen bir program içerir. Simgesel baðlarý
gözönüne almadan dizinleri rekürsif olarak arar ve kullanýcýnýn
önceden belirlediði bir sürede eriþilmemiþ olanlarý siler.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
libtoolize --copy --force
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
