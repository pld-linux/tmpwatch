Summary:	A utility for removing files based on when they were last accessed
Summary(de):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(fr):	Nettoie les fichiers dans les rИpertoires en fonction de leur age
Summary(pl):	NarzЙdzie kasuj╠ce pliki w oparciu o czas ostatniego dostЙpu
Summary(ru):	Утилита удаления файлов по критерию давности последнего доступа
Summary(uk):	Утил╕та видалення файл╕в за критер╕╓м давност╕ останнього доступу
Name:		tmpwatch
Version:	2.8.2
Release:	2
License:	GPL
Group:		Applications/System
# ftp://ftp.redhat.com/pub/redhat/linux/rawhide/SRPMS/SRPMS/
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
aufzurДumen, in denen temporДre Dateien gelagert werden (z.B. /tmp).
Tmpwatch ignoriert symlinks, wechselt kein Filesystem und entfernt nur
normale Dateien und leere Verzeichnisse.

%description -l fr
Ce paquetage offre un programme permettant de nettoyer les
rИpertoires. Il recherche rИcursivement dans le rИpertoire (en
ignorant les liens symboliques) et supprime les fichiers qui n'ont pas
ИtИ accИdИs depuis une pИriode donnИe.

%description -l pl
W pakiecie znajduje siЙ program, ktСry czy╤ci katalogi tmp oraz catman
z plikСw nie odczytywanych przez okre╤lony czas.

%description -l tr
Bu paket, dizinleri temizleyen bir program iГerir. Simgesel baПlarЩ
gЖzЖnЭne almadan dizinleri rekЭrsif olarak arar ve kullanЩcЩnЩn
Жnceden belirlediПi bir sЭrede eriЧilmemiЧ olanlarЩ siler.

%description -l ru
Утилита tmpwatch рекурсивно удаляет в указанных каталогах файлы, к
которым не было доступа указанное время. Обычно используется для
очистки каталогов, хранящих временные файлы (например, /tmp). Эта
утилита игнорирует симлинки, не переходит на другие файловые системы и
удаляет только пустые каталоги и обычные (не специальные) файлы.

%description -l uk
Утил╕та tmpwatch рекурсивно видаля╓ у вказаних каталогах файли, до
яких не було доступу вказаний час. Звичайно використову╓ться для
очистки каталог╕в, що збер╕гають тимчасов╕ файли (наприклад, /tmp). Ця
утил╕та ╕гнору╓ симл╕нки, не переходить на ╕нш╕ файлов╕ системи ╕
видаля╓ т╕льки порожн╕ каталоги та звичайн╕ (не спец╕альн╕) файли.

%prep
%setup -q
%patch0 -p1

%build
aclocal
%{__autoconf}
%{__automake}
%{__libtoolize}
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
