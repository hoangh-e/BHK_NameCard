#!/usr/bin/env python3
"""
PowerApps YAML Control Version Remover

This script removes version numbers from PowerApps YAML control declarations.
It processes the file and replaces versioned control names with clean versions.

Usage: python remove_control_versions.py <file_path>
Example: python remove_control_versions.py UserManagementScreen.yaml
"""

import re
import sys
import os
from pathlib import Path

# Dictionary mapping versioned controls to clean versions
CONTROL_VERSION_MAPPING = {
    # GroupContainer versions
    r'GroupContainer@\d+\.\d+\.\d+': 'GroupContainer',
    
    # Label versions
    r'Label@\d+\.\d+\.\d+': 'Label',
    
    # Button versions
    r'Classic/Button@\d+\.\d+\.\d+': 'Classic/Button',
    
    # TextInput versions
    r'Classic/TextInput@\d+\.\d+\.\d+': 'Classic/TextInput',
    
    # DropDown versions
    r'DropDown@\d+\.\d+\.\d+': 'DropDown',
    
    # Rectangle versions
    r'Rectangle@\d+\.\d+\.\d+': 'Rectangle',
    
    # Icon versions
    r'Classic/Icon@\d+\.\d+\.\d+': 'Classic/Icon',
    
    # DataTable versions
    r'DataTable@\d+\.\d+\.\d+': 'DataTable',
    
    # DataTableColumn versions
    r'DataTableColumn@\d+\.\d+\.\d+': 'DataTableColumn',
    
    # Image versions
    r'Image@\d+\.\d+\.\d+': 'Image',
    
    # Gallery versions
    r'Gallery@\d+\.\d+\.\d+': 'Gallery',
    
    # Form versions
    r'Form@\d+\.\d+\.\d+': 'Form',
    
    # Timer versions
    r'Timer@\d+\.\d+\.\d+': 'Timer',
    
    # Slider versions
    r'Slider@\d+\.\d+\.\d+': 'Slider',
    
    # Toggle versions
    r'Toggle@\d+\.\d+\.\d+': 'Toggle',
    
    # DatePicker versions
    r'DatePicker@\d+\.\d+\.\d+': 'DatePicker',
    
    # ComboBox versions
    r'ComboBox@\d+\.\d+\.\d+': 'ComboBox',
    
    # ListBox versions
    r'ListBox@\d+\.\d+\.\d+': 'ListBox',
    
    # Rating versions
    r'Rating@\d+\.\d+\.\d+': 'Rating',
    
    # Audio versions
    r'Audio@\d+\.\d+\.\d+': 'Audio',
    
    # Video versions
    r'Video@\d+\.\d+\.\d+': 'Video',
    
    # Camera versions
    r'Camera@\d+\.\d+\.\d+': 'Camera',
    
    # Barcode versions
    r'BarcodeScanner@\d+\.\d+\.\d+': 'BarcodeScanner',
    
    # Microphone versions
    r'Microphone@\d+\.\d+\.\d+': 'Microphone',
    
    # AddMediaButton versions
    r'AddMediaButton@\d+\.\d+\.\d+': 'AddMediaButton',
    
    # Export versions
    r'Export@\d+\.\d+\.\d+': 'Export',
    
    # Import versions
    r'Import@\d+\.\d+\.\d+': 'Import',
    
    # PDF Viewer versions
    r'PdfViewer@\d+\.\d+\.\d+': 'PdfViewer',
    
    # Power BI Tile versions
    r'PowerBITile@\d+\.\d+\.\d+': 'PowerBITile',
    
    # Stream versions
    r'Stream@\d+\.\d+\.\d+': 'Stream',
    
    # Rich Text Editor versions
    r'RichTextEditor@\d+\.\d+\.\d+': 'RichTextEditor',
    
    # HTML Text versions
    r'HtmlText@\d+\.\d+\.\d+': 'HtmlText',
    
    # Pen Input versions
    r'PenInput@\d+\.\d+\.\d+': 'PenInput',
    
    # Attachments versions
    r'Attachments@\d+\.\d+\.\d+': 'Attachments',
}

def remove_control_versions(file_path):
    """
    Remove version numbers from PowerApps YAML control declarations.
    
    Args:
        file_path (str): Path to the YAML file to process
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"❌ Error: File '{file_path}' not found!")
            return False
        
        # Read the file content
        print(f"📖 Reading file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        replacements_made = 0
        
        # Apply each replacement pattern
        print("🔄 Processing control version replacements...")
        for pattern, replacement in CONTROL_VERSION_MAPPING.items():
            # Count matches before replacement
            matches = re.findall(pattern, content)
            if matches:
                print(f"  ├─ Found {len(matches)} instances of pattern: {pattern}")
                # Replace the pattern
                content = re.sub(pattern, replacement, content)
                replacements_made += len(matches)
        
        # Check if any changes were made
        if content == original_content:
            print("ℹ️  No version numbers found to remove.")
            return True
        
        # Create backup of original file
        backup_path = f"{file_path}.backup"
        print(f"💾 Creating backup: {backup_path}")
        with open(backup_path, 'w', encoding='utf-8') as backup_file:
            backup_file.write(original_content)
        
        # Write the updated content back to file
        print(f"✏️  Writing cleaned content back to: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"✅ Successfully removed {replacements_made} version numbers!")
        print(f"📁 Original file backed up to: {backup_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing file: {str(e)}")
        return False

def main():
    """Main function to handle command line arguments and execute the script."""
    
    # Check command line arguments
    if len(sys.argv) != 2:
        print("🔧 PowerApps YAML Control Version Remover")
        print("=" * 50)
        print("Usage: python remove_control_versions.py <file_path>")
        print("Example: python remove_control_versions.py UserManagementScreen.yaml")
        print("\nThis script will:")
        print("  • Remove version numbers from all PowerApps control declarations")
        print("  • Create a backup of the original file (.backup extension)")
        print("  • Update the file with clean control names")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    print("🔧 PowerApps YAML Control Version Remover")
    print("=" * 50)
    print(f"Target file: {file_path}")
    print()
    
    # Process the file
    success = remove_control_versions(file_path)
    
    if success:
        print("\n🎉 Process completed successfully!")
    else:
        print("\n💥 Process failed!")
        sys.exit(1)
