"""Distinct Python example #41."""
import xml.etree.ElementTree as ET
root=ET.fromstring("<item><name>Pen</name></item>"); print({c.tag:c.text for c in root})
