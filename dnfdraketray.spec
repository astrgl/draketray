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

%changelog
*Tue May 02 2023 Astragalo <mauro.carbini@gmail.com> 2.0.8-mib1
- Separazione del pacchetto da DnfDrake

*Thu Dec 15 2022 Astragalo <mauro.carbini@gmail.com> 2.0.7-mib1
- Riassunto di tutti i changelog
- Aggiornamento di DnfDrakeTray versione 2.0.7 dovrebbe sistemare la posizione della finestra
- Modifica identificazione lingua in DnfDrake e DnfDrakeTray
- Spostata la finestra di DnfDrakeTray 2.0.3
- In DnfDrakeTray 2.0.2 corretta la gestione delle istanze multiple basata su intero anziche su stringa
- In DnfDrakeTray 2.0.1 corretta la gestione delle istanze multiple ora funziona
- In DnfDrakeTray 2.0.0 riscritta l'identificazione della lingua e la gestione delle istanze multiple
- Dnfdraketray imposta un carattere a 0 se non ci sono aggiornamenti a 1 se disponibili
- Fix  avvio automatico di   dnfdraketray quando non esiste la cartella autostart in .config
- Aggiunto pulsante reset su extra dnfdraketray
- Fix  su  dnfdraketray
- SHIFT+MOUSECLICK chiude dnfdraketray
- Fix vari su  dnfdraketray
- Cambiata l'icona di chiusura  dnfdraketray
- Semplificazione funzioni  dnfdraketray
- Fix vari su  dnfdraketray
- Fix opzione che  all'avvio  dnfdraketray
- Inserita opzione lancia all'avvio  dnfdraketray
- Rimosso il menu contestuale da dnfdraketray
- Migliorata la gestione di  dnfdraketray in dnfdrake >extra
- Evita l'apertura di più istanze di dnfdraketray
- Inizio funzionanalità trayicon
