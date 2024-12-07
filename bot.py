from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# List of video URLs
VIDEO_LINKS = [
    "https://graph.org/file/9ab991293a986ebf6bfc9.mp4",
    "https://example.com/video2.mp4",
    "https://envs.sh/YNo.mp4",
    "https://envs.sh/YNo.mp4",
    "https://example.com/video5.mp4",
    "https://example.com/video6.mp4",
    "https://example.com/video7.mp4",
    "https://example.com/video8.mp4",
    "https://example.com/video9.mp4",
    "https://example.com/video10.mp4",
]

# Initialize context to track current video index
CURRENT_VIDEO_INDEX = 0

# Start command: Send a welcome message with buttons, animations, and media
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Animation (GIF) to be sent with the start message
    animation_url = "https://media.giphy.com/media/l0HUqsz2jdQYElRm0/giphy.gif"  # Replace with your animation URL

    # Inline keyboard buttons
    keyboard = [
        [InlineKeyboardButton("❤️ PLAY VIDEO ❤️", callback_data="play_video")],
        [InlineKeyboardButton("💌 Support 💌", url="https://t.me/Ansh_coding_STR")],  # Replace with your support link
        [InlineKeyboardButton("All bots", url="https://t.me/ansh_hack")]  # Replace with your Telegram channel link
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the animation and message
    await update.message.reply_animation(
        animation=animation_url,
        caption="Dear: 😁 𝐔𝐒𝐄𝐑  ☹︎\nHere's your video\n\n"
                "══════♡@cyber_ansh♡════ \n═══════ ♡ ANSH ♡═══════\n"
                "═════════ ★★ ═════════",
        reply_markup=reply_markup,
    )

# Handle video playback
async def play_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CURRENT_VIDEO_INDEX

    # Get the current video URL
    video_url = VIDEO_LINKS[CURRENT_VIDEO_INDEX]

    # Update the index for the next video
    CURRENT_VIDEO_INDEX = (CURRENT_VIDEO_INDEX + 1) % len(VIDEO_LINKS)

    # Answer the callback query to show an updated response
    query = update.callback_query
    await query.answer()

    # Animation (GIF) for video interaction
    video_gif_url = "https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif"  # Replace with your animation URL

    # Send the animation before sharing the video link
    await query.message.reply_animation(animation=video_gif_url, caption="Preparing your video...")

    # Send the video link to the user
    await query.message.reply_text(
        f"Here's your video: [Click to Watch]({video_url})",
        parse_mode="Markdown",
    )

# Main function to set up the bot
def main():
    TOKEN = "7200585807:AAHCf3bGC-GGETE7NJe-UPPZI9AzLZ-VqUI"  # Replace with your Telegram bot token
    application = ApplicationBuilder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(play_video, pattern="play_video"))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# List of video URLs
VIDEO_LINKS = [
    "https://graph.org/file/9ab991293a986ebf6bfc9.mp4",
    "https://example.com/video2.mp4",
    "https://envs.sh/YNo.mp4",
    "https://envs.sh/YNo.mp4",
    "https://example.com/video5.mp4",
    "https://example.com/video6.mp4",
    "https://example.com/video7.mp4",
    "https://example.com/video8.mp4",
    "https://example.com/video9.mp4",
    "https://example.com/video10.mp4",
]

# Initialize context to track current video index
CURRENT_VIDEO_INDEX = 0

# Start command: Send a welcome message with buttons and media
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Image to be sent with the start message
    image_url = "https://envs.sh/YN8.jpg"  # Replace with your image URL

    # Inline keyboard buttons
    keyboard = [
        [InlineKeyboardButton("❤️ PLAY VIDEO ❤️", callback_data="play_video")],
        [InlineKeyboardButton("💌 Support 💌", url="https://t.me/Ansh_coding_STR")],  # Replace with your support link
        [InlineKeyboardButton("All bots", url="https://t.me/ansh_hack")]  # Replace with your Telegram channel link
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the image and message
    await update.message.reply_photo(
        photo=image_url,
        caption="Dear: 😁 𝐔𝐒𝐄𝐑  ☹︎\nHere's your video\n\n"
                "══════♡@cyber_ansh♡════ \n═══════ ♡ ANSH ♡═══════\n"
                "═════════ ★★ ═════════",
        reply_markup=reply_markup,
    )

# Handle video playback
# Handle video playback
async def play_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CURRENT_VIDEO_INDEX

    # Get the current video URL
    video_url = VIDEO_LINKS[CURRENT_VIDEO_INDEX]

    # Update the index for the next video
    CURRENT_VIDEO_INDEX = (CURRENT_VIDEO_INDEX + 1) % len(VIDEO_LINKS)

    # Answer the callback query to show an updated response
    query = update.callback_query
    await query.answer()

    # Image for video interaction
    video_image_url = "https://envs.sh/video_placeholder.jpg"  # Replace with your placeholder image URL

    # Send the image with the video link caption
    await query.message.reply_photo(
        photo=video_image_url,
        caption=f"Here's your video: [Click to Watch]({video_url})",
        parse_mode="Markdown",
    )


    # Get the current video URL
    video_url = VIDEO_LINKS[CURRENT_VIDEO_INDEX]

    # Update the index for the next video
    CURRENT_VIDEO_INDEX = (CURRENT_VIDEO_INDEX + 1) % len(VIDEO_LINKS)

    # Answer the callback query to show an updated response
    query = update.callback_query
    await query.answer()

    # Image for video interaction
    video_image_url = "https://envs.sh/video_placeholder.jpg"  # Replace with your placeholder image URL

    # Send the image before sharing the video link
    await query.message.reply_photo(photo=video_image_url, caption="Preparing your video...")

    # Send the video link to the user
    await query.message.reply_text(
        f"Here's your video: [Click to Watch]({video_url})",
        parse_mode="Markdown",
    )

# Main function to set up the bot
def main():
    TOKEN = "7200585807:AAHCf3bGC-GGETE7NJe-UPPZI9AzLZ-VqUI"  # Replace with your Telegram bot token
    application = ApplicationBuilder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(play_video, pattern="play_video"))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
