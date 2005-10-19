Summary:	Simple image viewer for GNUstep
Summary(pl):	Prosta przegl±darka obrazków dla ¶rodowiska GNUstep
Name:		PhotoClip
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.vaisburd.net/PhotoClip/%{name}-%{version}.tar.gz
# Source0-md5:	9d0b652f1db8a7d0a73183bf45e48420
URL:		http://www.vaisburd.net/PhotoClip/
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
This is PhotoClip, a simple image viewer application for GNUstep.

%description -l pl
To jest PhotoClip - prosta przegl±darka obrazków dla ¶rodowiska
GNUstep.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_prefix}/System/Applications/PhotoClip.app
%attr(755,root,root) %{_prefix}/System/Applications/PhotoClip.app/PhotoClip
%dir %{_prefix}/System/Applications/PhotoClip.app/Resources
%{_prefix}/System/Applications/PhotoClip.app/Resources/*.desktop
%{_prefix}/System/Applications/PhotoClip.app/Resources/*.plist
%{_prefix}/System/Applications/PhotoClip.app/Resources/*.tiff
%dir %{_prefix}/System/Applications/PhotoClip.app/%{gscpu}
%dir %{_prefix}/System/Applications/PhotoClip.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/PhotoClip.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/PhotoClip.app/%{gscpu}/%{gsos}/%{libcombo}/PhotoClip
%{_prefix}/System/Applications/PhotoClip.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
