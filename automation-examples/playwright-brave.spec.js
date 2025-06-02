const { test, expect } = require('@playwright/test');

test('Brave loads Windsurf project homepage', async ({ page }) => {
  await page.goto('http://localhost:3000'); // Change to your local dev server if different
  await expect(page).toHaveTitle(/Windsurf/i);
});
