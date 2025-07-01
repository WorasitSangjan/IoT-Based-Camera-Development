# RustDesk Installation Guide for Raspberry Pi 5

This guide provides step-by-step instructions for installing and configuring RustDesk on a Raspberry Pi 5.

## Table of Contents
- [Basic Installation](#basic-installation)
- [Optional Setup](#optional-setup)
- [Fixed Password Configuration](#fixed-password-configuration)

## Basic Installation

### 1. Download RustDesk
- Visit the [RustDesk official website](https://rustdesk.com/)
- Click "Download" at the top right
- Scroll down to the Linux section
- Select "Debian/Ubuntu (arm64)" to download

### 2. Install RustDesk
```bash
cd ~/Downloads
sudo dpkg -i rustdesk-*.deb   # Replace * with actual version number
```

### 3. Fix Dependencies (If Needed)
If the installation fails due to missing dependencies:
```bash
sudo apt --fix-broken install -y
sudo apt install -y libxdo3 gstreamer1.0-pipewire libayatana-appindicator3-1
sudo dpkg -i rustdesk-*.deb   # Reinstall after fixing dependencies
```

### 4. Launch Application
```bash
rustdesk &
```
The application should now open and display your ID and Password.

## Optional Setup

### Enable Auto-Start on Boot
To configure RustDesk to start automatically when your Raspberry Pi boots:
```bash
sudo systemctl enable rustdesk
sudo systemctl start rustdesk
```

## Fixed Password Configuration

To set up a permanent password for unattended access:

1. Open RustDesk on your Raspberry Pi
2. Locate the three-dot menu (⋮) next to your RustDesk ID
3. Open Settings
4. In the Security section:
   - Enable "Use permanent password"
   - Set your desired permanent password