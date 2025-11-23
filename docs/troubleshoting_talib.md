# Troubleshooting & Setup Guide

## TA-Lib Installation Issues
This project relies on `TA-Lib` for financial calculations. This library often fails to install via pip on Windows/Linux because it requires underlying C-libraries.

### For Windows Users
If `pip install ta-lib` fails:
1. Download the binary `.whl` file matching your Python version from [Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib).
2. Run: `pip install TA_Lib-0.4.24-cp310-win_amd64.whl` (Example name).

### For CI/CD (GitHub Actions)
The standard Ubuntu runner requires the C-library dependencies before `pip` installation:
```yaml
- name: Install TA-Lib System Dependencies
  run: |
    sudo apt-get update
    sudo apt-get install -y libta-lib-dev