#!/bin/bash

set -e

echo "🚀 Setting up OIDUTSML project..."

# Check Node.js version
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js version 18+ is required. Current version: $(node -v)"
    exit 1
fi

echo "✅ Node.js $(node -v) detected"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Create logs directory if it doesn't exist
mkdir -p logs

# Copy .env.example to .env if .env doesn't exist
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        echo "📝 Creating .env file from .env.example..."
        cp .env.example .env
        echo "⚠️  Please update .env with your configuration"
    else
        echo "⚠️  .env.example not found. Creating basic .env..."
        cat > .env << 'EOF'
NODE_ENV=development
PORT=3000
HOST=0.0.0.0
APP_NAME=OIDUTSML
APP_VERSION=1.0.0
API_PREFIX=/api/v1
LM_STUDIO_API_URL=http://localhost:1234
LOG_LEVEL=info
LOG_FORMAT=json
CORS_ORIGIN=http://localhost:3000
CORS_CREDENTIALS=true
EOF
    fi
else
    echo "✅ .env file already exists"
fi

# Setup Husky
echo "🐕 Setting up Husky..."
npx husky install || echo "⚠️  Husky setup skipped (may need git init first)"

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Review and update .env file"
echo "  2. Install LM Studio (see INSTALL_LM_STUDIO.md)"
echo "  3. Run 'npm run dev' to start development server"
echo ""
