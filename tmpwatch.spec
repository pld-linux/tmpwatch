Summary:	A utility for removing files based on when they were last accessed
Summary(de):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(es):	Limpia archivos en directorios basado en sus edades
Summary(fr):	Nettoie les fichiers dans les répertoires en fonction de leur age
Summary(pl):	Narzêdzie kasuj±ce pliki w oparciu o czas ostatniego dostêpu
Summary(pt_BR):	Limpa arquivos em diretórios baseado em suas idades
Summary(ru):	õÔÉÌÉÔÁ ÕÄÁÌÅÎÉÑ ÆÁÊÌÏ× ÐÏ ËÒÉÔÅÒÉÀ ÄÁ×ÎÏÓÔÉ ÐÏÓÌÅÄÎÅÇÏ ÄÏÓÔÕÐÁ
Summary(uk):	õÔÉÌ¦ÔÁ ×ÉÄÁÌÅÎÎÑ ÆÁÊÌ¦× ÚÁ ËÒÉÔÅÒ¦¤Í ÄÁ×ÎÏÓÔ¦ ÏÓÔÁÎÎØÏÇÏ ÄÏÓÔÕÐÕ
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
W pakiecie znajduje siê program, który czy¶ci katalogi tmp oraz catman
z plików nie odczytywanych przez okre¶lony czas.

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
