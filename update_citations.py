#!/usr/bin/env python3
"""
Script to update publication citations to format venue in italics
"""

import os
import re
import glob

def update_citation(citation, venue):
    """
    Update citation to make the venue italic
    Format: Authors. <b>Title</b>, <i>Venue</i>, Year
    """
    if not venue or venue == '':
        return citation
    
    # Replace plain venue with italic venue if venue is present
    # Pattern: After </b> and before the year
    if venue in citation and f'<i>{venue}</i>' not in citation:
        citation = citation.replace(f' {venue},', f' <i>{venue}</i>,')
        citation = citation.replace(f' {venue} ', f' <i>{venue}</i> ')
        return citation
    
    return citation

def process_publication_file(filepath):
    """
    Process a single publication markdown file
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract venue
    venue_match = re.search(r"^venue:\s*['\"]([^'\"]+)['\"]", content, re.MULTILINE)
    venue = venue_match.group(1) if venue_match else None
    
    # Find the citation line
    citation_match = re.search(r"^citation:\s*['\"](.+?)['\"](?:\s*$|\s*\n)", content, re.MULTILINE | re.DOTALL)
    
    if citation_match and venue:
        old_citation = citation_match.group(1)
        new_citation = update_citation(old_citation, venue)
        
        if old_citation != new_citation:
            # Replace the old citation with the new one
            content = content.replace(f"citation: '{old_citation}'", f"citation: '{new_citation}'")
            content = content.replace(f'citation: "{old_citation}"', f'citation: "{new_citation}"')
            content = content.replace(f"citation: ' {old_citation}'", f"citation: '{new_citation}'")
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Updated: {os.path.basename(filepath)}")
            return True
        else:
            print(f"Already formatted: {os.path.basename(filepath)}")
    else:
        print(f"Skipped: {os.path.basename(filepath)}")
    
    return False

def main():
    """
    Main function to process all publication files
    """
    # Get all publication markdown files
    pub_dir = "_publications"
    pub_files = glob.glob(os.path.join(pub_dir, "*.md"))
    
    print(f"Found {len(pub_files)} publication files\n")
    
    updated_count = 0
    for filepath in sorted(pub_files):
        if process_publication_file(filepath):
            updated_count += 1
    
    print(f"\nTotal updated: {updated_count} files")

if __name__ == "__main__":
    main()
