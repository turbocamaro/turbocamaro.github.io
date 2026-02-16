const fs = require('fs');
const xml2js = require('xml2js'); // You might need to run: npm install xml2js

const parser = new xml2js.Parser();
const data = fs.readFileSync('feed.atom');

parser.parseString(data, (err, result) => {
    const entries = result.feed.entry;

    entries.forEach(entry => {
        const title = entry.title[0]._ || entry.title[0];
        const date = entry.published[0].substring(0, 10);
        const content = entry.content[0]._;

        if (!content) return; // Skip if no content

        const cleanTitle = title.replace(/[^a-zA-Z0-9\s]/g, '').replace(/\s+/g, '-').toLowerCase();
        const fileName = `_posts/${date}-${cleanTitle}.md`;

        const fileContent = `---
title: "${title}"
date: ${date} 12:00:00 +0000
categories: [Build]
tags: [blogger]
---

${content}`;

        fs.writeFileSync(fileName, fileContent);
        console.log(`Created: ${fileName}`);
    });
});