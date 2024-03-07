const compressImages = require("compress-images");
const path = require("path");
const filePath = process.argv[2];
console.log(filePath);
var savePath = (filePath) => path.parse(filePath).dir;
const saveHere = savePath(filePath);
function compressImg(filePath, saveHere) {
  compressImages(
    filePath,
    saveHere + "/",
    { compress_force: true, statistic: true, autoupdate: true },
    true,

    {
      jpg: {
        engine: "mozjpeg",
        command: ["-quality", "60"],
      },
    },
    {
      png: {
        engine: "pngquant",
        command: ["--quality=20-50", "--ext=.png", "--force"],
      },
    },
    { svg: { engine: false, command: false } },
    { gif: { engine: false, command: false } },

    (error, completed, statistic) => {
      console.log("reached");
      console.log(error, completed, statistic);
    }
  );
}

compressImg(filePath, saveHere);
