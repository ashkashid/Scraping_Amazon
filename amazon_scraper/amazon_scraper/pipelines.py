from openpyxl import Workbook

class ExcelWriterPipeline:
    def __init__(self):
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.append(['Name', 'Processor', 'RAM', 'Storage', 'Display', 'Camera', 'Battery'])

    def process_item(self, item, spider):
        row = [
            item['name'],
            item['processor'],
            item['ram'],
            item['storage'],
            item['display'],
            item['camera'],
            item['battery']
        ]
        self.sheet.append(row)
        return item

    def close_spider(self, spider):
        self.workbook.save('mobile_phones.xlsx')
