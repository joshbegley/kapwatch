const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox']});
  const page = await browser.newPage();
  page.setViewport({width: 1024, height: 700});
  await page.goto('https://kapwatch.com');
  await page.waitFor(5000);
  await page.screenshot({path: 'screenshot.png'});

  await browser.close();
})();
