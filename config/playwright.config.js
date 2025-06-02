/**
 * playwright.config.js: Playwright Test Runner Configuration
 *
 * Purpose:
 *   - Defines browser automation and testing settings for this project.
 *   - Supports cross-platform and custom browser automation (e.g., Brave, Chrome, Firefox).
 *   - Used in CI pipelines and local development for E2E and integration tests.
 *
 * Usage:
 *   - Run tests with: npx playwright test
 *   - Update or add browser projects in the 'projects' array below.
 *   - For TypeScript settings, see tsconfig.json and tsconfig.node.json.
 *   - For onboarding and troubleshooting, see ONBOARDING.md.
 *
 * How to add a new browser project (template):
 *   {
 *     name: 'Firefox',
 *     use: {
 *       channel: 'firefox',
 *       headless: false,
 *     },
 *   }
 *
 * Extensibility:
 *   - Update 'executablePath' to support custom browser installs (see bravePath).
 *   - Add more projects for parallel cross-browser testing.
 *   - Integrate with CI by running 'npx playwright install' and 'npx playwright test'.
 *
 * Related files:
 *   - tsconfig.json, tsconfig.node.json: TypeScript settings for Playwright and test files.
 *   - ONBOARDING.md: Quick start and troubleshooting.
 */
const { defineConfig, devices } = require('@playwright/test');
const path = require('path');

// Path to Brave browser executable (update if your Brave install is elsewhere)
const bravePath = process.platform === 'win32'
  ? 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
  : '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser';

module.exports = defineConfig({
  projects: [
    {
      name: 'Brave',
      use: {
        channel: 'chrome', // Playwright uses Chromium, but we override the executablePath
        executablePath: bravePath,
        headless: true,
      },
    },
    // Example: Add more browser projects here for parallel testing
    // {
    //   name: 'Firefox',
    //   use: {
    //     channel: 'firefox',
    //     headless: false,
    //   },
    // }
  ],
});
