# Contributing to OIDUTSML

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Install dependencies: `npm install`

## Development Workflow

1. **Make your changes**
   - Write clean, readable code
   - Follow the existing code style
   - Add tests for new features
   - Update documentation as needed

2. **Run checks before committing**
   ```bash
   npm run lint
   npm run format:check
   npm run type-check
   npm test
   ```

3. **Commit your changes**
   - Use clear, descriptive commit messages
   - Follow conventional commit format when possible

4. **Push and create a Pull Request**
   - Push to your fork
   - Create a PR with a clear description
   - Reference any related issues

## Code Style

- Use TypeScript for all new code
- Follow ESLint and Prettier configurations
- Write self-documenting code with clear variable names
- Add JSDoc comments for public APIs

## Testing

- Write tests for all new features
- Maintain or improve test coverage
- Tests should be fast and isolated

## Pull Request Process

1. Ensure all tests pass
2. Update documentation if needed
3. Get at least one review before merging
4. Squash commits when merging (if requested)

## Questions?

Feel free to open an issue for questions or discussions.
