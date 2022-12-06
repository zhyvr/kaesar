const alphabet = "ێیەھۆونمڵلگکقڤفغعشسژزڕردخحچجتپبائ";
let output ="";

function encrypt(text, key) {
  for (let char of text) {
    if (alphabet.includes(char)) {
      let position = alphabet.indexOf(char);
      let newPosition = (position + key) % 33;
      let newChar = alphabet[newPosition];
      output += newChar;
    } else {
      output += char;
    }
  }
  return output;
}
function decrypt(text, key) {
  for (let char of text) {
    if (alphabet.includes(char)) {
      let position = alphabet.indexOf(char);
      let newPosition = (position - key) % 33;
      let originalChar = alphabet[newPosition];
      output += originalChar;
    } else {
      output += char;
    }
  }
  return output;
} 
//شتێک بنووسە
const text = "بردنەوە";
const key = 3; //کلیل
console.log(encrypt(text, key)); // بۆ ئینکریپت
//console.log(decrypt(text, key)); //بۆ دیکریپت
