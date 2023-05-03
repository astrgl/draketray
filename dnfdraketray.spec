Name: dnfdraketray
Version: 2.0.8
Release: 1
Packager: Astragalo
License: GPL
Group: Graphical desktop/KDE
Summary: Tray for DnfDrake
Url: https://mib.pianetalinux.org/
Source: %{name}-%{version}.tar.gz


Requires: sudo
Requires: gambas3-runtime
Requires: gambas3-gb-form
Requires: gambas3-gb-image
Requires: gambas3-gb-gui
Requires: gambas3-gb-qt5
Requires: gambas3-gb-gtk3
Requires: gambas3-gb-dbus
Requires: gambas3-gb-form-stock
Requires: hicolor-icon-theme
Requires: lsb-release
Requires: xrandr
Requires: dnfdrake
BuildArch: noarch

Conflicts:  gambas3-runtime  > 3.18.1

%description
DnfDrakeTray is a trayapp for DnfDrake

%prep
%autosetup -n %{name}

%build
gbc3
sleep 2
gba3


%install
install -Dm 755 dnfdraketray.gambas -t %{buildroot}/%{_bindir}/
install -Dm 644 FILE-EXTRA/license -t %{buildroot}/%{_datadir}/dnfdrake/
install -Dm 755 FILE-EXTRA/dnfdraketray.gambas.desktop -t %{buildroot}/%{_datadir}/dnfdrake/


%files
%{_bindir}/dnfdraketray.gambas
%{_datadir}/dnfdrake/license
%{_datadir}/dnfdrake/dnfdraketray.gambas.desktop
