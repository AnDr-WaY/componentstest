# Discord Meme Bot 🎭

A modern Discord bot that displays random memes using Discord's **experimental UI Kit Components v2** from an active pull request. This showcases the upcoming MediaGallery, Container, and LayoutView features before their official release.

## ⚠️ Important Notice

**This project uses EXPERIMENTAL features from discord.py pull request!**

- Uses discord.py from `feature/voice-receive` branch with UI Kit Components v2
- These components are **not yet officially released**
- API may change before stable release
- For educational and testing purposes

## ✨ Features

- **Random Meme Display**: Fetches random memes from the meme API
- **Experimental UI Components**: Uses unreleased Discord UI Kit v2 components
- **One-Click Refresh**: Button to generate new memes instantly
- **Russian Language Support**: Interface in Russian with emoji indicators
- **Cutting-edge Architecture**: Built with discord.py's upcoming Container and LayoutView system

## 🛠️ Requirements

- Python 3.8+
- **discord.py from pull request** (experimental UI Kit v2 support)
- requests library
- python-dotenv (for environment variables)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd componentstest
   ```

2. **Install dependencies** (includes experimental discord.py):
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   BOT_TOKEN=your_discord_bot_token_here
   ```

4. **Create a Discord Application**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to "Bot" section and create a bot
   - Copy the bot token to your `.env` file
   - Enable necessary intents (Message Content Intent may be required)

## 🚀 Usage

1. **Run the bot**:
   ```bash
   python main.py
   ```

2. **Invite the bot to your server**:
   - Go to Discord Developer Portal → Your App → OAuth2 → URL Generator
   - Select `bot` scope and necessary permissions
   - Use the generated URL to invite the bot

3. **Use the bot**:
   ```
   !meme        # Display a random meme with refresh button
   !random_meme # Alternative command
   ```

## 🎮 Commands

| Command | Aliases | Description |
|---------|---------|-------------|
| `!random_meme` | `!meme` | Displays a random meme with an interactive refresh button |

## 🔧 Configuration

The bot uses environment variables for configuration:

- `BOT_TOKEN`: Your Discord bot token (required)

## 🏗️ Architecture - UI Kit Components v2

This bot showcases Discord's **experimental** UI Kit components:

- **`Container`**: Groups UI components together *(experimental)*
- **`LayoutView`**: Modern view system for organizing layouts *(experimental)*
- **`MediaGallery`**: Displays media content with descriptions *(experimental)*
- **`Section`**: Organizes components with accessories *(experimental)*
- **`TextDisplay`**: Shows formatted text content *(experimental)*
- **`Button`**: Interactive button component *(existing)*

### Code Structure

```
main.py
├── TestButton          # Interactive button for meme refresh
├── TestContainer       # Container holding all UI components (v2)
├── TestView           # LayoutView managing the container (v2)
└── random_meme()      # Command handler
```

## 🔄 How It Works

1. User runs `!meme` command
2. Bot fetches a random meme from `https://meme-api.com/gimme`
3. Creates a MediaGallery with the meme image *(experimental component)*
4. Displays UI with title, meme, and refresh button
5. When button is clicked:
   - Bot defers the interaction
   - Fetches a new random meme
   - Updates the MediaGallery with new content
   - No new message is sent (seamless update)

## 🌐 API Used

- **Meme API**: `https://meme-api.com/gimme`
  - Returns JSON with random meme URLs
  - No authentication required
  - Free to use

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Requirements File

The `requirements.txt` includes experimental discord.py:
```
# Experimental discord.py with UI Kit Components v2
git+https://github.com/Rapptz/discord.py.git@feature/voice-receive#egg=discord.py

# Other dependencies
requests>=2.25.1
python-dotenv>=0.19.0
```

## ⚠️ Important Notes

- **EXPERIMENTAL**: This bot uses unreleased Discord UI Kit Components v2
- **API Changes**: Components API may change before official release
- **Pull Request Dependency**: Uses discord.py from active pull request
- **Testing Purpose**: Intended for learning and testing new features
- **Not Production Ready**: Wait for official release for production use

## 🔒 Security

- Never hardcode bot tokens in your source code
- Use environment variables for sensitive information
- Add `.env` to your `.gitignore` file
- Regularly rotate your bot tokens

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Troubleshooting

**Bot not responding to commands?**
- Check if the bot has proper permissions
- Ensure Message Content Intent is enabled if needed
- Verify the bot token is correct

**UI Components not working?**
- Make sure you're using the experimental discord.py from the pull request
- Check that all components are properly imported
- Verify the interaction defer timing

**Images not loading?**
- The meme API might be temporarily unavailable
- Check network connectivity
- Some meme URLs might be invalid or expired

**Installation issues?**
- Ensure git is installed for pull request installation
- Try reinstalling with `pip install --force-reinstall -r requirements.txt`

---

Made with ❤️ using Discord's **experimental** Bot UI Kit v2 