const fs = require('fs');
const xml2js = require('xml2js');

const parser = new xml2js.Parser();
const xmlData = fs.readFileSync('feed.atom');

if (!fs.existsSync('_posts')) {
    fs.mkdirSync('_posts');
}

parser.parseString(xmlData, (err, result) => {
    if (err) {
        console.error("Error parsing XML:", err);
        return;
    }

    const entries = result.feed.entry;
    console.log(`Found ${entries.length} entries. Starting conversion...`);

    entries.forEach(entry => {
        const title = entry.title[0]._ || entry.title[0] || "Untitled Post";
        const published = entry.published[0].substring(0, 10);
        
        // Rugged content extraction
        let rawContent = "";
        if (entry.content && entry.content[0]) {
            rawContent = entry.content[0]._ || entry.content[0];
        }

        // Force to string to prevent the .trim() crash
        let content = String(rawContent);

        if (!content || content.trim().length === 0 || content === "[object Object]") {
            console.log(`Skipping ${title} (No readable text/HTML)`);
            return;
        }

        const cleanTitle = title.replace(/[^a-zA-Z0-9\s]/g, '').replace(/\s+/g, '-').toLowerCase();
        const fileName = `_posts/${published}-${cleanTitle}.md`;

        const fileData = `---
title: "${title}"
date: ${published} 12:00:00 +0000
categories: [Migration]
tags: [blogger]
---

${content}`;

        fs.writeFileSync(fileName, fileData);
        console.log(`Success: ${fileName}`);
    });

    console.log("Migration complete. Check your _posts folder.");
});