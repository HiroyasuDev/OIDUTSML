import { z } from 'zod';

const configSchema = z.object({
  nodeEnv: z.enum(['development', 'production', 'test']).default('development'),
  port: z.coerce.number().default(3000),
  host: z.string().default('0.0.0.0'),
  appName: z.string().default('OIDUTSML'),
  appVersion: z.string().default('1.0.0'),
  apiPrefix: z.string().default('/api/v1'),
  cors: z.object({
    origin: z.string().default('http://localhost:3000'),
    credentials: z.boolean().default(true),
  }),
  lmStudio: z.object({
    apiUrl: z.string().url().default('http://localhost:1234'),
    apiKey: z.string().optional(),
    model: z.string().optional(),
    temperature: z.coerce.number().default(0.7),
    maxTokens: z.coerce.number().default(2048),
  }),
  logging: z.object({
    level: z.enum(['error', 'warn', 'info', 'debug']).default('info'),
    format: z.enum(['json', 'simple']).default('json'),
  }),
});

const rawConfig = {
  nodeEnv: process.env.NODE_ENV,
  port: process.env.PORT,
  host: process.env.HOST,
  appName: process.env.APP_NAME,
  appVersion: process.env.APP_VERSION,
  apiPrefix: process.env.API_PREFIX,
  cors: {
    origin: process.env.CORS_ORIGIN,
    credentials: process.env.CORS_CREDENTIALS,
  },
  lmStudio: {
    apiUrl: process.env.LM_STUDIO_API_URL,
    apiKey: process.env.LM_STUDIO_API_KEY,
    model: process.env.LM_STUDIO_MODEL,
    temperature: process.env.LM_STUDIO_TEMPERATURE,
    maxTokens: process.env.LM_STUDIO_MAX_TOKENS,
  },
  logging: {
    level: process.env.LOG_LEVEL,
    format: process.env.LOG_FORMAT,
  },
};

export const config = configSchema.parse(rawConfig);

export type Config = z.infer<typeof configSchema>;
