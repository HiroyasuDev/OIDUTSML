# Project Structure

This document describes the production scaffolding structure.

## Directory Layout

```
OIDUTSML/
├── .github/
│   └── workflows/
│       ├── ci.yml          # Continuous Integration
│       └── cd.yml          # Continuous Deployment
├── .husky/
│   └── pre-commit          # Git hooks
├── src/
│   ├── __tests__/          # Test files
│   ├── config/             # Configuration modules
│   ├── controllers/        # Request controllers
│   ├── middleware/         # Express middleware
│   ├── routes/             # API route definitions
│   ├── services/           # Business logic services
│   ├── types/              # TypeScript type definitions
│   ├── utils/              # Utility functions
│   └── index.ts            # Application entry point
├── dist/                   # Compiled output (generated)
├── logs/                   # Log files (generated)
├── .dockerignore           # Docker ignore patterns
├── .editorconfig           # Editor configuration
├── .eslintrc.json          # ESLint configuration
├── .gitignore              # Git ignore patterns
├── .lintstagedrc.json      # Lint-staged configuration
├── .nvmrc                  # Node version
├── .prettierrc             # Prettier configuration
├── .prettierignore         # Prettier ignore patterns
├── CONTRIBUTING.md         # Contribution guidelines
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # Docker build configuration
├── INSTALL_LM_STUDIO.md    # LM Studio installation guide
├── Makefile                # Make commands
├── package.json            # Dependencies and scripts
├── PROJECT_STRUCTURE.md    # This file
├── README.md               # Project documentation
├── tsconfig.json           # TypeScript configuration
└── vitest.config.ts        # Vitest test configuration
```

## Key Files

### Configuration
- `package.json` - Dependencies and npm scripts
- `tsconfig.json` - TypeScript compiler options
- `.env` - Environment variables (not in git)
- `.env.example` - Environment variable template

### Docker
- `Dockerfile` - Multi-stage production build
- `docker-compose.yml` - Container orchestration
- `.dockerignore` - Docker build exclusions

### CI/CD
- `.github/workflows/ci.yml` - Automated testing and building
- `.github/workflows/cd.yml` - Automated deployment

### Code Quality
- `.eslintrc.json` - Linting rules
- `.prettierrc` - Code formatting
- `.lintstagedrc.json` - Pre-commit linting
- `.husky/pre-commit` - Git hooks

### Testing
- `vitest.config.ts` - Test framework configuration
- `src/__tests__/` - Test files

## Scripts

See `package.json` for all available scripts:

- `npm run dev` - Development server with hot reload
- `npm run build` - Production build
- `npm start` - Start production server
- `npm test` - Run tests
- `npm run lint` - Lint code
- `npm run format` - Format code

## Services

### LM Studio Service
Located in `src/services/lmStudio.ts`, provides:
- Chat completion API
- Model listing
- Configurable temperature and token limits

## Next Steps

1. Install dependencies: `npm install`
2. Configure environment: Copy `.env.example` to `.env`
3. Install LM Studio: See `INSTALL_LM_STUDIO.md`
4. Start development: `npm run dev`
