$postFiles = Get-ChildItem "_posts/*.md"

$mappings = @{
    # INTERIOR - Fixes for Console Pod, Floor Shift, Gauge Choice, Paint
    "console-pod"        = @{cat="Interior"; tags="Gauges, Console, Custom"}
    "floor-shift"        = @{cat="Interior"; tags="Transmission, Shifter, Conversion"}
    "gauge-choice"       = @{cat="Interior"; tags="Gauges, Instrumentation"}
    "paint-your-dash"    = @{cat="Interior"; tags="Paint, Dash, Restoration"}
    "alarm-system-and"   = @{cat="Interior"; tags="Security, Electrical, Locks"}
    "retrosound"         = @{cat="Interior"; tags="Audio, Stereo"}
    "scat-procar"        = @{cat="Interior"; tags="Seats"}

    # EXTERIOR - Fixes for Tail/Turn LEDS
    "tail-and-turn"      = @{cat="Exterior"; tags="Lighting, LED, Safety"}
    "tail-amp-turn"      = @{cat="Exterior"; tags="Lighting, LED, Safety"}
    "sanding-amp"        = @{cat="Exterior"; tags="Bodywork, Paint, Prep"}

    # ENGINE - Fixes for Crank/Rods and Head Mods
    "crank-and-rods"     = @{cat="Engine"; tags="Bottom End, Crank, Rods"}
    "crank-amp-rods"     = @{cat="Engine"; tags="Bottom End, Crank, Rods"}
    "head-mods-amp"      = @{cat="Engine"; tags="Cylinder Head, Porting, Flow"}
    "machine-shop"       = @{cat="Engine"; tags="Machining, Block, Engine"}

    # FUEL & TUNING - Fix for Carb selection
    "carburetor-selection" = @{cat="Fuel & Tuning"; tags="Fuel, Carburetor, Tuning"}
}

foreach ($file in $postFiles) {
    $content = Get-Content $file.FullName -Raw
    $newName = $file.Name.ToLower()
    
    # Check if file is ALREADY categorized (to avoid double-running)
    if ($content -match "categories: \[`"") {
        # Optional: Uncomment the line below if you want to force-overwrite everything again
        # $content = $content -replace "(?m)^categories:.*\r?\n?", "" -replace "(?m)^tags:.*\r?\n?", ""
    }

    $matched = $false
    foreach ($key in $mappings.Keys) {
        if ($newName -match $key) {
            # Strip old lines to ensure a clean write
            $newContent = $content -replace "(?m)^categories:.*\r?\n?", ""
            $newContent = $newContent -replace "(?m)^tags:.*\r?\n?", ""

            $cat = $mappings[$key].cat
            $tags = $mappings[$key].tags
            
            # Inject after the first '---'
            if ($newContent -match "(?s)^---\r?\n(.*?)---") {
                $insertLine = "categories: [`"$cat`"]`ntags: [$tags]`n"
                $newContent = $newContent -replace "^---", "---`n$insertLine"
                
                $newContent | Set-Content $file.FullName -Encoding UTF8
                Write-Host "Updated: $($file.Name) -> $cat" -ForegroundColor Cyan
                $matched = $true
                break
            }
        }
    }
}
Write-Host "Cleanup Complete." -ForegroundColor Green