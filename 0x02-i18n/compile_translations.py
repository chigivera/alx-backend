#!/usr/bin/env python3
"""
Compile translation files for the Flask application.
"""
from babel.messages.frontend import compile_catalog
import os

def compile_translations():
    """Compile all translation files."""
    for lang in ['en', 'fr']:
        po_file = f'translations/{lang}/LC_MESSAGES/messages.po'
        mo_file = f'translations/{lang}/LC_MESSAGES/messages.mo'
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(po_file), exist_ok=True)
        
        # Compile the translation file
        compiler = compile_catalog()
        compiler.input_file = po_file
        compiler.output_file = mo_file
        compiler.run()

if __name__ == '__main__':
    compile_translations() 