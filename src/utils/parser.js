const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
  }

  async parseFile() {
    try {
      const data = await fs.promises.readFile(this.filePath, 'utf8');
      return this.parseData(data);
    } catch (error) {
      throw new Error(`Failed to read file: ${error.message}`);
    }
  }

  parseData(data) {
    const lines = data.split('\n');
    const parsedData = [];
    lines.forEach((line) => {
      const [key, value] = line.split('=');
      if (key && value) {
        parsedData.push({ [key.trim()]: value.trim() });
      }
    });
    return parsedData;
  }
}

module.exports = Parser;