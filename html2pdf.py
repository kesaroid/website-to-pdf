import os
import pdfkit
import xml.etree.ElementTree as ET

def extract_webpages_from_sitemap(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    webpages = []
    for child in root:
        for url in child:
            if url.tag.endswith('loc'):
                webpages.append(url.text)
                
    return webpages

def convert_webpages_to_pdf(webpage):
    options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
    }

    pdfkit.from_url(webpage, 'out.pdf', options=options)

# Example usage
xml_file = 'webpage-sitemap.xml'
webpages = extract_webpages_from_sitemap(xml_file)
print(webpages)
convert_webpages_to_pdf(webpages)
