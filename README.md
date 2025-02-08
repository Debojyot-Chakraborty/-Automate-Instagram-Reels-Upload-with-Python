Got it! Here's the updated **README** without the license section, marked as an open-source project created by you.

---

# Instagram Reels Auto-Uploader with Python 📲

This Python script automates Instagram Reels uploading for multiple accounts using the **Instagrapi library**. It logs into each account, uploads a video, and adds a comment automatically after posting. This tool is perfect for **social media managers, influencers, and marketers** who manage multiple Instagram accounts.

## Features 🚀

- ✅ **Multi-account login support**  
- ✅ **Automated Reel uploads**  
- ✅ **Auto-commenting after upload**  
- ✅ **Secure login/logout handling**  
- ✅ **Error handling for failed uploads**

## Requirements 🛠

Before you begin, ensure that you have the following:

- Python 3.x installed
- Instagram accounts for automation
- Install the necessary dependencies using:

```bash
pip install instagrapi
```

## How to Use 📋

1. **Clone the Repository**:  


2. **Set up Your Accounts**:  
   Edit the `accounts` list in the `bot.py` file with your Instagram account credentials (username and password).

   ```python
   accounts = [
       {'username': 'your_username1', 'password': 'your_password1'},
       {'username': 'your_username2', 'password': 'your_password2'},
   ]
   ```

3. **Set the Video Path**:  
   Ensure that the `video_path` variable in the `bot.py` file points to the video file you want to upload.

   ```python
   video_path = r"C:\path\to\your\video.mp4"
   ```

4. **Run the Script**:  
   Run the Python script to begin uploading the Reels:

   ```bash
   python bot.py
   ```

5. **Manual OTP Entry**:  
   If Instagram requests an OTP (two-factor authentication), enter it manually in the terminal for each account.

6. **Enjoy Automation**:  
   The script will automatically upload the video to each account and add a comment to the post.

## Notes ⚠️

- **Disable 2FA** on Instagram accounts to avoid login issues.
- Manual OTP entry will be required if Instagram requests it.
- **Use proxies** if managing multiple accounts to avoid IP bans.
- This script is for educational purposes. Use it responsibly.

## Contributing 🤝

Feel free to fork this repository, open issues, or submit pull requests. If you encounter any bugs or have suggestions for improvements, don't hesitate to contribute.

---

**This is an open-source project created by Debojyoti Chakraborty. Feel free to use and contribute!**
