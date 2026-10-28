pkgname = "wooting-spectro"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "gtk+3-devel",
    "hidapi-devel",
    "pipewire-devel",
    "rust-std",
    "xdotool-devel",
]
depends = [
    "dinit-chimera-udev",
    "libayatana-appindicator-devel",
]

pkgdesc = "Spectrum analyzer for Wooting keyboards"
license = "GPL-3.0-only"
url = "https://tinkery.primmr.dev/PrimmR/wooting-spectro"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d0c89176240602787afe1772c5834906b411f691e95fdc9b6e121a8ea2a43d57"


def install(self):
    self.cargo.install(args=["--locked"])

    self.install_file("wooting-spectro.desktop", "usr/share/applications")

    self.install_file(
        "icons/icon.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="wooting-spectro.svg",
    )
