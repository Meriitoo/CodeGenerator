import tkinter as tk
import pyotp


class OTPGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Generator and Verifier")

        self.secret_key = pyotp.random_base32()
        self.otp_label = tk.Label(root, text="Generated OTP: ", font=("Times New Roman", 20))
        self.otp_label.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate OTP", command=self.generate_otp, font=("Times New Roman", 18,), background='lightgreen')
        self.generate_button.pack(pady=10)

        self.verify_label = tk.Label(root, text="Enter OTP: ", font=("Times New Roman", 15, 'bold'))
        self.verify_label.pack()

        self.otp_entry = tk.Entry(root, font=("Times New Roman", 30))
        self.otp_entry.pack()

        self.verify_button = tk.Button(root, text="Verify OTP", command=self.verify_otp, font=("Times New Roman", 12), background ='lightblue')
        self.verify_button.pack(pady=10)

    def generate_otp(self):
        totp = pyotp.TOTP(self.secret_key)
        otp = totp.now()
        self.otp_label.config(text=f"Generated OTP: {otp}")

    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        totp = pyotp.TOTP(self.secret_key)

        if totp.verify(entered_otp):
            result_label.config(text="OTP verification successful!", fg="green")
        else:
            result_label.config(text="OTP verification failed!", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    otp_generator = OTPGenerator(root)
    result_label = tk.Label(root, text="", font=("Times New Roman", 14))
    result_label.pack(pady=10)
    root.mainloop()
