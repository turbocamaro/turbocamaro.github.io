const fs = require('fs');

const inputFile = 'feed.atom';
const outputDir = '_posts';

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
}

const data = fs.readFileSync(inputFile, 'utf8');

// This splits the file into individual <entry> blocks
const entries = data.split('<entry>');
// Remove the first chunk (it's just the feed header)
entries.shift();

console.log(`Found ${entries.length} entries. Starting brute-force migration...`);

entries.forEach(entry => {
    // 1. Get Title
    const titleMatch = entry.match(/<title type="text">(.*?)<\/title>/);
    const title = titleMatch ? titleMatch[1] : "Untitled Post";

    // 2. Get Date
    const dateMatch = entry.match(/<published>(.*?)T/);
    const date = dateMatch ? dateMatch[1] : "2026-01-01";

    // 3. Get Content (The raw HTML including <img> tags)
    // This looks for everything between <content type='html'> and </content>
    const contentMatch = entry.match(/<content type='html'>([\s\S]*?)<\/content>/);
    let content = contentMatch ? contentMatch[1] : "";

    if (!content) return;

    // Clean filename
    const cleanTitle = title.replace(/[^a-zA-Z0-9\s]/g, '').replace(/\s+/g, '-').toLowerCase();
    const fileName = `${outputDir}/${date}-${cleanTitle}.md`;

    const fileData = `---
title: "${title}"
date: ${date} 12:00:00 +0000
categories: [Migration]
tags: [blogger]
---

${content}`;

    fs.writeFileSync(fileName, fileData);
    console.log(`Successfully pulled: ${fileName}`);
});

console.log("Brute force complete. Check your _posts folder.");