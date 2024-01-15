import re

cats = [
    "sims4",
    "mc",
    "rust",
    "gta4",
    "gtav",
    "stardewvalley",
    "skyrim",
    "wow",
    "gmod",
    "csgo",
    "l4d2",
    "sc2",
    "fallout4",
    "tf2",
    "cs",
    "css",
    "halomcc"
]

mapper = {
    "mc": "minecraft",
    "gta4": "gtaiv"
}

def main():
    srcPath = "urls.txt"
    
    dstPathRaw = "output_raw.txt"
    dstPathRedirect = "output_redirect.txt"
    dstPathBroken = "output_broken.txt"
    
    outputRaw = ""
    outputRedirect = ""
    outputBroken = ""
    
    totalUrls = 0
    totRedirects = 0
    
    try:
        with open(srcPath, "r") as f:
            for line in f:
                totalUrls += 1
                
                # Get current URL.
                oldUrl = line.strip()
                newUrl = oldUrl
                
                catRaw = None
                
                # Loop through each category and replace it.
                for cat in cats:
                    regex = f"^({cat}-)"
                    # Check if we have a match.
                    match = re.search(regex, newUrl)
                    
                    if match:
                        # Replace match with empty string.
                        newUrl = re.sub(regex, "", newUrl)
                        
                        # Assign our raw category.
                        catRaw = cat
                        
                        break
                
                # Write to raw.
                outputRaw += f"{oldUrl}:{newUrl}\n"
                
                # Map as redirect if needed.
                if catRaw:
                    catMapped = catRaw
                    
                    # Check for mapping.
                    if catMapped in mapper:
                        catMapped = mapper[catMapped]
                    
                    totRedirects += 1
                    
                    outputRedirect += f"/view/{oldUrl}:/{catMapped}/mod/{newUrl}\n"
                else:
                    print(f"WARNING! URL doesn't have category: {oldUrl}")
                    
                    outputBroken += f"{oldUrl}\n"
                    
        # Write to output raw.
        with open(dstPathRaw, "w") as f:
            f.write(outputRaw)
            
        # Write to output redirect.
        with open(dstPathRedirect, "w") as f:
            f.write(outputRedirect)
            
        # Write to output broken.
        with open(dstPathBroken, "w") as f:
            f.write(outputBroken)
    except Exception as e:
        print("Failed to convert URLs.")
        print(e)
        
        return
    
    print(f"Wrote {totRedirects}/{totalUrls} redirects.")
    
if __name__ == "__main__":
    main()