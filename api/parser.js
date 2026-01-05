const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = {};
  }

  async readFile() {
    try {
      const rawData = await fs.promises.readFile(this.filePath, 'utf8');
      return rawData;
    } catch (error) {
      throw new Error(`Failed to read file: ${error.message}`);
    }
  }

  async parseFile() {
    const rawData = await this.readFile();
    const lines = rawData.split('\n');
    lines.forEach((line) => {
      const [key, value] = line.split('=');
      this.data[key.trim()] = value.trim();
    });
    return this.data;
  }
}

async function main() {
  const parser = new Parser(path.join(__dirname, 'user-data.txt'));
  const userData = await parser.parseFile();
  console.log(userData);
}

main();