import { useEffect, useState } from 'react';
// import '../lib/contextBridge';
const context = {
  subscribe: (key: string, cb: (val: unknown) => void) => () => {},
  update: (key: string, value: unknown) => {}
};

export function useCascadeContext<T>(key: string, initialValue?: T) {
  const [value, setValue] = useState<T>(initialValue as T);

  useEffect(() => {
    return context.subscribe(key, (newValue) => {
      setValue(newValue as T);
    });
  }, [key]);

  const update = (newValue: T) => context.update(key, newValue);

  return [value, update] as const;
}
