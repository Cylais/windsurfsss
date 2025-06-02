# Playwright + Brave Setup Guide

## Version: 1.0.0 (Last updated: 2025-05-25)

This guide explains how to run Playwright tests using the Brave browser in your Windsurf project.

## 1. Install Playwright (if not already)

```bash
npm install -D @playwright/test
```

## 2. Configure Playwright to Use Brave

- The provided `playwright.config.js` is already set up to launch Brave.
- If Brave is installed in a non-standard location, update the `bravePath` variable in the config file.

## 3. Run Your Tests

```bash
npx playwright test --project=Brave
```

## 4. Troubleshooting

- If Playwright cannot find Brave, double-check the path in `playwright.config.js`.
- You can find Brave's path by right-clicking the Brave shortcut and checking properties.

## 5. Why Use Brave?

- Matches your real-world browser for more accurate testing.
- Chromium-based, so most Playwright features work seamlessly.

---

For more advanced config, see Playwright docs: <https://playwright.dev/docs/browsers#google-chrome--microsoft-edge>
