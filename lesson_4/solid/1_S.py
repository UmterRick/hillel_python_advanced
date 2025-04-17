"""
S - single responsibility
"""

class Report:
    def generate_report(self, data):
        ...

    def transform_report(self):
        ...

    # def save_to_file(self, file):
    #     ...
    #
    # def send_by_email(self):
    #    ...
    #
    # def send_to_telegram(self):
    #     ...


"""
utils.py
report_utils.py
"""

class ReportUtils:

    @staticmethod
    def lower_to_upper(data):
        return data.upper()



class EmailProvider:

    def send_email(self):
        ...

    def send_document_by_email(self, doc):
        ...


email_sender = EmailProvider()

report = Report.generate_report({})

email_sender.send_document_by_email(report)

