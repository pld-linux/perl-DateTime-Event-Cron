#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DateTime
%define	pnam	Event-Cron
Summary:	DateTime::Event::Cron - DateTime extension for generating recurrence sets from crontabs
Summary(pl.UTF-8):	DateTime::Event::Cron - rozszerzenie DateTime do generowania zbiorów powtarzalności z crontabów
Name:		perl-DateTime-Event-Cron
Version:	0.07
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Date/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee2867ca4ef50ecf595904af3d322ee8
URL:		http://search.cpan.org/dist/DateTime-Event-Cron/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Set-Crontab
BuildRequires:	perl-DateTime-Set
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DateTime::Event::Cron generated DateTime events or DateTime::Set
objects based on crontab-style entries.

%description -l pl.UTF-8
DateTIme::Event::Cron generuje zdarzenia DateTime lub obiekty
DateTime::Set z wpisów w stylu crontaba.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/Event/*.pm
%{_mandir}/man3/*
