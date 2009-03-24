# TODO:
# - move whole amavis-related stuff to it's own spec. trigger is needed...
#
Summary:	A utility for removing files based on when they were last accessed
Summary(de.UTF-8):	Utility zum Entfernen von Dateien, basierend auf ihrer Zugriffszeit
Summary(es.UTF-8):	Limpia archivos en directorios basado en sus edades
Summary(fr.UTF-8):	Nettoie les fichiers dans les répertoires en fonction de leur age
Summary(pl.UTF-8):	Narzędzie kasujące pliki w oparciu o czas ostatniego dostępu
Summary(pt_BR.UTF-8):	Limpa arquivos em diretórios baseado em suas idades
Summary(ru.UTF-8):	Утилита удаления файлов по критерию давности последнего доступа
Summary(uk.UTF-8):	Утиліта видалення файлів за критерієм давності останнього доступу
Name:		tmpwatch
Version:	2.9.14
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/t/m/tmpwatch/%{name}-%{version}.tar.bz2
# Source0-md5:	9d77f5f4a1bb93fec08b17d53fef6d4f
Source1:	%{name}.sysconfig
Source2:	%{name}.cron
Source3:	%{name}.conf
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-fuser.patch
URL:		https://fedorahosted.org/tmpwatch/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tmpwatch utility recursively searches through specified
directories and removes files which have not been accessed in a
specified period of time. tmpwatch is normally used to clean up
directories which are used for temporarily holding files (for example,
/tmp). tmpwatch ignores symlinks, won't switch filesystems and only
removes empty directories and regular files.

%description -l de.UTF-8
Das tmpwatch-Utility sucht rekursiv durch angegebene Verzeichnisse und
entfernt Dateien, die in einer angegebenen Zeitspanne nicht benutzt
wurden. Tmpwatch wird normalerweise benutzt, um Verzeichnisse
aufzuräumen, in denen temporäre Dateien gelagert werden (z.B. /tmp).
Tmpwatch ignoriert symlinks, wechselt kein Filesystem und entfernt nur
normale Dateien und leere Verzeichnisse.

%description -l es.UTF-8
Este paquete nos ofrece un programa que puede ser usado para limpiar
directorios. Periódicamente remueve el directorio (ignorando symlinks)
y elimina archivos que no fueron accedidos en un tiempo especificado
por el usuario.

%description -l fr.UTF-8
Ce paquetage offre un programme permettant de nettoyer les
répertoires. Il recherche récursivement dans le répertoire (en
ignorant les liens symboliques) et supprime les fichiers qui n'ont pas
été accédés depuis une période donnée.

%description -l pl.UTF-8
tmpwatch rekursywnie przeszukuje wyspecyfikowane katalogi szukając
plików, które nie były używane przez określony okres czasu, w celu ich
usunięcia. Jest on zazwyczaj używany do czyszczenia katalogów w
których przechowywane są pliki tymczasowe (na przykład /tmp). tmpwatch
ignoruje symlinki, nie zmienia systemu plików podczas przeszukiwania
katalogów, usuwa tylko puste katalogi i zwyczajne pliki.

%description -l pt_BR.UTF-8
Este pacote oferece um programa que pode ser usado para limpar
diretórios. Ele periodicamente vasculha o diretório (ignorando
symlinks) e remove arquivos que não foram acessados em um tempo
especificado pelo usuário.

%description -l tr.UTF-8
Bu paket, dizinleri temizleyen bir program içerir. Simgesel bağları
gözönüne almadan dizinleri rekürsif olarak arar ve kullanıcının
önceden belirlediği bir sürede erişilmemiş olanları siler.

%description -l ru.UTF-8
Утилита tmpwatch рекурсивно удаляет в указанных каталогах файлы, к
которым не было доступа указанное время. Обычно используется для
очистки каталогов, хранящих временные файлы (например, /tmp). Эта
утилита игнорирует симлинки, не переходит на другие файловые системы и
удаляет только пустые каталоги и обычные (не специальные) файлы.

%description -l uk.UTF-8
Утиліта tmpwatch рекурсивно видаляє у вказаних каталогах файли, до
яких не було доступу вказаний час. Звичайно використовується для
очистки каталогів, що зберігають тимчасові файли (наприклад, /tmp). Ця
утиліта ігнорує симлінки, не переходить на інші файлові системи і
видаляє тільки порожні каталоги та звичайні (не спеціальні) файли.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{cron.daily,sysconfig,%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT/etc/cron.daily/%{name} <<'EOF'
#!/bin/sh
# Some defaults:
AMAVIS_QUARANTINE="1440"
OPTIONS="-fq"
if [ -f /etc/sysconfig/tmpwatch ]; then
	. /etc/sysconfig/tmpwatch
fi

%{_sbindir}/tmpwatch ${OPTIONS} -x /tmp/.X11-unix -x /tmp/.XIM-unix -x /tmp/.font-unix \
-x /tmp/.ICE-unix -x /tmp/.Test-unix -x /tmp/.s.PGSQL.\* 240 /tmp

# Cleanup amavis quarantine:
if [ -d /var/spool/amavis/virusmails ]; then
	if [ ${AMAVIS_QUARANTINE} -ne 0 ]; then
		%{_sbindir}/tmpwatch ${OPTIONS} ${AMAVIS_QUARANTINE} /var/spool/amavis/virusmails
	fi
fi
EOF

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sbindir}/%{name}.cron
install %{SOURCE3} $RPM_BUILD_ROOT/etc/tmpwatch/common.conf

ln -s %{_sbindir}/%{name}.cron $RPM_BUILD_ROOT/etc/cron.daily/%{name}.directories

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 2.9.1-4
if [ -f /usr/sbin/amavisd ]; then
	echo "WARNING!! Take a look at /etc/sysconfig/%{name}"
	echo "That version has enabled amavis-spool cleaning"
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/tmpwatch
%attr(755,root,root) %{_sbindir}/tmpwatch.cron
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/tmpwatch/*.conf
%attr(750,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) /etc/cron.daily/tmpwatch
%attr(750,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) /etc/cron.daily/tmpwatch.directories
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/tmpwatch
%{_mandir}/man8/tmpwatch.8*
