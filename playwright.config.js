const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: '.',
  testMatch: ['**/*.ts'],
  use: {
    headless: false,
  },
});
