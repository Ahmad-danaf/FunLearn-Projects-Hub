import inquirer from 'inquirer';
import qr from 'qr-image';
import fs from 'fs';
inquirer
  .prompt([
    {
      type: 'input',
      name: 'url',
      message: 'Please enter the URL to generate a QR code:',
      validate: (input) => {
        const urlRegex = /^(ftp|http|https):\/\/[^ "]+$/;
        return urlRegex.test(input) || 'Please enter a valid URL.';
      },
    },
  ])
  .then((answers) => {
    // Use the URL from the answers
    console.log(`You entered the URL: ${answers.url}`);

    var qr_png = qr.image(answers.url);
    qr_png.pipe(fs.createWriteStream('qr-code-img.png'));

    fs.writeFile("URL.txt", answers.url, (err) => {
        if (err) throw err;
        console.log("The URL file has been saved!");
      });

  })
  .catch((error) => {
    if (error.isTtyError) {
      // Prompt couldn't be rendered in the current environment
      console.error('Prompt couldn\'t be rendered in the current environment');
    } else {
      // Something else went wrong
      console.error('An error occurred:', error);
    }
  });
