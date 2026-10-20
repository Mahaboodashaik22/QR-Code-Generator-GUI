import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
from urllib.parse import urlparse


class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("520x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6fb")

        self.qr_image = None
        self.qr_photo = None

        tk.Label(
            root, text="QR Code Generator", font=("Arial", 20, "bold"),
            bg="#f4f6fb", fg="#202744"
        ).pack(pady=(22, 8))

        tk.Label(
            root, text="Enter a website URL to create your QR code",
            font=("Arial", 10), bg="#f4f6fb", fg="#555b70"
        ).pack(pady=(0, 14))

        self.url_entry = tk.Entry(
            root, width=48, font=("Arial", 11), relief="solid", bd=1
        )
        self.url_entry.pack(ipady=8, padx=28)
        self.url_entry.insert(0, "https://www.example.com")

        tk.Button(
            root, text="Generate QR Code", command=self.generate_qr,
            font=("Arial", 11, "bold"), bg="#4357d8", fg="white",
            activebackground="#3446bd", activeforeground="white",
            relief="flat", cursor="hand2", padx=14, pady=9
        ).pack(pady=14)

        self.image_label = tk.Label(
            root, text="Your QR code will appear here",
            width=34, height=14, bg="white", fg="#777777",
            relief="groove", bd=1
        )
        self.image_label.pack(pady=5)

        tk.Button(
            root, text="Save QR as PNG", command=self.save_qr,
            font=("Arial", 10, "bold"), bg="#16845b", fg="white",
            activebackground="#116b49", activeforeground="white",
            relief="flat", cursor="hand2", padx=14, pady=8
        ).pack(pady=14)

        tk.Label(
            root, text="Python • Tkinter • qrcode • Pillow",
            font=("Arial", 9), bg="#f4f6fb", fg="#777777"
        ).pack(side="bottom", pady=12)

    def generate_qr(self):
        url = self.url_entry.get().strip()

        if not url:
            messagebox.showwarning("Missing URL", "Please enter a URL.")
            return

        # Add a scheme if the user enters a domain without https://
        if "://" not in url:
            url = "https://" + url
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)

        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            messagebox.showerror(
                "Invalid URL",
                "Enter a valid web address, such as https://example.com."
            )
            return

        try:
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4
            )
            qr.add_data(url)
            qr.make(fit=True)
            self.qr_image = qr.make_image(
                fill_color="black", back_color="white"
            ).convert("RGB")

            preview = self.qr_image.copy()
            preview = self.qr_image.resize((250, 250))
            self.qr_photo = ImageTk.PhotoImage(preview)
            self.image_label.configure(
    image=self.qr_photo,
    text="",
    width=250,
    height=250
)
        except Exception as error:
            messagebox.showerror(
                "Generation Error", f"Could not generate the QR code.\n{error}"
            )

    def save_qr(self):
        if self.qr_image is None:
            messagebox.showwarning(
                "No QR Code", "Generate a QR code before saving it."
            )
            return

        file_path = filedialog.asksaveasfilename(
            title="Save QR Code",
            defaultextension=".png",
            filetypes=[("PNG image", "*.png")],
            initialfile="my_qr_code.png"
        )
        if not file_path:
            return

        try:
            self.qr_image.save(file_path, format="PNG")
            messagebox.showinfo(
                "Saved Successfully", f"QR code saved to:\n{file_path}"
            )
        except (OSError, ValueError) as error:
            messagebox.showerror(
                "Save Error", f"Could not save the image.\n{error}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
