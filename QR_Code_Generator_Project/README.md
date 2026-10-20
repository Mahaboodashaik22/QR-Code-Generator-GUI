# QR Code Generator GUI

A simple desktop QR Code Generator built with Python, Tkinter, `qrcode`, and Pillow.

## Features
- Enter a website URL.
- Generate and preview a QR code in the GUI.
- Save the generated QR code as a PNG image.
- Basic validation and error messages.

## Requirements
- Python 3.9 or newer
- Tkinter (usually included with Python)
- `qrcode`
- Pillow

## Installation
Open a terminal in this folder and run:

```bash
python -m pip install "qrcode[pil]" Pillow
```

## Run
```bash
python qr_code_generator.py
```

## Test checklist
1. Enter `https://www.example.com` and generate a QR code.
2. Save it as `my_qr_code.png`.
3. Open the PNG and scan it with a phone camera.
4. Try an empty input and confirm a warning appears.
5. Try invalid text such as `hello world` and confirm an error appears.
6. Try a domain such as `example.com`; the app adds `https://`.

## Files to submit
- `qr_code_generator.py` — source code
- `my_qr_code.png` — sample generated QR image
- `gui_screenshot.png` — take a screenshot of the running app on your computer

## GitHub upload
Create a GitHub repository named `QR-Code-Generator-GUI`, then run:

```bash
git init
git add qr_code_generator.py README.md my_qr_code.png
git commit -m "Add Python QR Code Generator GUI"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/QR-Code-Generator-GUI.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Add `gui_screenshot.png` after you take it:
```bash
git add gui_screenshot.png
git commit -m "Add GUI screenshot"
git push
```
