const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = null;
  }

  async readData() {
    try {
      const rawData = await fs.promises.readFile(this.filePath, 'utf8');
      this.data = JSON.parse(rawData);
    } catch (error) {
      throw new Error(`Failed to read file: ${error.message}`);
    }
  }

  async writeData(data) {
    try {
      const jsonData = JSON.stringify(data, null, 2);
      await fs.promises.writeFile(this.filePath, jsonData);
    } catch (error) {
      throw new Error(`Failed to write file: ${error.message}`);
    }
  }

  isValidData() {
    if (!this.data) return false;
    if (typeof this.data !== 'object') return false;
    return true;
  }

  getData() {
    if (!this.isValidData()) {
      throw new Error('Invalid data');
    }
    return this.data;
  }
}

module.exports = Parser;