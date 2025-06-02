import { createRoot } from 'react-dom/client';
import React from 'react';
import App from './App';
// import { context } from './lib/contextBridge'; // Stub: contextBridge import

if ((import.meta as any).hot) {
  (import.meta as any).hot.on('cascade:update', (data) => {
    // context.update(data.key, data.value); // Commented out due to stubbed import
  });
}

const container = document.getElementById('root');
if (container) {
  createRoot(container).render(<App />);
}
