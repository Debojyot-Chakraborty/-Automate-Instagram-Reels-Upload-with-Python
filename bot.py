from instagrapi import Client

# List of Instagram accounts (Replace with your credentials)
accounts = [
    {'username': 'your_username1', 'password': 'your_password1'},
    {'username': 'your_username2', 'password': 'your_password2'}
]

# Path to the video file
video_path = r"C:\Path\To\Your\Video.mp4"
caption = "Your video caption here"

for account in accounts:
    try:
        cl = Client()
        print(f"\n🔑 Logging into {account['username']}...")
        cl.login(account['username'], account['password'])
        print(f"✅ Successfully logged in to {account['username']}!")

        # Uploading the video
        print(f"📤 Uploading video for {account['username']}...")
        cl.video_upload(video_path, caption)
        print(f"🎬 Video uploaded successfully to {account['username']}!")

        # Fetch user ID
        user_id = cl.user_id_from_username(account['username'])

        # Fetch last uploaded media
        user_medias = cl.user_medias(user_id, 1)
        if user_medias:
            media_id = user_medias[0].id  # Get the media ID
            cl.media_comment(media_id, "Follow @your_account")
            print(f"💬 Comment added to {account['username']}'s post!")

        cl.logout()
        print(f"🚪 Logged out from {account['username']}.")

    except Exception as e:
        print(f"❌ Error uploading video to {account['username']}: {e}")
