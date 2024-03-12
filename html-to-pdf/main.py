from weasyprint import HTML

HTML('./new.html').write_pdf('test.pdf')
