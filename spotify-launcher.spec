%global debug_package %{nil}

Name:		spotify-launcher
Version:	0.6.3
Release:	2
Source0:	https://github.com/kpcyrd/spotify-launcher/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Client for spotifies apt repository in Rust
URL:		https://github.com/kpcyrd/spotify-launcher
License:	Apache 2.0
Group:		Application/Audio

BuildRequires:	cargo
BuildRequires:	pkgconfig(liblzma)


Requires:	%mklibname sequoia-sqv
Requires: zenity-gtk

%description
%summary

%prep
%autosetup -p1
tar -zxf %{SOURCE1}
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/SoftbearStudios/bitcode.git?rev=5f25a59"]
git = "https://github.com/SoftbearStudios/bitcode.git"
rev = "5f25a59"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
cargo build --release --frozen

%install
install -Dm 755 target/release/spotify-launcher %{buildroot}%{_bindir}/%{name}

install -Dm 644 data/pubkey_C85668DF69375001.gpg %{buildroot}%{_datadir}/%{name}/keyring.pgp

install -Dm644 contrib/spotify-launcher.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm644 contrib/icons/spotify-linux-512.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

install -Dm644 contrib/spotify-launcher.conf -t %{buildroot}%{_sysconfdir}/

install -Dm644 contrib/icons/spotify-linux-22.png %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/spotify-launcher.png
install -Dm644 contrib/icons/spotify-linux-24.png %{buildroot}/%{_datadir}/icons/hicolor/24x24/apps/spotify-launcher.png
install -Dm644 contrib/icons/spotify-linux-32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/spotify-launcher.png
install -Dm644 contrib/icons/spotify-linux-48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/spotify-launcher.png
install -Dm644 contrib/icons/spotify-linux-64.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/spotify-launcher.png
install -Dm644 contrib/icons/spotify-linux-128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/spotify-launcher.png
install -Dm644 contrib/icons/spotify-linux-256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/spotify-launcher.png
install -Dm644 contrib/icons/spotify-linux-512.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/spotify-launcher.png

install -Dm644 LICENSE-APACHE %{buildroot}%{_datadir}/license/%{name}/LICENSE-APACHE
install -Dm644 LICENSE-MIT %{buildroot}%{_datadir}/license/%{name}/LICENSE-MIT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/keyring.pgp
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_sysconfdir}/%{name}.conf
%{_datadir}/icons/hicolor/*
%{_datadir}/license/%{name}/LICENSE-APACHE
%{_datadir}/license/%{name}/LICENSE-MIT
