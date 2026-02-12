# Installing LM Studio on Linux

LM Studio is a desktop application for running local LLMs. Here are the installation instructions for Linux.

## Method 1: AppImage (Recommended)

1. **Download LM Studio AppImage**
   - Visit [lmstudio.ai](https://lmstudio.ai)
   - Navigate to Downloads section
   - Download the Linux AppImage file

2. **Make it executable**
   ```bash
   chmod +x ~/Downloads/LM_Studio-*.AppImage
   ```

3. **Run LM Studio**
   ```bash
   ~/Downloads/LM_Studio-*.AppImage
   ```

4. **Optional: Move to Applications**
   ```bash
   sudo mv ~/Downloads/LM_Studio-*.AppImage /opt/lm-studio/
   sudo chmod +x /opt/lm-studio/LM_Studio-*.AppImage
   ```

## Method 2: Using the Official Installer

1. **Download the installer**
   ```bash
   cd ~/Downloads
   wget https://releases.lmstudio.ai/linux/latest -O lm-studio-installer
   ```

2. **Make executable and run**
   ```bash
   chmod +x lm-studio-installer
   ./lm-studio-installer
   ```

## Configuration

After installing and starting LM Studio:

1. **Start LM Studio** and download a model (e.g., Mistral 7B, Llama 2)
2. **Start the local server** in LM Studio (usually on port 1234)
3. **Update your `.env` file**:
   ```
   LM_STUDIO_API_URL=http://localhost:1234
   ```

## Verifying Installation

Test the connection:
```bash
curl http://localhost:1234/v1/models
```

If you get a JSON response with models, LM Studio is running correctly!

## Troubleshooting

- **Port already in use**: Change the port in LM Studio settings
- **API not responding**: Make sure the local server is started in LM Studio
- **Model not found**: Download a model in LM Studio first
