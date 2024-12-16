Name:			espanso-wayland
Version: 		2.2.1
Release:		1%?dist
Summary:		Cross-platform Text Expander written in Rust for Wayland
License:		GPL-3.0
URL:			https://espanso.org
Source0:		https://github.com/espanso/espanso/archive/refs/tags/v%version.tar.gz
Requires:		libxkbcommon dbus libnotify wxGTK wl-clipboard
Conflicts:		espanso-x11
BuildRequires:	gcc gcc-c++
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	wxGTK-devel
BuildRequires:	openssl-devel
BuildRequires:  mold

%global debug_package %{nil}
%description
A cross-platform Text Expander written in Rust. A text expander is a program
that detects when you type a specific keyword and replaces it with something
else.

This package includes the Wayland version of espanso.


%prep
#%autosetup -n espanso-%version
#cd espanso
cargo install --force cargo-make --version 0.34.0
#%cargo_prep_online

%build
#cd espanso
cargo make --profile release --env NO_X11=true build-binary

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm755 target/release/espanso %{buildroot}%{_bindir}/espanso

%files
%caps(cap_dac_override=pe) %_bindir/espanso

%changelog
%autochangelog
