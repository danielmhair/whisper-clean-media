const { readdirSync, writeFileSync } = require("fs");

const imagesPaths = readdirSync(`${__dirname}/../cleaner/in_browser/public/images/`);
const images = imagesPaths.filter(i => i.endsWith(".jpg"))
writeFileSync(
  `${__dirname}/../cleaner/in_browser/src/utils/images.json`,
  JSON.stringify(images),
  "utf8",
)
