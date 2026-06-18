import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://www.amazon.in/');
  await page.getByPlaceholder('Search Amazon.in').click();
  await page.getByPlaceholder('Search Amazon.in').fill('Iphone');
  await page.getByPlaceholder('Search Amazon.in').press('Enter');
  const page1Promise = page.waitForEvent('popup');
  await page.getByRole('link', { name: 'Sponsored Ad - iPhone 17e 256 GB: 15.40 cm (6.1″) Super Retina XDR Display, A19 Chip, All-Day Battery Life, 48MP Fusion Camera, 256GB Starting Storage; White' }).click();
  const page1 = await page1Promise;

  await page1.goto('https://www.amazon.in/Apple-iPhone-17e-256-GB/dp/B0GQW31KLK/ref=sr_1_1_sspa?crid=3708B4ZI34683&dib=eyJ2IjoiMSJ9.6W4JIzyvrzEdf_lw18RWajOo4L3jNrCf9rdP75Qpl0yp6d-M9gSZ-okDPp-2sSwxXv2NoYJKIPG8vp5LGUizOkoMnv4FzNGDwYn6bWkb60Etu2OjuqU908HQIE0e1QpqfyjQwh_TrPppwjxZ3bhB0HoKcTjLON6VdbW_vkd7dpkF3b_EwCAjF5cDiFHXH7wyDv-GdWUQBAmlaqCz69Yr0A5ghH9FPhqiURAVRFQNbmg.B6atrZhmo5ok2DDfclpk7VmRhXPCJ8MnmDulpKjYFmg&dib_tag=se&keywords=Iphone&qid=1781508279&sprefix=iphone%2Caps%2C344&sr=8-1-spons&aref=IrbePqgAbF&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1');


  expect(await page1.getByRole('button', { name: 'Add to cart' }).click());
  screenshot: true;
  await page1.screenshot({ path: 'screenshot.png' });
});