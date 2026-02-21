$postFiles = Get-ChildItem "_posts/*.md"

foreach ($file in $postFiles) {
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content

    # Replace variations of "amp" and "&" in links with "and"
    # This targets common patterns found in Jekyll/Blogger links
    $content = $content -replace "-amp-", "-and-"
    $content = $content -replace "-&-", "-and-"

    if ($content -ne $originalContent) {
        $content | Set-Content $file.FullName -Encoding UTF8
        Write-Host "Fixed links in: $($file.Name)" -ForegroundColor Cyan
    }
}
Write-Host "Link Cleanup Complete." -ForegroundColor Green