# OIDUTSML

Production-ready application with LM Studio integration.

## 🚀 Features

- **TypeScript** - Full type safety
- **Express.js** - Fast, unopinionated web framework
- **LM Studio Integration** - Local LLM support
- **Docker** - Containerized deployment
- **CI/CD** - GitHub Actions workflows
- **Testing** - Vitest test framework
- **Linting & Formatting** - ESLint + Prettier
- **Logging** - Winston logger
- **Security** - Helmet, CORS, input validation

## 📋 Prerequisites

- Node.js >= 18.0.0
- npm >= 9.0.0
- Docker (optional, for containerized deployment)
- LM Studio (for LLM features)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd OIDUTSML
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Create logs directory**
   ```bash
   mkdir -p logs
   ```

## 🏃 Development

```bash
# Start development server with hot reload
npm run dev

# Run tests
npm test

# Run tests with coverage
npm run test:coverage

# Lint code
npm run lint

# Format code
npm run format

# Type check
npm run type-check

# Build for production
npm run build
```

## 🐳 Docker

```bash
# Build Docker image
npm run docker:build

# Run with docker-compose
npm run docker:run

# Stop containers
npm run docker:down
```

## 📦 Production

```bash
# Build application
npm run build

# Start production server
npm start
```

## 🔧 Configuration

Environment variables are configured in `.env` file. See `.env.example` for all available options.

### LM Studio Setup

1. Install and start LM Studio
2. Configure the API URL in `.env`:
   ```
   LM_STUDIO_API_URL=http://localhost:1234
   ```
3. Optionally set model and API key

## 🧪 Testing

```bash
# Run all tests
npm test

# Run tests with UI
npm run test:ui

# Run tests with coverage
npm run test:coverage
```

## 📁 Project Structure

```
OIDUTSML/
├── src/
│   ├── config/          # Configuration
│   ├── controllers/     # Request handlers
│   ├── middleware/      # Express middleware
│   ├── routes/          # API routes
│   ├── services/        # Business logic
│   ├── types/           # TypeScript types
│   ├── utils/           # Utility functions
│   └── index.ts         # Application entry point
├── dist/                # Compiled output
├── tests/               # Test files
├── .github/             # GitHub Actions workflows
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
└── package.json         # Dependencies and scripts
```

## 🔒 Security

- Helmet.js for security headers
- CORS configuration
- Input validation with Zod
- Environment variable validation

## 📝 License

MIT

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.
