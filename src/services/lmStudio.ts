import { config } from '../config';
import { logger } from '../utils/logger';

export interface LMStudioRequest {
  model: string;
  messages: Array<{
    role: 'system' | 'user' | 'assistant';
    content: string;
  }>;
  temperature?: number;
  max_tokens?: number;
}

export interface LMStudioResponse {
  choices: Array<{
    message: {
      role: string;
      content: string;
    };
    finish_reason: string;
  }>;
  usage: {
    prompt_tokens: number;
    completion_tokens: number;
    total_tokens: number;
  };
}

export class LMStudioService {
  private apiUrl: string;
  private apiKey?: string;
  private defaultModel?: string;
  private defaultTemperature: number;
  private defaultMaxTokens: number;

  constructor() {
    this.apiUrl = config.lmStudio.apiUrl;
    this.apiKey = config.lmStudio.apiKey;
    this.defaultModel = config.lmStudio.model;
    this.defaultTemperature = config.lmStudio.temperature;
    this.defaultMaxTokens = config.lmStudio.maxTokens;
  }

  async chat(request: LMStudioRequest): Promise<LMStudioResponse> {
    const url = `${this.apiUrl}/v1/chat/completions`;

    const payload = {
      model: request.model || this.defaultModel || 'local-model',
      messages: request.messages,
      temperature: request.temperature ?? this.defaultTemperature,
      max_tokens: request.max_tokens ?? this.defaultMaxTokens,
    };

    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (this.apiKey) {
      headers['Authorization'] = `Bearer ${this.apiKey}`;
    }

    try {
      logger.debug('Sending request to LM Studio', { url, model: payload.model });

      const response = await fetch(url, {
        method: 'POST',
        headers,
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`LM Studio API error: ${response.status} ${errorText}`);
      }

      const data = (await response.json()) as LMStudioResponse;
      logger.debug('Received response from LM Studio', {
        tokens: data.usage?.total_tokens,
      });

      return data;
    } catch (error) {
      logger.error('LM Studio API request failed', { error });
      throw error;
    }
  }

  async listModels(): Promise<string[]> {
    const url = `${this.apiUrl}/v1/models`;

    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (this.apiKey) {
      headers['Authorization'] = `Bearer ${this.apiKey}`;
    }

    try {
      const response = await fetch(url, {
        method: 'GET',
        headers,
      });

      if (!response.ok) {
        throw new Error(`LM Studio API error: ${response.status}`);
      }

      const data = (await response.json()) as { data: Array<{ id: string }> };
      return data.data.map((model) => model.id);
    } catch (error) {
      logger.error('Failed to list LM Studio models', { error });
      throw error;
    }
  }
}

export const lmStudioService = new LMStudioService();
