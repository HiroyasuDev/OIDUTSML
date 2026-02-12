import { Router } from 'express';
// Import your API route handlers here
// import { exampleRouter } from './example';

export const apiRouter = Router();

// Mount API routes
// apiRouter.use('/example', exampleRouter);

apiRouter.get('/', (_req, res) => {
  res.json({
    success: true,
    message: 'API is running',
    version: '1.0.0',
  });
});
