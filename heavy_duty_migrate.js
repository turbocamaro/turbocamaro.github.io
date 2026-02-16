const fs = require('fs');
const xml2js = require('xml2js');

const parser = new xml2js.Parser();
const xmlData = fs.readFileSync('feed.atom');

// Ensure _posts directory exists
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
        // Extract Title
        const title = entry.title[0]._ || entry.title[0];
        
        // Extract Date (YYYY-MM-DD)
        const published = entry.published[0].substring(0, 10);
        
        // Extract Content - This is the "Engine Room" of the post
        let content = "";
        if (entry.content && entry.content[0]) {
            content = entry.content[0]._ || entry.content[0];
        }

        if (!content || content.trim().length === 0) {
            console.log(`Skipping ${title} (No content found)`);
            return;
        }

        // Clean title for filename (RCMP style: no special characters)
        const cleanTitle = title.replace(/[^a-zA-Z0-9\s]/g, '').replace(/\s+/g, '-').toLowerCase();
        const fileName = `_posts/${published}-${cleanTitle}.md`;

        // Build the Markdown file with Jekyll Front Matter
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