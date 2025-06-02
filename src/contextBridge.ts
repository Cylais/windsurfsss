import { EventEmitter } from 'events';
import { nanoid } from 'nanoid';

type ContextUpdate = {
  id: string;
  key: string;
  value: unknown;
  timestamp: number;
  origin: string;
};

declare global {
  interface CascadeContext extends EventEmitter {
    emit?: (...args: any[]) => void;
    on?: (...args: any[]) => void;
    off?: (...args: any[]) => void;
  }
}

export class CascadeContext extends EventEmitter {
  private state: Record<string, unknown> = {};
  private versions = new Map<string, string>();

  update(key: string, value: unknown) {
    const updateId = nanoid();
    this.state[key] = value;
    this.versions.set(key, updateId);
    this.emit('update', { 
      id: updateId,
      key,
      value,
      timestamp: Date.now(),
      origin: window.location.href 
    });
  }

  subscribe(key: string, callback: (value: unknown) => void) {
    const handler = (update: ContextUpdate) => {
      if (update.key === key) callback(update.value);
    };
    this.on('update', handler);
    return () => this.off('update', handler);
  }
}

export const context = new CascadeContext();
